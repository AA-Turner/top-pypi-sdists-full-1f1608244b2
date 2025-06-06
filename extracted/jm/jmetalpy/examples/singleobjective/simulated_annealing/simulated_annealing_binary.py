from jmetal.algorithm.singleobjective.simulated_annealing import SimulatedAnnealing
from jmetal.operator import BitFlipMutation
from jmetal.problem import OneMax
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == "__main__":
    problem = OneMax(number_of_bits=512)

    max_evaluations = 10000

    algorithm = SimulatedAnnealing(
        problem=problem,
        mutation=BitFlipMutation(probability=1.0 / problem.total_number_of_bits()),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )

    algorithm.run()
    result = algorithm.result()

    # Save results to file
    print_function_values_to_file(result, "FUN." + algorithm.get_name() + "." + problem.name())
    print_variables_to_file(result, "VAR." + algorithm.get_name() + "." + problem.name())

    print("Algorithm: " + algorithm.get_name())
    print("Problem: " + problem.name())
    print("Solution: " + result.get_binary_string())
    print("Fitness:  " + str(result.objectives[0]))
    print("Computing time: " + str(algorithm.total_computing_time))
