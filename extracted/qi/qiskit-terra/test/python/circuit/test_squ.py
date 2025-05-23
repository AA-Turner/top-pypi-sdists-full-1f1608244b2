# This code is part of Qiskit.
#
# (C) Copyright IBM 2019, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name

"""Single-qubit unitary tests."""

import unittest
from test import combine
import numpy as np
from ddt import ddt
from qiskit.quantum_info.random import random_unitary
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.test import QiskitTestCase
from qiskit.extensions.quantum_initializer.squ import SingleQubitUnitary
from qiskit.compiler import transpile
from qiskit.quantum_info.operators.predicates import matrix_equal
from qiskit.quantum_info import Operator

squs = [
    np.eye(2, 2),
    np.array([[0.0, 1.0], [1.0, 0.0]]),
    1 / np.sqrt(2) * np.array([[1.0, 1.0], [-1.0, 1.0]]),
    np.array([[np.exp(1j * 5.0 / 2), 0], [0, np.exp(-1j * 5.0 / 2)]]),
    random_unitary(2, seed=42).data,
]

up_to_diagonal_list = [True, False]


@ddt
class TestSingleQubitUnitary(QiskitTestCase):
    """Qiskit ZYZ-decomposition tests."""

    @combine(u=squs, up_to_diagonal=up_to_diagonal_list)
    def test_squ(self, u, up_to_diagonal):
        """Tests for single-qubit unitary decomposition."""
        qr = QuantumRegister(1, "qr")
        qc = QuantumCircuit(qr)
        with self.assertWarns(DeprecationWarning):
            qc.squ(u, qr[0], up_to_diagonal=up_to_diagonal)
        # Decompose the gate
        qc = transpile(qc, basis_gates=["u1", "u3", "u2", "cx", "id"])
        # Simulate the decomposed gate
        unitary = Operator(qc).data
        if up_to_diagonal:
            with self.assertWarns(DeprecationWarning):
                squ = SingleQubitUnitary(u, up_to_diagonal=up_to_diagonal)
            unitary = np.dot(np.diagflat(squ.diag), unitary)
        unitary_desired = u
        self.assertTrue(matrix_equal(unitary_desired, unitary, ignore_phase=True))


if __name__ == "__main__":
    unittest.main()
