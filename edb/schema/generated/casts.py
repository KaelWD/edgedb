# DO NOT EDIT. This file was generated with:
#
# $ edb gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.edgeql import ast
from edb.schema import types


class CastMixin:

    def get_from_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_type'
        )

    def get_to_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'to_type'
        )

    def get_allow_implicit(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'allow_implicit'
        )

    def get_allow_assignment(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'allow_assignment'
        )

    def get_language(
        self, schema: 's_schema.Schema'
    ) -> 'ast.Language':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'language'
        )

    def get_from_function(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_function'
        )

    def get_from_expr(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_expr'
        )

    def get_from_cast(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_cast'
        )

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'code'
        )
