"""Map functions with tqdm progress bars for parallel and sequential processing.

p_map: Performs a parallel ordered map.
p_imap: Returns an iterator for a parallel ordered map.
p_umap: Performs a parallel unordered map.
p_uimap: Returns an iterator for a parallel unordered map.
t_map: Performs a sequential map.
t_imap: Returns an iterator for a sequential map.
"""

from collections.abc import Callable, Generator, Iterable, Sized
from typing import Any

from pathos.helpers import cpu_count
from pathos.multiprocessing import ProcessPool as Pool
from tqdm.auto import tqdm


def _parallel(
    ordered: bool, function: Callable, *iterables: Iterable, **kwargs: Any
) -> Generator:
    """Returns a generator for a parallel map with a progress bar.

    Arguments:
        ordered(bool): True for an ordered map, false for an unordered map.
        function(Callable): The function to apply to each element of the given Iterables.
        iterables(Tuple[Iterable]): One or more Iterables containing the data to be mapped.

    Returns:
        A generator which will apply the function to each element of the given Iterables
        in parallel in order with a progress bar.
    """

    # Extract num_cpus
    num_cpus = kwargs.pop("num_cpus", None)

    # Determine num_cpus
    if num_cpus is None:
        num_cpus = cpu_count()
    elif isinstance(num_cpus, float):
        num_cpus = int(round(num_cpus * cpu_count()))

    # Determine length of tqdm (equal to length of shortest iterable or total kwarg), if possible
    total = kwargs.pop("total", None)
    lengths = [len(iterable) for iterable in iterables if isinstance(iterable, Sized)]
    length = total or (min(lengths) if lengths else None)

    # Create parallel generator
    map_type = "imap" if ordered else "uimap"

    # Choose tqdm variant
    tqdm_func = kwargs.pop("tqdm", tqdm)

    with Pool(num_cpus) as pool:
        map_func = getattr(pool, map_type)

        yield from tqdm_func(map_func(function, *iterables), total=length, **kwargs)

        pool.clear()


def p_map(function: Callable, *iterables: Iterable, **kwargs: Any) -> list[Any]:
    """Performs a parallel ordered map with a progress bar."""

    ordered = True
    generator = _parallel(ordered, function, *iterables, **kwargs)
    return list(generator)


def p_imap(function: Callable, *iterables: Iterable, **kwargs: Any) -> Generator:
    """Returns a generator for a parallel ordered map with a progress bar."""

    ordered = True
    return _parallel(ordered, function, *iterables, **kwargs)


def p_umap(function: Callable, *iterables: Iterable, **kwargs: Any) -> list[Any]:
    """Performs a parallel unordered map with a progress bar."""

    ordered = False
    generator = _parallel(ordered, function, *iterables, **kwargs)
    return list(generator)


def p_uimap(function: Callable, *iterables: Iterable, **kwargs: Any) -> Generator:
    """Returns a generator for a parallel unordered map with a progress bar."""

    ordered = False
    return _parallel(ordered, function, *iterables, **kwargs)


def _sequential(function: Callable, *iterables: Iterable, **kwargs: Any) -> Generator:
    """Returns a generator for a sequential map with a progress bar.

    Arguments:
        function(Callable): The function to apply to each element of the given Iterables.
        iterables(Tuple[Iterable]): One or more Iterables containing the data to be mapped.

    Returns:
        A generator which will apply the function to each element of the given Iterables
        sequentially in order with a progress bar.
    """

    # Determine length of tqdm (equal to length of shortest iterable)
    length = min(len(iterable) for iterable in iterables if isinstance(iterable, Sized))

    # Create sequential generator
    yield from tqdm(map(function, *iterables), total=length, **kwargs)


def t_map(function: Callable, *iterables: Iterable, **kwargs: Any) -> list[Any]:
    """Performs a sequential map with a progress bar."""

    generator = _sequential(function, *iterables, **kwargs)
    return list(generator)


def t_imap(function: Callable, *iterables: Iterable, **kwargs: Any) -> Generator:
    """Returns a generator for a sequential map with a progress bar."""

    return _sequential(function, *iterables, **kwargs)
