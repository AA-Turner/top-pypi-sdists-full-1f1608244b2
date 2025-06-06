# fmt: off

# Copyright (C) 2010, Jesper Friis
# (see accompanying license files for details).

"""
A module for ASE for simple creation of crystalline structures from
knowledge of the space group.

"""

from typing import Any, Dict

import numpy as np
from scipy import spatial

import ase
from ase.geometry import cellpar_to_cell
from ase.spacegroup import Spacegroup
from ase.symbols import string2symbols

__all__ = ['crystal']


def crystal(symbols=None, basis=None, occupancies=None, spacegroup=1, setting=1,
            cell=None, cellpar=None,
            ab_normal=(0, 0, 1), a_direction=None, size=(1, 1, 1),
            onduplicates='warn', symprec=0.001,
            pbc=True, primitive_cell=False, **kwargs) -> ase.Atoms:
    """Create an Atoms instance for a conventional unit cell of a
    space group.

    Parameters:

    symbols : str | sequence of str | sequence of Atom | Atoms
        Element symbols of the unique sites.  Can either be a string
        formula or a sequence of element symbols. E.g. ('Na', 'Cl')
        and 'NaCl' are equivalent.  Can also be given as a sequence of
        Atom objects or an Atoms object.
    basis : list of scaled coordinates
        Positions of the unique sites corresponding to symbols given
        either as scaled positions or through an atoms instance.  Not
        needed if *symbols* is a sequence of Atom objects or an Atoms
        object.
    occupancies : list of site occupancies
        Occupancies of the unique sites. Defaults to 1.0 and thus no mixed
        occupancies are considered if not explicitly asked for. If occupancies
        are given, the most dominant species will yield the atomic number.
        The occupancies in the atoms.info['occupancy'] dictionary will have
        integers keys converted to strings. The conversion is done in order
        to avoid unexpected conversions when using the JSON serializer.
    spacegroup : int | string | Spacegroup instance
        Space group given either as its number in International Tables
        or as its Hermann-Mauguin symbol.
    setting : 1 | 2
        Space group setting.
    cell : 3x3 matrix
        Unit cell vectors.
    cellpar : [a, b, c, alpha, beta, gamma]
        Cell parameters with angles in degree. Is not used when `cell`
        is given.
    ab_normal : vector
        Is used to define the orientation of the unit cell relative
        to the Cartesian system when `cell` is not given. It is the
        normal vector of the plane spanned by a and b.
    a_direction : vector
        Defines the orientation of the unit cell a vector. a will be
        parallel to the projection of `a_direction` onto the a-b plane.
    size : 3 positive integers
        How many times the conventional unit cell should be repeated
        in each direction.
    onduplicates : 'keep' | 'replace' | 'warn' | 'error'
        Action if `basis` contain symmetry-equivalent positions:
            'keep'    - ignore additional symmetry-equivalent positions
            'replace' - replace
            'warn'    - like 'keep', but issue an UserWarning
            'error'   - raises a SpacegroupValueError
    symprec : float
        Minimum "distance" betweed two sites in scaled coordinates
        before they are counted as the same site.
    pbc : one or three bools
        Periodic boundary conditions flags.  Examples: True,
        False, 0, 1, (1, 1, 0), (True, False, False).  Default
        is True.
    primitive_cell : bool
        Whether to return the primitive instead of the conventional
        unit cell.

    Keyword arguments:

    All additional keyword arguments are passed on to the Atoms
    constructor.  Currently, probably the most useful additional
    keyword arguments are `info`, `constraint` and `calculator`.

    Examples:

    Two diamond unit cells (space group number 227)

    >>> diamond = crystal('C', [(0,0,0)], spacegroup=227,
    ...     cellpar=[3.57, 3.57, 3.57, 90, 90, 90], size=(2,1,1))
    >>> ase.view(diamond)  # doctest: +SKIP

    A CoSb3 skutterudite unit cell containing 32 atoms

    >>> skutterudite = crystal(('Co', 'Sb'),
    ...     basis=[(0.25,0.25,0.25), (0.0, 0.335, 0.158)],
    ...     spacegroup=204, cellpar=[9.04, 9.04, 9.04, 90, 90, 90])
    >>> len(skutterudite)
    32
    """
    sg = Spacegroup(spacegroup, setting)
    if (
            not isinstance(symbols, str) and
            hasattr(symbols, '__getitem__') and
            len(symbols) > 0 and
            isinstance(symbols[0], ase.Atom)):
        symbols = ase.Atoms(symbols)
    if isinstance(symbols, ase.Atoms):
        basis = symbols
        symbols = basis.get_chemical_symbols()
    if isinstance(basis, ase.Atoms):
        basis_coords = basis.get_scaled_positions()
        if cell is None and cellpar is None:
            cell = basis.cell
        if symbols is None:
            symbols = basis.get_chemical_symbols()
    else:
        basis_coords = np.array(basis, dtype=float, ndmin=2)

    if occupancies is not None:
        occupancies_dict = {}

        for index, coord in enumerate(basis_coords):
            # Compute all distances and get indices of nearest atoms
            dist = spatial.distance.cdist(coord.reshape(1, 3), basis_coords)
            indices_dist = np.flatnonzero(dist < symprec)

            occ = {symbols[index]: occupancies[index]}

            # Check nearest and update occupancy
            for index_dist in indices_dist:
                if index == index_dist:
                    continue
                else:
                    occ.update({symbols[index_dist]: occupancies[index_dist]})

            occupancies_dict[str(index)] = occ.copy()

    sites, kinds = sg.equivalent_sites(basis_coords,
                                       onduplicates=onduplicates,
                                       symprec=symprec)

    # this is needed to handle deuterium masses
    masses = None
    if 'masses' in kwargs:
        masses = kwargs['masses'][kinds]
        del kwargs['masses']

    symbols = parse_symbols(symbols)

    if occupancies is None:
        symbols = [symbols[i] for i in kinds]
    else:
        # make sure that we put the dominant species there
        symbols = [sorted(occupancies_dict[str(i)].items(),
                          key=lambda x: x[1])[-1][0] for i in kinds]

    if cell is None:
        cell = cellpar_to_cell(cellpar, ab_normal, a_direction)

    info: Dict[str, Any] = {}
    info['spacegroup'] = sg
    if primitive_cell:
        info['unit_cell'] = 'primitive'
    else:
        info['unit_cell'] = 'conventional'

    if 'info' in kwargs:
        info.update(kwargs['info'])

    if occupancies is not None:
        info['occupancy'] = occupancies_dict

    kwargs['info'] = info

    atoms = ase.Atoms(symbols,
                      scaled_positions=sites,
                      cell=cell,
                      pbc=pbc,
                      masses=masses,
                      **kwargs)

    if isinstance(basis, ase.Atoms):
        for name in basis.arrays:
            if not atoms.has(name):
                array = basis.get_array(name)
                atoms.new_array(name, [array[i] for i in kinds],
                                dtype=array.dtype, shape=array.shape[1:])

    if kinds:
        atoms.new_array('spacegroup_kinds', np.asarray(kinds, dtype=int))

    if primitive_cell:
        from ase.build import cut
        prim_cell = sg.scaled_primitive_cell

        # Preserve calculator if present:
        calc = atoms.calc
        atoms = cut(atoms, a=prim_cell[0], b=prim_cell[1], c=prim_cell[2])
        atoms.calc = calc

    if size != (1, 1, 1):
        atoms = atoms.repeat(size)
    return atoms


def parse_symbols(symbols):
    """Return `sumbols` as a sequence of element symbols."""
    if isinstance(symbols, str):
        symbols = string2symbols(symbols)
    return symbols
