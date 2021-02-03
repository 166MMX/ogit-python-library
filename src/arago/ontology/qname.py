from dataclasses import dataclass

from arago.ontology.utils import to_constant

NAMESPACE_BASE_URI = 'http://www.purl.org/'


@dataclass(frozen=True)
class Prefix:
    full_name: str

    @property
    def full_uri(self) -> str:
        return self.base_uri + self.uri

    @property
    def base_uri(self) -> str:
        return NAMESPACE_BASE_URI

    @property
    def uri(self) -> str:
        prefix = self.full_name
        if prefix.startswith('ogit.'):
            prefix = prefix.replace('.', '/')

        return f'{prefix}'

    @property
    def constant(self) -> str:
        return to_constant(self.uri)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, str):
            return \
                self.uri == o or \
                self.full_uri == o or \
                self.full_name == o
        return super().__eq__(o)

    def __hash__(self) -> int:
        return hash(self.full_name)

    def __repr__(self) -> str:
        return f'''{self.__class__.__name__}('{self.full_name}')'''


# https://www.w3.org/TR/turtle/#prefixed-name

@dataclass(frozen=True)
class QName:
    full_name: str

    @property
    def prefix(self) -> str:
        name = self.full_name
        if ':' in name:
            colon_idx = name.rindex(':')
            return name[:colon_idx]
        else:
            return ''

    @property
    def name(self) -> str:
        name = self.full_name
        if ':' in name:
            colon_idx = name.rindex(':')
            return name[colon_idx + 1:]
        else:
            return name

    @property
    def full_uri(self) -> str:
        return self.base_uri + self.uri

    @property
    def base_uri(self) -> str:
        return NAMESPACE_BASE_URI

    @property
    def uri(self) -> str:
        prefix = self.prefix
        if prefix.startswith('ogit.'):
            prefix = prefix.replace('.', '/')

        return f'{prefix}/{self.name}'

    @property
    def constant(self) -> str:
        return to_constant(self.uri)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, str):
            return \
                self.uri == o or \
                self.full_uri == o or \
                self.full_name == o
        return super().__eq__(o)

    def __hash__(self) -> int:
        return hash(self.full_name)

    def __repr__(self) -> str:
        return f'''{self.__class__.__name__}('{self.full_name}')'''

    #    	QName	           ::=   PrefixedName | UnprefixedName
    #    	PrefixedName	   ::=   Prefix ':' LocalPart
    #    	UnprefixedName     ::=   LocalPart
