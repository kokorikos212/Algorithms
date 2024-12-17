from class_Algorithms import *
from Tester import Tester


@Tester
class MC_Recursive(Algorithms):
    """
    Recursive solution for the Minimum Coin Change problem.

    This class provides a straightforward recursive implementation to solve 
    the Minimum Coin Change problem. The algorithm explores all possible 
    combinations of coin denominations recursively, determining the minimum 
    number of coins needed to achieve a given target sum.

    **Approach**:
    - For each coin, decide whether to:
        1. Include it (reducing the remaining sum by the coin's value).
        2. Exclude it (proceeding to the next coin).
    - Recursively explore all options, keeping track of the minimum number 
      of coins required.
    - Base Cases:
        - If the target sum becomes `0`, return `0` (no more coins needed).
        - If the target sum becomes negative or no coins are left, return infinity 
          (indicating no valid solution for this branch).

    **Drawbacks**:
    - Exponential time complexity due to overlapping subproblems, as the same 
      states may be recalculated multiple times.
    - High recursion overhead, making this approach inefficient for large inputs.

    **Key Characteristics**:
    - Simple and intuitive, serving as a baseline for comparison with optimized 
      approaches such as memoization and bottom-up DP.
    - Suitable for understanding the problem's recursive structure.

    Inherits:
    ----------
    Algorithms : Base class
        Provides a foundation for structuring algorithmic solutions.

    Methods:
    --------
    minCoinsRecur(i, sum, coins):
        Recursive function to compute the minimum number of coins needed for 
        a given sum, starting from index `i`.

    execute(coins, target_sum):
        Entry point to execute the recursive solution for the given input.

    Example:
    --------
    >>> coins = [1, 2, 5]
    >>> target_sum = 11
    >>> mc_recursive = MC_Recursive()
    >>> mc_recursive.execute(coins, target_sum)
    3
    """

    def __init__(self):
        super().__init__("Recursive solution for Minimum Coin Change Problem")
        
    def minCoinsRecur(self, i, target_sum, coins):
        """
        Recursive solution to find the minimum number of coins needed for a given sum.

        Parameters:
        i (int): Current index in the list of coins.
        target_sum (int): The remaining sum to be formed.
        coins (list): List of available coin denominations.

        Returns:
        int: Minimum number of coins needed, or infinity if not possible.
        """
        # Base case
        if target_sum == 0:
            return 0
        if target_sum < 0 or i == len(coins):
            return float('inf')

        take = float('inf')

        # Take a coin only if its value
        # is greater than 0.
        if coins[i] > 0:
            take = self.minCoinsRecur(i, target_sum - coins[i], coins)
            if take != float('inf'):
                take += 1

        noTake = self.minCoinsRecur(i + 1, target_sum, coins)

        return min(take, noTake)

    def execute(self, coins, target_sum):
        """
        Wrapper function to start the recursive calculation of the minimum coins required 
        for a specific sum using the minCoinsRecur function.

        Parameters:
        coins (list): List of available coin denominations.
        target_sum (int): The sum for which the minimum number of coins is to be calculated.

        Returns:
        int: Minimum number of coins needed, or -1 if it's not possible to form the sum.
        """
        ans = self.minCoinsRecur(0, target_sum, coins)
        return ans if ans != float('inf') else -1

# if __name__ == "__main__":
#     # Instantiate the recursive minimum coin change class
#     rec_mnc = MC_Recursive()

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
#         if result["result"] == expected:
#             print(f"PASSED: Expected {expected}, Got {result}")
#         else:
#             print(f"FAILED: Expected {expected}, Got {result}")



















