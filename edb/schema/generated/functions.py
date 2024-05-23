# DO NOT EDIT. This file was generated with:
#
# $ edb gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
import uuid
from edb.edgeql import qltypes
from edb.edgeql import ast
from edb.schema import expr
from edb.schema import functions
from edb.schema import types
from edb.schema import globals


class ParameterMixin:

    def get_num(
        self, schema: 's_schema.Schema'
    ) -> 'int':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'num'
        )

    def get_default(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'default'
        )

    def get_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'type'
        )

    def get_typemod(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.TypeModifier':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'typemod'
        )

    def get_kind(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.ParameterKind':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'kind'
        )


class VolatilitySubjectMixin:

    def get_volatility(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.Volatility':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'volatility'
        )


class CallableObjectMixin:

    def get_params(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[functions.Parameter]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'params'
        )

    def get_return_type(
        self, schema: 's_schema.Schema'
    ) -> 'types.Type':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'return_type'
        )

    def get_return_typemod(
        self, schema: 's_schema.Schema'
    ) -> 'qltypes.TypeModifier':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'return_typemod'
        )

    def get_abstract(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'abstract'
        )

    def get_impl_is_strict(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'impl_is_strict'
        )

    def get_prefer_subquery_args(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'prefer_subquery_args'
        )


class FunctionMixin:

    def get_used_globals(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectSet[globals.Global]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'used_globals'
        )

    def get_backend_name(
        self, schema: 's_schema.Schema'
    ) -> 'uuid.UUID':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'backend_name'
        )

    def get_code(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'code'
        )

    def get_nativecode(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'nativecode'
        )

    def get_language(
        self, schema: 's_schema.Schema'
    ) -> 'ast.Language':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'language'
        )

    def get_reflected_language(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'reflected_language'
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

    def get_force_return_cast(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'force_return_cast'
        )

    def get_sql_func_has_out_params(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'sql_func_has_out_params'
        )

    def get_error_on_null_result(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'error_on_null_result'
        )

    def get_preserves_optionality(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'preserves_optionality'
        )

    def get_preserves_upper_cardinality(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'preserves_upper_cardinality'
        )

    def get_initial_value(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'initial_value'
        )

    def get_has_dml(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'has_dml'
        )

    def get_fallback(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'fallback'
        )
