import enum


# noinspection PyProtectedMember,SpellCheckingInspection
def patched__new__(metacls, cls, bases, classdict):
    # an Enum class is final once enumeration items have been defined; it
    # cannot be mixed with other types (int, float, etc.) if it has an
    # inherited __new__ unless a new __new__ is defined (or the resulting
    # class will fail).
    #
    # remove any keys listed in _ignore_
    classdict.setdefault('_ignore_', []).append('_ignore_')
    ignore = classdict['_ignore_']
    for key in ignore:
        classdict.pop(key, None)
    member_type, first_enum = metacls._get_mixins_(cls, bases)
    __new__, save_new, use_args = metacls._find_new_(classdict, member_type,
                                                     first_enum)

    # save enum items into separate mapping so they don't get baked into
    # the new class
    enum_members = {k: classdict[k] for k in classdict._member_names}
    for name in classdict._member_names:
        del classdict[name]

    # adjust the sunders
    _order_ = classdict.pop('_order_', None)

    # check for illegal enum names (any others?)
    invalid_names = set(enum_members) & {'mro', ''}
    if invalid_names:
        raise ValueError('Invalid enum member name: {0}'.format(
            ','.join(invalid_names)))

    # create a default docstring if one has not been provided
    if '__doc__' not in classdict:
        classdict['__doc__'] = 'An enumeration.'

    # create our new Enum type
    enum_class = type.__new__(metacls, cls, bases, classdict)
    enum_class._member_names_ = []  # names in definition order
    enum_class._member_map_ = {}  # name->value map
    enum_class._member_type_ = member_type

    # save DynamicClassAttribute attributes from super classes so we know
    # if we can take the shortcut of storing members in the class dict
    dynamic_attributes = {k for c in enum_class.mro()
                          for k, v in c.__dict__.items()
                          if isinstance(v, enum.DynamicClassAttribute)}

    # Reverse value->name map for hashable values.
    enum_class._value2member_map_ = {}

    # If a custom type is mixed into the Enum, and it does not know how
    # to pickle itself, pickle.dumps will succeed but pickle.loads will
    # fail.  Rather than have the error show up later and possibly far
    # from the source, sabotage the pickle protocol for this class so
    # that pickle.dumps also fails.
    #
    # However, if the new class implements its own __reduce_ex__, do not
    # sabotage -- it's on them to make sure it works correctly.  We use
    # __reduce_ex__ instead of any of the others as it is preferred by
    # pickle over __reduce__, and it handles all pickle protocols.
    if '__reduce_ex__' not in classdict:
        if member_type is not object:
            methods = ('__getnewargs_ex__', '__getnewargs__',
                       '__reduce_ex__', '__reduce__')
            if not any(m in member_type.__dict__ for m in methods):
                enum._make_class_unpicklable(enum_class)

    member_values = set()

    # instantiate them, checking for duplicates as we go
    # we instantiate first instead of checking for duplicates first in case
    # a custom __new__ is doing something funky with the values -- such as
    # auto-numbering ;)
    for member_name in classdict._member_names:
        value = enum_members[member_name]
        if not isinstance(value, tuple):
            args = (value,)
        else:
            args = value
        if member_type is tuple:  # special case for tuple enums
            args = (args,)  # wrap it one more time
        if not use_args:
            enum_member = __new__(enum_class)
            if not hasattr(enum_member, '_value_'):
                enum_member._value_ = value
        else:
            enum_member = __new__(enum_class, *args)
            if not hasattr(enum_member, '_value_'):
                if member_type is object:
                    enum_member._value_ = value
                else:
                    enum_member._value_ = member_type(*args)
        value = enum_member._value_
        enum_member._name_ = member_name
        enum_member.__objclass__ = enum_class
        enum_member.__init__(*args)
        # If another member with the same value was already defined, the
        # new member becomes an alias to the existing one.
        if value in member_values:
            for name, canonical_member in enum_class._member_map_.items():
                if canonical_member._value_ == value:
                    enum_member = canonical_member
                    break
        else:
            # Aliases don't appear in member names (only in __members__).
            enum_class._member_names_.append(member_name)
            member_values.add(value)
        # performance boost for any member that would not shadow
        # a DynamicClassAttribute
        if member_name not in dynamic_attributes:
            setattr(enum_class, member_name, enum_member)
        # now add to _member_map_
        enum_class._member_map_[member_name] = enum_member
        try:
            # This may fail if value is not hashable. We can't add the value
            # to the map, and by-value lookups for this value will be
            # linear.
            enum_class._value2member_map_[value] = enum_member
        except TypeError:
            pass

    # double check that repr and friends are not the mixin's or various
    # things break (such as pickle)
    # however, if the method is defined in the Enum itself, don't replace
    # it
    for name in ('__repr__', '__str__', '__format__', '__reduce_ex__'):
        if name in classdict:
            continue
        class_method = getattr(enum_class, name)
        obj_method = getattr(member_type, name, None)
        enum_method = getattr(first_enum, name, None)
        if obj_method is not None and obj_method is class_method:
            setattr(enum_class, name, enum_method)

    # replace any other __new__ with our own (as long as Enum is not None,
    # anyway) -- again, this is to support pickle
    if enum.Enum is not None:
        # if the user defined their own __new__, save it before it gets
        # clobbered in case they subclass later
        if save_new:
            enum_class.__new_member__ = __new__
        enum_class.__new__ = enum.Enum.__new__

    # py3 support for definition order (helps keep py2/py3 code in sync)
    if _order_ is not None:
        if isinstance(_order_, str):
            _order_ = _order_.replace(',', ' ').split()
        if _order_ != enum_class._member_names_:
            raise TypeError('member order does not match _order_')

    return enum_class


def monkeypatch_enum():
    original = enum.EnumMeta.__new__
    enum.EnumMeta.__new__ = patched__new__
    return original


def revert_enum_monkeypatch(original):
    enum.EnumMeta.__new__ = original
