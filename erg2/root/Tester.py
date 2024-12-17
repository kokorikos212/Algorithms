import time
import matplotlib.pyplot as plt

import numpy as np


def Tester(algorithm_cls):
    """
    A decorator that wraps an algorithm class to measure the execution time of its methods.

    Args:
        algorithm_cls (type): The class of the algorithm to test.

    Returns:
        type: A new class that wraps the original algorithm class, adding timing functionality.
    """
    
    class WrappedAlgorithm:
        """
        A wrapper class for measuring the execution time of an algorithm's methods.

        Attributes:
            instance: An instance of the original algorithm class.
        """
        def __init__(self, *args, **kwargs):
            """
            Initializes the wrapped algorithm instance.

            Args:
                *args: Positional arguments for the original algorithm class.
                **kwargs: Keyword arguments for the original algorithm class.
            """
            self.instance = algorithm_cls(*args, **kwargs)
        
        def time_execution(self, *args, **kwargs):
            """
            Measures the execution time of the algorithm's `execute` method.

            Args:
                *args: Positional arguments for the `execute` method.
                **kwargs: Keyword arguments for the `execute` method.

            Returns:
                dict: A dictionary containing the result of the algorithm and the time taken.
            """
            start_time = time.time()
            
            # Dynamically call the execute method of the instance with the arguments
            result = self.instance.execute(*args, **kwargs)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            return {"result": result, "time": execution_time}
    
    return WrappedAlgorithm



def run_experiment1():
    import sys
    from class_MC_memo import MC_Memo
    from class_MCopt import MC_OPT
    from class_MCRecursive import MC_Recursive  

    # List of different coin denominations and target sums to experiment with
    test_cases = [
        {"coins": [2, 5, 10, 1], "target_sum": 20},
        {"coins": [1, 2, 3], "target_sum": 50},
        {"coins": [1, 3, 4, 5], "target_sum": 70},
        {"coins": [1, 2, 5], "target_sum": 110},
        {"coins": [1, 3, 7, 10], "target_sum": 140}
    ]

    results = {
        'Recursive': [],
        'Memoization': [],
        'Bottom-up': []
    }
    mc_rec, mc_memo, mc_opt = MC_Recursive(), MC_Memo(), MC_OPT()  
    algorithms = [mc_rec, mc_memo, mc_opt]   
    

    for i, algorithm in enumerate(algorithms):
        times = []
        for test_case in test_cases:
            coins = test_case["coins"]
            target_sum = test_case["target_sum"]
        
            # Time the execution of the algorithm
            result = algorithm.time_execution(coins, target_sum)
            result_time = result['time']
            result_value = result['result']
            times.append(result_time) 
            # Output the result and time taken
            print(f"Result: {result_value}, Time: {result_time} seconds")
            if i == 0:
                # Store the execution times for each algorithm
                results["Recursive"] = times 
            elif i == 1:
                results["Memoization"] = times 
            elif i == 2:
                results["Bottom-up"] = times 
    print(results)
    plot_all_results(test_cases, results)
    results = {'Bottom-up': results["Bottom-up"], 'Memoization': results["Memoization"]}
    plot_all_results(test_cases, results ) 

def plot_all_results(test_cases, results):
    """
    Plot the execution times for different algorithms.

    Args:
        test_cases (list): A list of test case dictionaries containing coins, target_sum, and expected results.
        results (dict): A dictionary containing execution times for each algorithm.
    """
    # Extract test case labels (coin/target combinations)
    test_labels = [f"Coins: {test_case['coins']}, Target: {test_case['target_sum']}" 
                   for test_case in test_cases]

    # Plotting
    plt.figure(figsize=(10, 6))

    for algorithm_name, times in results.items():
        plt.plot(test_labels, times, label=algorithm_name, marker='o')

    plt.xlabel('Test Cases')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance Comparison of Coin Change Algorithms')
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    run_experiment1()

