# This code is part of Qiskit.
#
# (C) Copyright IBM 2022
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Test VQD"""

import unittest
import warnings
from test.python.algorithms import QiskitAlgorithmsTestCase

import numpy as np
from ddt import data, ddt

from qiskit import QuantumCircuit
from qiskit.algorithms.eigensolvers import VQD, VQDResult
from qiskit.algorithms import AlgorithmError
from qiskit.algorithms.optimizers import COBYLA, L_BFGS_B, SLSQP, SPSA
from qiskit.algorithms.state_fidelities import ComputeUncompute
from qiskit.circuit.library import TwoLocal, RealAmplitudes
from qiskit.opflow import PauliSumOp
from qiskit.primitives import Sampler, Estimator
from qiskit.quantum_info import SparsePauliOp
from qiskit.quantum_info.operators import Operator
from qiskit.utils import algorithm_globals


H2_SPARSE_PAULI = SparsePauliOp.from_list(
    [
        ("II", -1.052373245772859),
        ("IZ", 0.39793742484318045),
        ("ZI", -0.39793742484318045),
        ("ZZ", -0.01128010425623538),
        ("XX", 0.18093119978423156),
    ]
)
H2_OP = Operator(H2_SPARSE_PAULI.to_matrix())

H2_PAULI = PauliSumOp(H2_SPARSE_PAULI)


@ddt
class TestVQD(QiskitAlgorithmsTestCase):
    """Test VQD"""

    def setUp(self):
        super().setUp()
        self.seed = 50
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            algorithm_globals.random_seed = self.seed

        self.h2_energy = -1.85727503
        self.h2_energy_excited = [-1.85727503, -1.24458455, -0.88272215, -0.22491125]

        self.ryrz_wavefunction = TwoLocal(
            rotation_blocks=["ry", "rz"], entanglement_blocks="cz", reps=1
        )
        self.ry_wavefunction = TwoLocal(rotation_blocks="ry", entanglement_blocks="cz")

        self.estimator = Estimator()
        self.estimator_shots = Estimator(options={"shots": 1024, "seed": self.seed})
        self.fidelity = ComputeUncompute(Sampler())
        self.betas = [50, 50]

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_basic_operator(self, op):
        """Test the VQD without aux_operators."""
        wavefunction = self.ryrz_wavefunction
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=wavefunction,
            optimizer=COBYLA(),
            betas=self.betas,
        )

        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(operator=op)
        else:
            result = vqd.compute_eigenvalues(operator=op)

        with self.subTest(msg="test eigenvalue"):
            np.testing.assert_array_almost_equal(
                result.eigenvalues.real, self.h2_energy_excited[:2], decimal=1
            )

        with self.subTest(msg="test dimension of optimal point"):
            self.assertEqual(len(result.optimal_points[-1]), 8)

        with self.subTest(msg="assert cost_function_evals is set"):
            self.assertIsNotNone(result.cost_function_evals)

        with self.subTest(msg="assert optimizer_times is set"):
            self.assertIsNotNone(result.optimizer_times)

        with self.subTest(msg="assert return ansatz is set"):
            if isinstance(op, Operator):
                with self.assertWarns(DeprecationWarning):
                    job = self.estimator.run(
                        result.optimal_circuits,
                        [op] * len(result.optimal_points),
                        result.optimal_points,
                    )
            else:
                job = self.estimator.run(
                    result.optimal_circuits,
                    [op] * len(result.optimal_points),
                    result.optimal_points,
                )
            np.testing.assert_array_almost_equal(job.result().values, result.eigenvalues, 6)

        with self.subTest(msg="assert returned values are eigenvalues"):
            np.testing.assert_array_almost_equal(
                result.optimal_values, self.h2_energy_excited[:2], decimal=3
            )

    def test_full_spectrum(self):
        """Test obtaining all eigenvalues."""
        vqd = VQD(self.estimator, self.fidelity, self.ryrz_wavefunction, optimizer=L_BFGS_B(), k=4)
        result = vqd.compute_eigenvalues(H2_PAULI)
        np.testing.assert_array_almost_equal(
            result.eigenvalues.real, self.h2_energy_excited, decimal=2
        )

    @data(H2_PAULI, H2_SPARSE_PAULI)
    def test_beta_autoeval(self, op):
        """Test beta autoevaluation for different operator types."""

        with self.assertLogs(level="INFO") as logs:
            vqd = VQD(
                self.estimator_shots, self.fidelity, self.ryrz_wavefunction, optimizer=L_BFGS_B()
            )
            _ = vqd.compute_eigenvalues(op)

        # the first log message shows the value of beta[0]
        beta = float(logs.output[0].split()[-1])
        self.assertAlmostEqual(beta, 20.40459399499687, 4)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_mismatching_num_qubits(self, op):
        """Ensuring circuit and operator mismatch is caught"""
        wavefunction = QuantumCircuit(1)
        optimizer = SLSQP(maxiter=50)
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            k=1,
            ansatz=wavefunction,
            optimizer=optimizer,
            betas=self.betas,
        )
        with self.assertRaises(AlgorithmError):
            _ = vqd.compute_eigenvalues(operator=op)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_missing_varform_params(self, op):
        """Test specifying a variational form with no parameters raises an error."""
        circuit = QuantumCircuit(op.num_qubits)
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=circuit,
            optimizer=SLSQP(),
            k=1,
            betas=self.betas,
        )
        with self.assertRaises(AlgorithmError):
            vqd.compute_eigenvalues(operator=op)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_callback(self, op):
        """Test the callback on VQD."""
        history = {"eval_count": [], "parameters": [], "mean": [], "metadata": [], "step": []}

        def store_intermediate_result(eval_count, parameters, mean, metadata, step):
            history["eval_count"].append(eval_count)
            history["parameters"].append(parameters)
            history["mean"].append(mean)
            history["metadata"].append(metadata)
            history["step"].append(step)

        optimizer = COBYLA(maxiter=3)
        wavefunction = self.ry_wavefunction

        vqd = VQD(
            estimator=self.estimator_shots,
            fidelity=self.fidelity,
            ansatz=wavefunction,
            optimizer=optimizer,
            callback=store_intermediate_result,
            betas=self.betas,
        )

        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                vqd.compute_eigenvalues(operator=op)
        else:
            vqd.compute_eigenvalues(operator=op)

        self.assertTrue(all(isinstance(count, int) for count in history["eval_count"]))
        self.assertTrue(all(isinstance(mean, float) for mean in history["mean"]))
        self.assertTrue(all(isinstance(metadata, dict) for metadata in history["metadata"]))
        self.assertTrue(all(isinstance(count, int) for count in history["step"]))
        for params in history["parameters"]:
            self.assertTrue(all(isinstance(param, float) for param in params))

        ref_eval_count = [1, 2, 3, 1, 2, 3]
        ref_mean = [-1.07, -1.45, -1.37, 37.43, 48.55, 28.94]
        # new ref_mean for statevector simulator. The old unit test was on qasm
        # and the ref_mean values were slightly different.

        ref_step = [1, 1, 1, 2, 2, 2]

        np.testing.assert_array_almost_equal(history["eval_count"], ref_eval_count, decimal=0)
        np.testing.assert_array_almost_equal(history["mean"], ref_mean, decimal=2)
        np.testing.assert_array_almost_equal(history["step"], ref_step, decimal=0)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_vqd_optimizer(self, op):
        """Test running same VQD twice to re-use optimizer, then switch optimizer"""

        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=RealAmplitudes(),
            optimizer=SLSQP(),
            k=2,
            betas=self.betas,
        )

        def run_check():
            if isinstance(op, Operator):
                with self.assertWarns(DeprecationWarning):
                    result = vqd.compute_eigenvalues(operator=op)
            else:
                result = vqd.compute_eigenvalues(operator=op)
            np.testing.assert_array_almost_equal(
                result.eigenvalues.real, self.h2_energy_excited[:2], decimal=3
            )

        run_check()

        with self.subTest("Optimizer re-use"):
            run_check()

        with self.subTest("Optimizer replace"):
            vqd.optimizer = L_BFGS_B()
            run_check()

        with self.subTest("Batched optimizer replace"):
            vqd.optimizer = SLSQP(maxiter=60, max_evals_grouped=10)
            run_check()

        with self.subTest("SPSA replace"):
            # SPSA takes too long to converge, so we will
            # only check that it runs with no errors.
            vqd.optimizer = SPSA(maxiter=5, learning_rate=0.01, perturbation=0.01)
            if isinstance(op, Operator):
                with self.assertWarns(DeprecationWarning):
                    result = vqd.compute_eigenvalues(operator=op)
            else:
                result = vqd.compute_eigenvalues(operator=op)
            self.assertIsInstance(result, VQDResult)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_optimizer_list(self, op):
        """Test sending an optimizer list"""

        optimizers = [SLSQP(), L_BFGS_B()]
        initial_point_1 = [
            1.70256666,
            -5.34843975,
            -0.39542903,
            5.99477786,
            -2.74374986,
            -4.85284669,
            0.2442925,
            -1.51638917,
        ]
        initial_point_2 = [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ]
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=RealAmplitudes(),
            optimizer=optimizers,
            initial_point=[initial_point_1, initial_point_2],
            k=2,
            betas=self.betas,
        )

        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(operator=op)
        else:
            result = vqd.compute_eigenvalues(operator=op)
        np.testing.assert_array_almost_equal(
            result.eigenvalues.real, self.h2_energy_excited[:2], decimal=3
        )

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_aux_operators_list(self, op):
        """Test list-based aux_operators."""
        wavefunction = self.ry_wavefunction
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=wavefunction,
            optimizer=SLSQP(),
            k=2,
            betas=self.betas,
        )

        # Start with an empty list
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=[])
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=[])
        np.testing.assert_array_almost_equal(
            result.eigenvalues.real, self.h2_energy_excited[:2], decimal=2
        )
        self.assertIsNone(result.aux_operators_evaluated)

        # Go again with two auxiliary operators
        aux_op1 = SparsePauliOp.from_list([("II", 2.0)])
        aux_op2 = SparsePauliOp.from_list([("II", 0.5), ("ZZ", 0.5), ("YY", 0.5), ("XX", -0.5)])
        aux_ops = [aux_op1, aux_op2]
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        np.testing.assert_array_almost_equal(
            result.eigenvalues.real, self.h2_energy_excited[:2], decimal=2
        )
        self.assertEqual(len(result.aux_operators_evaluated), 2)
        # expectation values
        self.assertAlmostEqual(result.aux_operators_evaluated[0][0][0], 2, places=2)
        self.assertAlmostEqual(result.aux_operators_evaluated[0][1][0], 0, places=2)
        # metadata
        self.assertIsInstance(result.aux_operators_evaluated[0][1][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][1][1], dict)

        # Go again with additional None and zero operators
        extra_ops = [*aux_ops, None, 0]
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=extra_ops)
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=extra_ops)
        np.testing.assert_array_almost_equal(
            result.eigenvalues.real, self.h2_energy_excited[:2], decimal=2
        )
        self.assertEqual(len(result.aux_operators_evaluated), 2)
        # expectation values
        self.assertAlmostEqual(result.aux_operators_evaluated[0][0][0], 2, places=2)
        self.assertAlmostEqual(result.aux_operators_evaluated[0][1][0], 0, places=2)
        self.assertEqual(result.aux_operators_evaluated[0][2][0], 0.0)
        self.assertEqual(result.aux_operators_evaluated[0][3][0], 0.0)
        # metadata
        self.assertIsInstance(result.aux_operators_evaluated[0][0][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][1][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][3][1], dict)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_aux_operators_dict(self, op):
        """Test dictionary compatibility of aux_operators"""
        wavefunction = self.ry_wavefunction
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=wavefunction,
            optimizer=SLSQP(),
            betas=self.betas,
        )

        # Start with an empty dictionary
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators={})
        else:
            result = vqd.compute_eigenvalues(op, aux_operators={})
        np.testing.assert_array_almost_equal(
            result.eigenvalues.real, self.h2_energy_excited[:2], decimal=2
        )
        self.assertIsNone(result.aux_operators_evaluated)

        # Go again with two auxiliary operators
        aux_op1 = SparsePauliOp.from_list([("II", 2.0)])
        aux_op2 = SparsePauliOp.from_list([("II", 0.5), ("ZZ", 0.5), ("YY", 0.5), ("XX", -0.5)])
        aux_ops = {"aux_op1": aux_op1, "aux_op2": aux_op2}
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        self.assertEqual(len(result.eigenvalues), 2)
        self.assertEqual(result.eigenvalues.dtype, np.complex128)
        self.assertAlmostEqual(result.eigenvalues[0], -1.85727503, 2)
        self.assertEqual(len(result.aux_operators_evaluated), 2)
        self.assertEqual(len(result.aux_operators_evaluated[0]), 2)
        # expectation values
        self.assertAlmostEqual(result.aux_operators_evaluated[0]["aux_op1"][0], 2, places=6)
        self.assertAlmostEqual(result.aux_operators_evaluated[0]["aux_op2"][0], 0, places=1)
        # metadata
        self.assertIsInstance(result.aux_operators_evaluated[0]["aux_op1"][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0]["aux_op2"][1], dict)

        # Go again with additional None and zero operators
        extra_ops = {**aux_ops, "None_operator": None, "zero_operator": 0}
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=extra_ops)
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=extra_ops)
        self.assertEqual(len(result.eigenvalues), 2)
        self.assertEqual(result.eigenvalues.dtype, np.complex128)
        self.assertAlmostEqual(result.eigenvalues[0], -1.85727503, places=5)
        self.assertEqual(len(result.aux_operators_evaluated), 2)
        self.assertEqual(len(result.aux_operators_evaluated[0]), 3)
        # expectation values
        self.assertAlmostEqual(result.aux_operators_evaluated[0]["aux_op1"][0], 2, places=6)
        self.assertAlmostEqual(result.aux_operators_evaluated[0]["aux_op2"][0], 0.0, places=2)
        self.assertEqual(result.aux_operators_evaluated[0]["zero_operator"][0], 0.0)
        self.assertTrue("None_operator" not in result.aux_operators_evaluated[0].keys())
        # metadata
        self.assertIsInstance(result.aux_operators_evaluated[0]["aux_op1"][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0]["aux_op2"][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0]["zero_operator"][1], dict)

    @data(H2_PAULI, H2_OP, H2_SPARSE_PAULI)
    def test_aux_operator_std_dev(self, op):
        """Test non-zero standard deviations of aux operators."""
        wavefunction = self.ry_wavefunction
        vqd = VQD(
            estimator=self.estimator,
            fidelity=self.fidelity,
            ansatz=wavefunction,
            initial_point=[
                1.70256666,
                -5.34843975,
                -0.39542903,
                5.99477786,
                -2.74374986,
                -4.85284669,
                0.2442925,
                -1.51638917,
            ],
            optimizer=COBYLA(maxiter=0),
            betas=self.betas,
        )

        # Go again with two auxiliary operators
        aux_op1 = SparsePauliOp.from_list([("II", 2.0)])
        aux_op2 = SparsePauliOp.from_list([("II", 0.5), ("ZZ", 0.5), ("YY", 0.5), ("XX", -0.5)])
        aux_ops = [aux_op1, aux_op2]
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        self.assertEqual(len(result.aux_operators_evaluated), 2)
        # expectation values
        self.assertAlmostEqual(result.aux_operators_evaluated[0][0][0], 2.0, places=1)
        self.assertAlmostEqual(
            result.aux_operators_evaluated[0][1][0], 0.0019531249999999445, places=1
        )
        # metadata
        self.assertIsInstance(result.aux_operators_evaluated[0][0][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][1][1], dict)

        # Go again with additional None and zero operators
        aux_ops = [*aux_ops, None, 0]
        if isinstance(op, Operator):
            with self.assertWarns(DeprecationWarning):
                result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        else:
            result = vqd.compute_eigenvalues(op, aux_operators=aux_ops)
        self.assertEqual(len(result.aux_operators_evaluated[0]), 4)
        # expectation values
        self.assertAlmostEqual(result.aux_operators_evaluated[0][0][0], 2.0, places=1)
        self.assertAlmostEqual(
            result.aux_operators_evaluated[0][1][0], 0.0019531249999999445, places=1
        )
        self.assertEqual(result.aux_operators_evaluated[0][2][0], 0.0)
        self.assertEqual(result.aux_operators_evaluated[0][3][0], 0.0)
        # metadata
        self.assertIsInstance(result.aux_operators_evaluated[0][0][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][1][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][2][1], dict)
        self.assertIsInstance(result.aux_operators_evaluated[0][3][1], dict)


if __name__ == "__main__":
    unittest.main()
