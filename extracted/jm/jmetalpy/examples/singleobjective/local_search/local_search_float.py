from jmetal.algorithm.singleobjective.local_search import LocalSearch
from jmetal.operator import PolynomialMutation
from jmetal.problem.singleobjective.unconstrained import Rastrigin
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == "__main__":
    problem = Rastrigin(10)

    max_evaluations = 100000

    algorithm = LocalSearch(
        problem=problem,
        mutation=PolynomialMutation(1.0 / problem.number_of_variables(), 20.0),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )

    algorithm.run()
    result = algorithm.result()

    # Save results to file
    print_function_values_to_file(result, "FUN." + algorithm.get_name() + "." + problem.name())
    print_variables_to_file(result, "VAR." + algorithm.get_name() + "." + problem.name())

    print("Algorithm: " + algorithm.get_name())
    print("Problem: " + problem.name())
    print("Solution: " + str(result.variables))
    print("Fitness:  " + str(result.objectives[0]))
    print("Computing time: " + str(algorithm.total_computing_time))
