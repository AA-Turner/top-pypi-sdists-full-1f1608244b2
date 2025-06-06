from __future__ import annotations
import torch
from torch import device
class joint_helper(torch.nn.Module):
    def forward(self, primals, tangents):
        primals_1: "Sym(s97)"; primals_2: "f32[s97]"; primals_3: "Sym(s52)"; primals_4: "f32[s52]"; tangents_1: "f32[s97]"; 
    
        primals_1, primals_2, primals_3, primals_4, tangents_1, = fx_pytree.tree_flatten_spec([primals, tangents], self._in_spec)
         # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:4 in toy_function, code: x = a / (torch.abs(a) + 1)
        abs_1: "f32[s97]" = torch.ops.aten.abs.default(primals_2)
        add_2: "f32[s97]" = torch.ops.aten.add.Tensor(abs_1, 1);  abs_1 = None
        div: "f32[s97]" = torch.ops.aten.div.Tensor(primals_2, add_2)
        
         # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:5 in toy_function, code: if b.sum() < 0:
        sum_1: "f32[]" = torch.ops.aten.sum.default(primals_4);  primals_4 = None
        lt: "b8[]" = torch.ops.aten.lt.Scalar(sum_1, 0);  sum_1 = None
        
         # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:4 in toy_function, code: x = a / (torch.abs(a) + 1)
        neg: "f32[s97]" = torch.ops.aten.neg.default(tangents_1)
        div_1: "f32[s97]" = torch.ops.aten.div.Tensor(primals_2, add_2)
        div_2: "f32[s97]" = torch.ops.aten.div.Tensor(div_1, add_2);  div_1 = None
        mul_3: "f32[s97]" = torch.ops.aten.mul.Tensor(neg, div_2);  neg = div_2 = None
        div_3: "f32[s97]" = torch.ops.aten.div.Tensor(tangents_1, add_2);  tangents_1 = add_2 = None
        sgn: "f32[s97]" = torch.ops.aten.sgn.default(primals_2);  primals_2 = None
        mul_4: "f32[s97]" = torch.ops.aten.mul.Tensor(mul_3, sgn);  mul_3 = sgn = None
        
         # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:4 in toy_function, code: x = a / (torch.abs(a) + 1)
        add_7: "f32[s97]" = torch.ops.aten.add.Tensor(div_3, mul_4);  div_3 = mul_4 = None
        return pytree.tree_unflatten([lt, div, None, add_7, None, None], self._out_spec)
        