import warnings

from pettingzoo.mpe.simple_adversary.simple_adversary import env, parallel_env, raw_env

warnings.warn(
    "The environment `pettingzoo.mpe.simple_adversary_v3` has been moved to `mpe2.simple_adversary_v3` and will be removed in a future release. "
    "Please update your imports.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["env", "parallel_env", "raw_env"]
