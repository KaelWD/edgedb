# DO NOT EDIT. This file was generated with:
#
# $ edb gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.edgeql import qltypes
from edb.schema import pointers
from edb.schema import rewrites
from edb.schema import expr
from edb.schema import types


class PointerMixin:

    def get_source(
        self, schema: 's_schema.Schema'
    ) -> 'objects.InheritingObject':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'source'
        )

    def get_target(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'target'
        )

    def get_required(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'required'
        )

    def get_readonly(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'readonly'
        )

    def get_secret(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'secret'
        )

    def get_protected(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'protected'
        )

    def get_computable(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'computable'
        )

    def get_from_alias(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_alias'
        )

    def get_defined_here(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'defined_here'
        )

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'expr'
        )

    def get_default(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'default'
        )

    def get_cardinality(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.SchemaCardinality':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'cardinality'
        )

    def get_union_of(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[pointers.Pointer]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'union_of'
        )

    def get_intersection_of(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[pointers.Pointer]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'intersection_of'
        )

    def get_computed_link_alias_is_backward(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'computed_link_alias_is_backward'
        )

    def get_computed_link_alias(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'computed_link_alias'
        )

    def get_rewrites(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectIndexByUnqualifiedName[rewrites.Rewrite]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'rewrites'
        )
