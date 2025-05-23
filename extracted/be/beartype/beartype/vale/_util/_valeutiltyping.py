#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2025 Beartype authors.
# See "LICENSE" for further details.

'''
**Beartype validator PEP-compliant type hints** (i.e., hints annotating callables
declared throughout the :mod:`beartype.vale` subpackage, either for compliance
with :pep:`561` or simply for documentation purposes).

This private submodule is *not* intended for importation by downstream callers.
'''

# ....................{ IMPORTS                            }....................
from beartype.typing import (
    Any,
    Callable,
    Union,
)

# ....................{ HINTS                              }....................
BeartypeValidatorRepresenter = Union[str, Callable[[], str]]
'''
PEP-compliant type hint matching a **beartype validator representer** (i.e.,
either a string *or* caller-defined callable accepting no arguments returning a
machine-readable representation of a beartype validator).

Technically, this representation *could* be passed by the caller rather than
this callable dynamically generating that representation. Pragmatically,
generating this representation is sufficiently slow for numerous types of
validators that deferring their generation until required by a call to the
:meth:`__repr__` dunder method externally called by a call to the :func:`repr`
builtin` on this validator is effectively mandatory. Validators whose
representations are particularly slow to generate include:

* The :class:`beartype.vale.Is` class subscripted by a lambda rather than
  non-lambda function. Generating the representation of that class subscripted
  by a non-lambda function only requires introspecting the name of that function
  and is thus trivially fast. However, lambda functions have no names and are
  thus *only* distinguishable by their source code; generating the
  representation of that class subscripted by a lambda function requires parsing
  the source code of the file declaring that lambda for the exact substring of
  that code declaring that lambda.
'''


BeartypeValidatorTester = Callable[[Any], bool]
'''
PEP-compliant type hint matching a **beartype validator tester** (i.e.,
caller-defined callable accepting a single arbitrary object and returning
either :data:`True` if that object satisfies an arbitrary constraint *or*
:data:`True` otherwise).

Beartype validator testers are suitable for subscripting functional beartype
validator factories (e.g., :attr:`beartype.vale.Is`).

Caveats
-------
This parent type hint is intentionally subscripted by the child parameter type
hint :data:`.Any` rather than :class:`object`. Previously, this parent type hint
was instead subscripted by :class:`object` -- which static type-checkers
objected to as "incompatible" with various user-defined validator testers: e.g.,

.. code-block:: python

   # Given this function, pyright previously complained that the str.isascii()
   # method failed to satisfy the "Callable[[object], bool]" type hint:
   #     "object" is incompatible with "str" reportArgumentType
   @beartype
   def foo(ascii: Annotated[str, Is[str.isascii]]) -> str:
       return ascii
'''
