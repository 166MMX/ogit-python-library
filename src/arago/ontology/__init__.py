import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import unique, Enum, auto
from typing import Optional, FrozenSet, Type, Mapping, Set, Tuple, Final

from arago.ontology.dc import DCTermsValid
from arago.ontology.qname import QName
from arago.ontology.utils import to_constant

NAMESPACE_BASE_URI = 'http://www.purl.org/'


@dataclass(frozen=True)
class OntologyNamespace:
    prefix: str
    parent: Optional['OntologyNamespace'] = field(default=None, init=False, hash=False, compare=False)

    def __post_init__(self):
        object.__setattr__(self, '_Namespace__hot', True)

    def finalize(self, namespaces: Mapping[str, 'OntologyNamespace']):
        if not hasattr(self, '_Namespace__hot'):
            return

        prefix = self.prefix
        if '.' in prefix:
            i = prefix.rindex('.')
            parent_prefix = prefix[:i]
            if parent_prefix:
                constant = to_constant(parent_prefix).replace('.', '_')
                parent = namespaces[constant]
                object.__setattr__(self, 'parent', parent)
        object.__delattr__(self, '_Namespace__hot')

    @property
    def uri(self) -> str:
        return self.prefix.replace('.', '/')

    @property
    def full_uri(self) -> str:
        return NAMESPACE_BASE_URI + self.uri + '/'


@dataclass(frozen=True)
class Named(ABC):
    name: QName  # @rdf:about


class NamedEnum(Enum):
    value: Named


@unique
class Cardinality(Enum):
    MANY_TO_MANY = auto()

    def __repr__(self):
        # https://docs.python.org/3/library/enum.html#omitting-values
        return '<%s.%s>' % (self.__class__.__name__, self.name)


@dataclass(frozen=True)
class OntologyVerb(Named):
    label: Optional[str] = field(default=None, hash=False, compare=False)  # rdfs:label
    description: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:description

    valid: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:valid

    created_at: Optional[datetime] = field(default=None, hash=False, compare=False)  # dcterms:created
    modified_at: Optional[datetime] = field(default=None, hash=False, compare=False)  # dcterms:modified
    valid_from: Optional[datetime] = field(default=None, hash=False, compare=False)
    valid_until: Optional[datetime] = field(default=None, hash=False, compare=False)
    hide: bool = field(default=False, hash=False, compare=False)  # ogit:hide

    created_by: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:creator
    deleted_by: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:deleter
    admin_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:admin-contact
    tech_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:tech-contact

    cardinality: Optional[Cardinality] = field(default=None, hash=False, compare=False)  # ogit:cardinality


@dataclass(frozen=True)
class TurtleVerb:
    about: str  # @rdf:about
    label: Optional[str] = field(default=None, hash=False, compare=False)  # rdfs:label
    description: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:description

    valid: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:valid

    created_at: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:created
    modified_at: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:modified
    hide: bool = field(default=False, hash=False, compare=False)  # ogit:hide

    created_by: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:creator
    deleted_by: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:deleter
    admin_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:admin-contact
    tech_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:tech-contact

    cardinality: Optional[Cardinality] = field(default=None, hash=False, compare=False)  # ogit:cardinality

    def as_model(self) -> OntologyVerb:
        name = QName(self.about)
        created_at = datetime.fromisoformat(self.created_at) if self.created_at else self.created_at
        modified_at = datetime.fromisoformat(self.modified_at) if self.modified_at else self.modified_at
        dc_terms_valid = DCTermsValid.parse(self.valid) if self.valid is not None else None
        valid_from = dc_terms_valid.start if dc_terms_valid is not None else None
        valid_until = dc_terms_valid.end if dc_terms_valid is not None else None
        return OntologyVerb(
            name=name,
            label=self.label,
            description=self.description,

            valid=self.valid,

            created_at=created_at,
            modified_at=modified_at,
            valid_from=valid_from,
            valid_until=valid_until,
            hide=self.hide,

            created_by=self.created_by,
            deleted_by=self.deleted_by,
            admin_contact=self.admin_contact,
            tech_contact=self.tech_contact,

            cardinality=self.cardinality,
        )


@unique
class ValidatorType(Enum):
    FIXED = auto()
    REGEX = auto()

    def __repr__(self):
        # https://docs.python.org/3/library/enum.html#omitting-values
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class Validator(ABC):
    __slots__ = ()

    @abstractmethod
    def __call__(self, value: str) -> bool:
        ...

    @property
    @abstractmethod
    def type(self) -> ValidatorType:
        ...


class FixedValidator(Validator):
    __values: Final[FrozenSet[str]]
    __pattern: Final[re.Pattern] = re.compile(r'\s*,\s*')

    __slots__ = '__values'

    def __init__(self, values: str) -> None:
        super().__init__()
        values = values.strip()
        lst = FixedValidator.__pattern.split(values)
        self.__values = frozenset(lst)

    def __call__(self, value: str) -> bool:
        return value in self.__values

    def type(self) -> ValidatorType:
        return ValidatorType.FIXED


class RegExpValidator(Validator):
    __pattern: Final[re.Pattern]

    __slots__ = '__pattern'

    def __init__(self, expression: str) -> None:
        super().__init__()
        self.__pattern = re.compile(expression)

    def __call__(self, value: str) -> bool:
        return self.__pattern.fullmatch(value) is not None

    def type(self) -> ValidatorType:
        return ValidatorType.REGEX


@dataclass(frozen=True)
class Attribute(ABC):
    name: QName  # @rdf:about


@dataclass(frozen=True)
class OntologyAttribute(Attribute, Named):
    label: Optional[str] = field(default=None, hash=False, compare=False)  # rdfs:label
    description: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:description

    valid: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:valid
    validation_type: Optional[ValidatorType] = field(default=None, hash=False, compare=False)  # ogit:validation-type
    validation_parameter: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:validation-parameter
    validation: Optional[Validator] = field(default=None, hash=False, compare=False)

    created_at: Optional[datetime] = field(default=None, hash=False, compare=False)  # dcterms:created
    modified_at: Optional[datetime] = field(default=None, hash=False, compare=False)  # dcterms:modified
    valid_from: Optional[datetime] = field(default=None, hash=False, compare=False)
    valid_until: Optional[datetime] = field(default=None, hash=False, compare=False)
    hide: bool = field(default=False, hash=False, compare=False)  # ogit:hide

    created_by: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:creator
    deleted_by: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:deleter
    admin_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:admin-contact
    tech_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:tech-contact

    def __repr__(self) -> str:
        return f'''{self.__class__.__name__}('{self.name.full_name}')'''


def _create_validator(
        validation_type: Optional[str],
        validation_parameter: Optional[str],
) -> Optional[Validator]:
    if validation_type is None and validation_parameter is None:
        return None
    elif validation_type is None or validation_parameter is None:
        raise RuntimeError('Either both or none of must be set: validation_type and validation_parameter')
    elif validation_type is ValidatorType.FIXED:
        return FixedValidator(validation_parameter)
    elif validation_type is ValidatorType.REGEX:
        return RegExpValidator(validation_parameter)
    else:
        raise RuntimeError(f"Unknown validation_type: '{validation_type}'")


@dataclass(frozen=True)
class TurtleAttribute:
    about: str  # @rdf:about
    label: Optional[str] = field(default=None, hash=False, compare=False)  # rdfs:label
    description: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:description

    valid: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:valid
    validation_type: Optional[ValidatorType] = field(default=None, hash=False, compare=False)  # ogit:validation-type
    validation_parameter: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:validation-parameter

    created_at: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:created
    modified_at: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:modified
    hide: bool = field(default=False, hash=False, compare=False)  # ogit:hide

    created_by: Optional[str] = field(default=None, hash=False, compare=False)  # dcterms:creator
    deleted_by: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:deleter
    admin_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:admin-contact
    tech_contact: Optional[str] = field(default=None, hash=False, compare=False)  # ogit:tech-contact

    def as_model(self) -> OntologyAttribute:
        name = QName(self.about)
        validation = _create_validator(self.validation_type, self.validation_parameter)
        created_at = datetime.fromisoformat(self.created_at) if self.created_at else self.created_at
        modified_at = datetime.fromisoformat(self.modified_at) if self.modified_at else self.modified_at
        dc_terms_valid = DCTermsValid.parse(self.valid) if self.valid is not None else None
        valid_from = dc_terms_valid.start if dc_terms_valid is not None else None
        valid_until = dc_terms_valid.end if dc_terms_valid is not None else None
        return OntologyAttribute(
            name=name,
            label=self.label,
            description=self.description,

            valid=self.valid,
            validation_type=self.validation_type,
            validation_parameter=self.validation_parameter,
            validation=validation,

            created_at=created_at,
            modified_at=modified_at,
            valid_from=valid_from,
            valid_until=valid_until,
            hide=self.hide,

            created_by=self.created_by,
            deleted_by=self.deleted_by,
            admin_contact=self.admin_contact,
            tech_contact=self.tech_contact,
        )


@unique
class Scope(Enum):
    NTO = auto()
    SGO = auto()

    def __repr__(self):
        # https://docs.python.org/3/library/enum.html#omitting-values
        return '<%s.%s>' % (self.__class__.__name__, self.name)


@dataclass(frozen=True)
class AllowedConnection:
    verb: OntologyVerb
    entity: 'OntologyEntity'


@dataclass(frozen=True)
class OntologyEntity(Named):
    label: str = field(
        hash=False, compare=False)  # rdfs:label
    description: str = field(
        hash=False, compare=False)  # dcterms:description

    scope: Scope = field(
        hash=False, compare=False)  # ogit:scope  # immutable!

    valid: Optional[str] = field(
        default=None, repr=False, hash=False, compare=False)  # dcterms:valid

    created_at: Optional[datetime] = field(
        default=None, hash=False, compare=False)  # dcterms:created
    modified_at: Optional[datetime] = field(
        default=None, hash=False, compare=False)  # dcterms:modified
    valid_from: Optional[datetime] = field(
        default=None, hash=False, compare=False)
    valid_until: Optional[datetime] = field(
        default=None, hash=False, compare=False)
    hide: bool = field(
        default=False, hash=False, compare=False)  # ogit:hide

    created_by: Optional[str] = field(
        default=None, hash=False, compare=False)  # dcterms:creator
    deleted_by: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:deleter
    admin_contact: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:admin-contact
    tech_contact: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:tech-contact

    parent: Optional['OntologyEntity'] = field(
        default=None, init=False, repr=False, hash=False, compare=False)  # ogit:parent

    required_attributes: FrozenSet[OntologyAttribute] = field(
        default_factory=frozenset, init=False, repr=False, hash=False, compare=False)
    optional_attributes: FrozenSet[OntologyAttribute] = field(
        default_factory=frozenset, init=False, repr=False, hash=False, compare=False)
    indexed_attributes: FrozenSet[OntologyAttribute] = field(
        default_factory=frozenset, init=False, repr=False, hash=False, compare=False)
    # https://github.com/arago/OGIT/blob/master/ogit.ttl#L135
    allowed_connections: FrozenSet[AllowedConnection] = field(
        default_factory=frozenset, init=False, repr=False, hash=False, compare=False)

    def __post_init__(self):
        object.__setattr__(self, '_Entity__hot', True)

    def finalize(
            self,
            turtle: 'TurtleEntity',
            attributes: Type[Enum],
            verbs: Type[Enum],
            entities: Mapping[str, 'OntologyEntity']
    ):
        if not hasattr(self, '_Entity__hot'):
            return

        if turtle.parent is not None:
            k = QName(turtle.parent).constant
            parent = entities[k]
            object.__setattr__(self, 'parent', parent)
        if turtle.required_attributes is not None:
            required_attributes = frozenset({
                attributes[a].value for a in turtle.required_attributes
            })
            object.__setattr__(self, 'required_attributes', required_attributes)
        if turtle.optional_attributes is not None:
            optional_attributes = frozenset({
                attributes[a].value for a in turtle.optional_attributes
            })
            object.__setattr__(self, 'optional_attributes', optional_attributes)
        if turtle.indexed_attributes is not None:
            indexed_attributes = frozenset({
                attributes[a].value for a in turtle.indexed_attributes
            })
            object.__setattr__(self, 'indexed_attributes', indexed_attributes)
        if turtle.allowed_connections is not None:
            allowed_connections = frozenset({
                AllowedConnection(verbs[v].value, entities[QName(e).constant]) for v, e in turtle.allowed_connections
            })
            object.__setattr__(self, 'allowed_connections', allowed_connections)
        object.__delattr__(self, '_Entity__hot')

    def __eq__(self, o: object) -> bool:
        if isinstance(o, OntologyEntity):
            return self.name == o.name
        if isinstance(o, NamedEnum):
            return self.name == o.value.name

        return False

    def __repr__(self) -> str:
        return f'''{self.__class__.__name__}('{self.name.full_name}')'''


@dataclass(frozen=True)
class TurtleEntity:
    about: str  # @rdf:about
    scope: Optional[Scope] = field(
        default=None, hash=False, compare=False)  # ogit:scope

    label: Optional[str] = field(
        default=None, hash=False, compare=False)  # rdfs:label
    description: Optional[str] = field(
        default=None, hash=False, compare=False)  # dcterms:description

    valid: Optional[str] = field(
        default=None, hash=False, compare=False)  # dcterms:valid

    created_at: Optional[str] = field(
        default=None, hash=False, compare=False)  # dcterms:created
    modified_at: Optional[str] = field(
        default=None, hash=False, compare=False)  # dcterms:modified
    hide: bool = field(
        default=False, hash=False, compare=False)  # ogit:hide

    created_by: Optional[str] = field(
        default=None, hash=False, compare=False)  # dcterms:creator
    deleted_by: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:deleter
    admin_contact: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:admin-contact
    tech_contact: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:tech-contact

    parent: Optional[str] = field(
        default=None, hash=False, compare=False)  # ogit:parent

    required_attributes: Set[str] = field(
        default_factory=set, hash=False, compare=False)  # ogit:mandatory-attributes
    optional_attributes: Set[str] = field(
        default_factory=set, hash=False, compare=False)  # ogit:optional-attributes
    indexed_attributes: Set[str] = field(
        default_factory=set, hash=False, compare=False)  # ogit:indexed-attributes
    allowed_connections: Set[Tuple[str, str]] = field(
        default_factory=set, hash=False, compare=False)  # ogit:allowed

    # namespace_enum: TypedEnum[OntologyNamespace]
    def as_model(self) -> OntologyEntity:
        name = QName(self.about)
        created_at = datetime.fromisoformat(self.created_at) if self.created_at else self.created_at
        modified_at = datetime.fromisoformat(self.modified_at) if self.modified_at else self.modified_at
        dc_terms_valid = DCTermsValid.parse(self.valid) if self.valid is not None else None
        valid_from = dc_terms_valid.start if dc_terms_valid is not None else None
        valid_until = dc_terms_valid.end if dc_terms_valid is not None else None
        return OntologyEntity(
            name=name,
            label=self.label,
            description=self.description,

            scope=self.scope,

            valid=self.valid,

            created_at=created_at,
            modified_at=modified_at,
            valid_from=valid_from,
            valid_until=valid_until,
            hide=self.hide,

            created_by=self.created_by,
            deleted_by=self.deleted_by,
            admin_contact=self.admin_contact,
            tech_contact=self.tech_contact,
        )
