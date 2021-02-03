from itertools import combinations

import pytest

from arago.ogit import OgitAttribute


@pytest.mark.parametrize('a,b', combinations((
        OgitAttribute.OGIT_NAME,
        'http://www.purl.org/ogit/name',
        'ogit/name',
        'ogit:name'
), 2))
def test_attribute(a, b):
    if isinstance(a, str):
        a = OgitAttribute[a]
    if isinstance(b, str):
        b = OgitAttribute[b]
    assert id(a) == id(b)


@pytest.mark.parametrize('a,b', combinations((
        OgitAttribute.OGIT_NAME.value,
        'http://www.purl.org/ogit/name',
        'ogit/name',
        'ogit:name'
), 2))
def test_attribute_value(a, b):
    if isinstance(a, str):
        a = OgitAttribute[a]
        a = a.value
    if isinstance(b, str):
        b = OgitAttribute[b]
        b = b.value
    assert id(a) == id(b)

