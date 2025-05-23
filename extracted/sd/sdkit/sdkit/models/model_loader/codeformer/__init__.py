# hack for basicsr https://github.com/XPixelGroup/BasicSR/pull/650
# credit: https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/14186/files

import sys

try:
    import torchvision.transforms.functional_tensor
except ImportError:
    try:
        import torchvision.transforms.functional as functional

        sys.modules["torchvision.transforms.functional_tensor"] = functional
    except ImportError:
        pass
# /hack

from .codeformer_arch import CodeFormer

from sdkit import Context
from sdkit.utils import load_tensor_file


def load_model(context: Context, **kwargs):
    codeformer_path = context.model_paths["codeformer"]
    sd = load_tensor_file(codeformer_path)
    sd = sd["params_ema"]

    model = CodeFormer(dim_embd=512, codebook_size=1024, n_head=8, n_layers=9, connect_list=["32", "64", "128", "256"])
    model = model.to(context.torch_device)

    model.load_state_dict(sd)
    model.eval()

    return model


def unload_model(context: Context, **kwargs):
    pass
