from __future__ import annotations
import torch
from torch import device
class GraphModule(torch.nn.Module):
    def forward(self, s52: "Sym(s52)", L_b_: "f32[s52]", L_x_: "f32[s52]"):
        l_b_ = L_b_
        l_x_ = L_x_
        
         # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:16 in torch_dynamo_resume_in_forward_at_15, code: b = b * -1
        b: "f32[s52]" = l_b_ * -1;  l_b_ = None
        
         # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:17 in torch_dynamo_resume_in_forward_at_15, code: return x * b
        mul_1: "f32[s52]" = l_x_ * b;  l_x_ = b = None
        return (mul_1,)
        