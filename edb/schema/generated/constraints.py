# DO NOT EDIT. This file was generated with:
#
# $ edb gen-schema-mixins

"""Type definitions for generated methods on schema classes"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edb.schema import schema as s_schema
from edb.schema import orm as s_orm
from edb.schema import objects
from edb.common import checked
from edb.schema import expr
from edb.schema import constraints
from edb.schema import functions


class ConstraintMixin:

    def get_params(
        self, schema: 's_schema.Schema'
    ) -> 'objects.ObjectList[functions.Parameter]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'params'
        )

    def get_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'expr'
        )

    def get_subjectexpr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'subjectexpr'
        )

    def get_finalexpr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'finalexpr'
        )

    def get_except_expr(
        self, schema: 's_schema.Schema'
    ) -> 'expr.Expression':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'except_expr'
        )

    def get_subject(
        self, schema: 's_schema.Schema'
    ) -> 'objects.Object':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'subject'
        )

    def get_args(
        self, schema: 's_schema.Schema'
    ) -> 'checked.FrozenCheckedList[expr.Expression]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'args'
        )

    def get_delegated(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'delegated'
        )

    def get_errmessage(
        self, schema: 's_schema.Schema'
    ) -> 'str':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'errmessage'
        )

    def get_is_aggregate(
        self, schema: 's_schema.Schema'
    ) -> 'bool':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'is_aggregate'
        )


class ConsistencySubjectMixin:

    def get_constraints(
        self, schema: 's_schema.Schema'
    ) -> 'constraints.ObjectIndexByConstraintName[constraints.Constraint]':
        return s_orm.get_field_value(  # type: ignore
            self, schema, 'constraints'
        )
