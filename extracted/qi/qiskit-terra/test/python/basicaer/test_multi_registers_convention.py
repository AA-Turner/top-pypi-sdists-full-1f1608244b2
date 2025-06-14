# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Test executing multiple-register circuits on BasicAer."""

import warnings
from qiskit import BasicAer  # pylint: disable=no-name-in-module
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Operator, Statevector, process_fidelity, state_fidelity
from qiskit.test import QiskitTestCase


class TestCircuitMultiRegs(QiskitTestCase):
    """QuantumCircuit Qasm tests."""

    def test_circuit_multi(self):
        """Test circuit multi regs declared at start."""
        qreg0 = QuantumRegister(2, "q0")
        creg0 = ClassicalRegister(2, "c0")
        qreg1 = QuantumRegister(2, "q1")
        creg1 = ClassicalRegister(2, "c1")
        circ = QuantumCircuit(qreg0, qreg1, creg0, creg1)
        circ.x(qreg0[1])
        circ.x(qreg1[0])

        meas = QuantumCircuit(qreg0, qreg1, creg0, creg1)
        meas.measure(qreg0, creg0)
        meas.measure(qreg1, creg1)

        qc = circ.compose(meas)

        # filter warnings raised by deprecated functionality in BasicAer backends .run() method
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning, message=r".*basicaer.*")

            backend_sim = BasicAer.get_backend("qasm_simulator")

            result = backend_sim.run(qc).result()
            counts = result.get_counts(qc)

            target = {"01 10": 1024}

            backend_sim = BasicAer.get_backend("statevector_simulator")
            result = backend_sim.run(circ).result()
            state = result.get_statevector(circ)

            backend_sim = BasicAer.get_backend("unitary_simulator")
            result = backend_sim.run(circ).result()
            unitary = Operator(result.get_unitary(circ))

            self.assertEqual(counts, target)
            self.assertAlmostEqual(
                state_fidelity(Statevector.from_label("0110"), state), 1.0, places=7
            )
            self.assertAlmostEqual(
                process_fidelity(Operator.from_label("IXXI"), unitary), 1.0, places=7
            )
