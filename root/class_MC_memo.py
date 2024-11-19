from class_Algorithms import *
from Tester import Tester    

@Tester
class MC_Memo(Algorithms):
    """
    Memoized (Tabulation) solution for the Minimum Coin Change problem.

    This class implements a dynamic programming approach to solve the Minimum 
    Coin Change problem using memoization. The algorithm builds a solution 
    iteratively by maintaining a table (memo) that records the results of 
    overlapping subproblems.

    By leveraging the memoization approach, this class ensures efficient 
    computation, avoiding the exponential time complexity of naive recursive 
    solutions. This implementation is particularly suitable for scenarios 
    involving large target sums or extensive coin denominations.

    Inherits:
    ----------
    Algorithms : Base class
        Provides a foundation for structuring algorithmic solutions.

    Methods:
    -------
    get_memo_solution(coins, target_sum):
        Computes the minimum number of coins needed to form the target sum 
        using memoization.

    execute(coins, target_sum):
        Invokes the memoized solution and serves as the entry point for 
        testing and executing the algorithm.

    Example:
    -------
    >>> coins = [1, 2, 5]
    >>> target_sum = 11
    >>> memo_mnc = MEMO_MNC()
    >>> memo_mnc.execute(coins, target_sum)
    3
    """

    def __init__(self):
        """
        Initializes the MC_Memo instance, setting the algorithm name.
        """
        super().__init__("Recursive solution for Minimum")

    def execute(self, coins, target_sum):
        """
        Recursively computes the minimum number of coins needed using memoization.

        Parameters:
        ----------
        i : int
            Current index in the list of coins.
        target_sum : int
            The remaining sum to be formed.
        coins : list
            List of available coin denominations.
        memo : list of lists
            Table for storing results of overlapping subproblems.

        Returns:
        -------
        int
            Minimum number of coins required to form the remaining sum, or infinity 
            if not possible.
        """
        memo = [[-1] * (target_sum + 1) for _ in range(len(coins))]
        ans = self.minCoinsRecur(0, target_sum, coins, memo)
        return ans if ans != float('inf') else -1
    
    def minCoinsRecur(self, i, target_sum, coins, memo):
        """
        Recursive solution with memoization to find the minimum number of coins needed 
        for a given sum. It stores intermediate results to avoid redundant calculations.

        Parameters:
        i (int): Current index in the list of coins.
        target_sum (int): The remaining sum to be formed.
        coins (list): List of available coin denominations.
        memo (list of lists): Memoization table storing the results of subproblems.

        Returns:
        int: Minimum number of coins needed, or infinity if not possible.
        """
        # Base case
        if target_sum == 0:
            return 0
        if target_sum < 0 or i == len(coins):
            return float('inf')

        if memo[i][target_sum] != -1:
            return memo[i][target_sum]

        take = float('inf')

        # Take a coin only if its value
        # is greater than 0.
        if coins[i] > 0:
            take = self.minCoinsRecur(i, target_sum - coins[i], coins, memo)
            if take != float('inf'):
                take += 1

        noTake = self.minCoinsRecur(i + 1, target_sum, coins, memo)

        memo[i][target_sum] = min(take, noTake)
        return memo[i][target_sum]


# if __name__ == "__main__":
#     # Instantiate the recursive minimum coin change class
#     rec_mnc = MC_Memo()

#     # Define test cases
#     test_cases = [
#         {"coins": [1, 2, 5], "target_sum": 11, "expected": 3},  # 5+5+1
#         {"coins": [2], "target_sum": 3, "expected": -1},        # Not possible
#         {"coins": [1, 2, 3], "target_sum": 4, "expected": 2},   # 3+1 or 2+2
#         {"coins": [5, 10, 25], "target_sum": 30, "expected": 2} # 25+5
#     ]

#     # Test each case
#     for idx, test_case in enumerate(test_cases, start=1):
#         coins = test_case["coins"]
#         target_sum = test_case["target_sum"]
#         expected = test_case["expected"]

#         print(f"Test Case {idx}: Coins = {coins}, Target Sum = {target_sum}")
#         result = rec_mnc.time_execution(coins, target_sum)

#         # Verify the result
#         if result == expected:
#             print(f"PASSED: Expected {expected}, Got {result}")
#         else:
#             print(f"FAILED: Expected {expected}, Got {result}")