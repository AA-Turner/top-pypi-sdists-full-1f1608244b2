# fmt: off

from ase.atoms import Atoms
from ase.utils import reader, writer


@writer
def write_crystal(fd, atoms):
    """Method to write atom structure in crystal format
       (fort.34 format)
    """

    ispbc = atoms.get_pbc()
    box = atoms.get_cell()

    # here it is assumed that the non-periodic direction are z
    # in 2D case, z and y in the 1D case.

    if ispbc[2]:
        fd.write('%2s %2s %2s %23s \n' %
                 ('3', '1', '1', 'E -0.0E+0 DE 0.0E+0( 1)'))
    elif ispbc[1]:
        fd.write('%2s %2s %2s %23s \n' %
                 ('2', '1', '1', 'E -0.0E+0 DE 0.0E+0( 1)'))
        box[2, 2] = 500.
    elif ispbc[0]:
        fd.write('%2s %2s %2s %23s \n' %
                 ('1', '1', '1', 'E -0.0E+0 DE 0.0E+0( 1)'))
        box[2, 2] = 500.
        box[1, 1] = 500.
    else:
        fd.write('%2s %2s %2s %23s \n' %
                 ('0', '1', '1', 'E -0.0E+0 DE 0.0E+0( 1)'))
        box[2, 2] = 500.
        box[1, 1] = 500.
        box[0, 0] = 500.

    # write box
    # crystal dummy
    fd.write(' %.17E %.17E %.17E \n'
             % (box[0][0], box[0][1], box[0][2]))
    fd.write(' %.17E %.17E %.17E \n'
             % (box[1][0], box[1][1], box[1][2]))
    fd.write(' %.17E %.17E %.17E \n'
             % (box[2][0], box[2][1], box[2][2]))

    # write symmetry operations (not implemented yet for
    # higher symmetries than C1)
    fd.write(' %2s \n' % (1))
    fd.write(f' {1:.17E} {0:.17E} {0:.17E} \n')
    fd.write(f' {0:.17E} {1:.17E} {0:.17E} \n')
    fd.write(f' {0:.17E} {0:.17E} {1:.17E} \n')
    fd.write(f' {0:.17E} {0:.17E} {0:.17E} \n')

    # write coordinates
    fd.write(' %8s \n' % (len(atoms)))
    coords = atoms.get_positions()
    tags = atoms.get_tags()
    atomnum = atoms.get_atomic_numbers()
    for iatom, coord in enumerate(coords):
        fd.write('%5i  %19.16f %19.16f %19.16f \n'
                 % (atomnum[iatom] + tags[iatom],
                    coords[iatom][0], coords[iatom][1], coords[iatom][2]))


@reader
def read_crystal(fd):
    """Method to read coordinates form 'fort.34' files
    additionally read information about
    periodic boundary condition
    """
    lines = fd.readlines()

    atoms_pos = []
    anumber_list = []
    my_pbc = [False, False, False]
    mycell = []

    if float(lines[4]) != 1:
        raise ValueError('High symmetry geometry is not allowed.')

    if float(lines[1].split()[0]) < 500.0:
        cell = [float(c) for c in lines[1].split()]
        mycell.append(cell)
        my_pbc[0] = True
    else:
        mycell.append([1, 0, 0])

    if float(lines[2].split()[1]) < 500.0:
        cell = [float(c) for c in lines[2].split()]
        mycell.append(cell)
        my_pbc[1] = True
    else:
        mycell.append([0, 1, 0])

    if float(lines[3].split()[2]) < 500.0:
        cell = [float(c) for c in lines[3].split()]
        mycell.append(cell)
        my_pbc[2] = True
    else:
        mycell.append([0, 0, 1])

    natoms = int(lines[9].split()[0])
    for i in range(natoms):
        index = 10 + i
        anum = int(lines[index].split()[0]) % 100
        anumber_list.append(anum)

        position = [float(p) for p in lines[index].split()[1:]]
        atoms_pos.append(position)

    atoms = Atoms(positions=atoms_pos, numbers=anumber_list,
                  cell=mycell, pbc=my_pbc)

    return atoms
