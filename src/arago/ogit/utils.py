from typing import Generator, Type, Callable, Iterable, TypeVar

from arago.ontology import NamedEnum

_NAMED_ENUM_T_co = TypeVar('_NAMED_ENUM_T_co', covariant=True)


def add_aliases(enum_class: Type[_NAMED_ENUM_T_co], gen_factory: Callable[[_NAMED_ENUM_T_co], Iterable[str]]):
    set_attr = type.__setattr__
    # noinspection PyProtectedMember
    member_map = enum_class._member_map_
    enum_member: NamedEnum
    for enum_member in enum_class:
        for alias_name in gen_factory(enum_member):
            set_attr(enum_class, alias_name, enum_member)
            member_map[alias_name] = enum_member


def named_aliases(enum_member: NamedEnum) -> Generator[str, None, None]:
    name = enum_member.value.name
    yield name.full_name
    yield name.uri
    yield name.full_uri
