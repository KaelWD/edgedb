from typing import *

# from .data.data_ops import ShapeExpr, ObjectExpr



# def shape_to_expr(node: ShapeExpr) -> ObjectExpr:
#     def binding_error():
#         raise ElaborationError()

#     return ObjectExpr(
#         {k: ((s.body) if binding_is_unnamed(s) else binding_error())
#          for (k, s) in node.shape.items()})
