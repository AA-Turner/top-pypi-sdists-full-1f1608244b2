#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________
#
# Unit Tests for util/misc
#

import os
from os.path import abspath, dirname

pyomodir = dirname(abspath(__file__)) + "/../.."
currdir = dirname(abspath(__file__)) + os.sep

import pyomo.common.unittest as unittest
from pyomo.common.tempfiles import TempfileManager

import pyomo.opt

old_tempdir = TempfileManager.tempdir


class MockSolver1(pyomo.opt.OptSolver):
    def __init__(self, **kwds):
        kwds['type'] = 'stest_type'
        kwds['doc'] = 'MockSolver1 Documentation'
        pyomo.opt.OptSolver.__init__(self, **kwds)


class OptSolverDebug(unittest.TestCase):
    def setUp(self):
        pyomo.opt.SolverFactory.register('stest1')(MockSolver1)
        TempfileManager.tempdir = currdir

    def tearDown(self):
        pyomo.opt.SolverFactory.unregister('stest1')
        TempfileManager.clear_tempfiles()
        TempfileManager.tempdir = old_tempdir

    def test_solver_init1(self):
        """
        Verify the processing of 'type', 'name' and 'doc' options
        """
        ans = pyomo.opt.SolverFactory("stest1")
        self.assertEqual(type(ans), MockSolver1)
        self.assertEqual(ans._doc, "MockSolver1 Documentation")

        ans = pyomo.opt.SolverFactory("stest1", doc="My Doc")
        self.assertEqual(type(ans), MockSolver1)
        self.assertEqual(ans._doc, "MockSolver1 Documentation")

        ans = pyomo.opt.SolverFactory("stest1", name="my name")
        self.assertEqual(type(ans), MockSolver1)
        self.assertEqual(ans._doc, "MockSolver1 Documentation")

    def test_solver_init2(self):
        """
        Verify that options can be passed in.
        """
        opt = {}
        opt['a'] = 1
        opt['b'] = "two"
        ans = pyomo.opt.SolverFactory("stest1", name="solver_init2", options=opt)
        self.assertEqual(ans.options['a'], opt['a'])
        self.assertEqual(ans.options['b'], opt['b'])

    def test_avail(self):
        ans = pyomo.opt.SolverFactory("stest1")
        # This should not generate an exception
        ans.available()

    def test_problem_format(self):
        opt = pyomo.opt.SolverFactory("stest1")
        opt._problem_format = 'a'
        self.assertEqual(opt.problem_format(), 'a')
        opt._problem_format = None
        self.assertEqual(opt.problem_format(), None)

    def test_results_format(self):
        opt = pyomo.opt.SolverFactory("stest1")
        opt._results_format = 'a'
        self.assertEqual(opt.results_format(), 'a')
        opt._results_format = None
        self.assertEqual(opt.results_format(), None)

    def test_set_problem_format(self):
        opt = pyomo.opt.SolverFactory("stest1")
        opt._valid_problem_formats = []
        try:
            opt.set_problem_format('a')
        except ValueError:
            pass
        else:
            self.fail(
                "Should not be able to set the problem format undless it's declared as valid."
            )
        opt._valid_problem_formats = ['a']
        self.assertEqual(opt.results_format(), None)
        opt.set_problem_format('a')
        self.assertEqual(opt.problem_format(), 'a')
        self.assertEqual(opt.results_format(), opt._default_results_format('a'))

    def test_set_results_format(self):
        opt = pyomo.opt.SolverFactory("stest1")
        opt._valid_problem_formats = ['a']
        opt._valid_result_formats = {'a': 'b'}
        self.assertEqual(opt.problem_format(), None)
        try:
            opt.set_results_format('b')
        except ValueError:
            pass
        else:
            self.fail(
                "Should not be able to set the results format unless it's "
                "declared as valid for the current problem format."
            )
        opt.set_problem_format('a')
        self.assertEqual(opt.problem_format(), 'a')
        opt.set_results_format('b')
        self.assertEqual(opt.results_format(), 'b')


if __name__ == "__main__":
    unittest.main()
