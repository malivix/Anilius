from collections import OrderedDict

from anilius.core.serializer_field import SerializerField
from google.protobuf.message import Message
from google.protobuf.pyext._message import RepeatedCompositeContainer


class SerializerMetaclass(type):
    """
    This metaclass sets a dictionary named `_declared_fields` on the class.

    Any instances of `Field` included as attributes on either the class
    or on any of its superclasses will be include in the
    `_declared_fields` dictionary.
    """

    @classmethod
    def _get_declared_fields(mcs, bases, attrs):
        fields = [
            (field_name, attrs.pop(field_name))
            for field_name, obj in list(attrs.items())
            if isinstance(obj, SerializerField)
        ]
        fields.sort(key=lambda x: x[1].get_creation_counter())

        # Ensures a base class field doesn't override cls attrs, and maintains
        # field precedence when inheriting multiple parents. e.g. if there is a
        # class C(A, B), and A and B both define 'field', use 'field' from A.
        known = set(attrs)

        def visit(name):
            known.add(name)
            return name

        base_fields = [
            (visit(name), f)
            for base in bases
            if hasattr(base, "_declared_fields")
            for name, f in getattr(base, "_declared_fields").items()
            if name not in known
        ]

        return OrderedDict(base_fields + fields)

    def __new__(mcs, name, bases, attrs):
        attrs["_declared_fields"] = mcs._get_declared_fields(bases, attrs)
        return super().__new__(mcs, name, bases, attrs)


class Serializer(metaclass=SerializerMetaclass):
    _declared_fields = None

    def __init__(self, request):
        assert isinstance(request, Message), "Request should be type of Message"

        for field in request.ListFields():
            if field[0].name in self._declared_fields:
                raw_value = getattr(request, field[0].name)
                raw_value = self.extract_message(raw_value)
                self._declared_fields[field[0].name].set_raw_value(raw_value)

    def extract_message(self, raw_value):
        if isinstance(raw_value, Message):
            raw_dict = {}
            for field in raw_value.ListFields():
                raw_value = getattr(raw_value, field[0].name)
                raw_value = self.extract_message(raw_value)
                raw_dict[field[0].name] = raw_value
            raw_value = raw_dict
        elif type(raw_value) is RepeatedCompositeContainer:
            raw_list = []

            for element in raw_value:
                raw_list.append(self.extract_message(element))

            raw_value = raw_list

        return raw_value

    def get_declared_fields(self):
        return self._declared_fields

    def to_dict(self):
        return dict(self.get_declared_fields())
