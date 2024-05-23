# DO NOT EDIT. This file was generated with:
#
# $ edb gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
import uuid
from edb.common import span
from edb.schema import name
from edb.schema import objects
from edb.common import checked


class ObjectMixin:

    def get_id(
        self, schema: 's_schema.Schema'
    ) -> 'uuid.UUID':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'id'
        )

    def get_internal(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'internal'
        )

    def get_sourcectx(
        self, schema: 's_schema.Schema'
    ) -> 'span.Span':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'sourcectx'
        )

    def get_name(
        self, schema: 's_schema.Schema'
    ) -> 'name.Name':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'name'
        )

    def get_builtin(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'builtin'
        )

    def get_computed_fields(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedSet[str]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'computed_fields'
        )


class InternalObjectMixin:
    pass


class QualifiedObjectMixin:

    def get_name(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'name'
        )


class ObjectFragmentMixin:
    pass


class GlobalObjectMixin:
    pass


class ExternalObjectMixin:
    pass


class DerivableObjectMixin:
    pass


class SubclassableObjectMixin:

    def get_abstract(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'abstract'
        )


class InheritingObjectMixin:

    def get_bases(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[objects.InheritingObject]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'bases'
        )

    def get_ancestors(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[objects.InheritingObject]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'ancestors'
        )

    def get_inherited_fields(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedSet[str]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'inherited_fields'
        )

    def get_is_derived(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'is_derived'
        )


class DerivableInheritingObjectMixin:
    pass
