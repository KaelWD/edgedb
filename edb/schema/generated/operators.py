# DO NOT EDIT. This file was generated with:
#
# $ edb gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.edgeql import qltypes
from edb.schema import name
from edb.edgeql import ast
from edb.common import checked


class OperatorMixin:

    def get_operator_kind(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.OperatorKind':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'operator_kind'
        )

    def get_language(
        self, schema: 's_schema.Schema'
    ) -> 'ast.Language':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'language'
        )

    def get_from_operator(
        self, schema: 's_schema.Schema'
    ) -> 'checked.CheckedList[str]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_operator'
        )

    def get_from_function(
        self, schema: 's_schema.Schema'
    ) -> 'checked.CheckedList[str]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_function'
        )

    def get_from_expr(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'from_expr'
        )

    def get_force_return_cast(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'force_return_cast'
        )

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'code'
        )

    def get_derivative_of(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'derivative_of'
        )

    def get_commutator(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'commutator'
        )

    def get_negator(
        self, schema: 's_schema.Schema'
    ) -> 'name.QualName':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'negator'
        )

    def get_recursive(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'recursive'
        )
