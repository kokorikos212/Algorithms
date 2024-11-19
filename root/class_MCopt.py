from class_Algorithms import *
from Tester import Tester    

@Tester
class MC_OPT(Algorithms):
    """
    Optimized Bottom-Up Dynamic Programming solution for the Minimum Coin Change problem.

    This class implements a bottom-up tabulation approach with O(n * sum) time complexity 
    and O(n * sum) space complexity to solve the Minimum Coin Change problem. 
    The algorithm iteratively fills a DP table, considering whether to include or exclude 
    each coin for a given sum, starting from the largest coin down to the smallest.

    **Dynamic Programming Relation**:
    - If (current_sum - coins[i]) >= 0:
        dp[i][current_sum] = min(1 + dp[i][current_sum - coins[i]], dp[i + 1][current_sum])
    - Otherwise:
        dp[i][current_sum] = dp[i + 1][current_sum]

    This ensures that all combinations of coins contributing to a target sum are evaluated 
    in an efficient manner, leveraging previous results stored in the DP table.

    **Key Characteristics**:
    - Iterative and space-efficient for solving the problem.
    - Builds the solution iteratively from smaller subproblems, avoiding recursion overhead.
    - Particularly suitable for applications where both time and space optimization are critical.

    Inherits:
    ----------
    Algorithms : Base class
        Provides a foundation for structuring algorithmic solutions.

    Methods:
    --------
    opt_solution(coins, target_sum):
        Computes the minimum number of coins needed using a bottom-up approach.

    execute(coins, target_sum):
        Invokes the bottom-up DP solution and serves as the entry point for testing and execution.

    Example:
    --------
    >>> coins = [1, 2, 5]
    >>> target_sum = 11
    >>> mc_opt = MC_OPT()
    >>> mc_opt.execute(coins, target_sum)
    3
    """

    def __init__(self):
        super().__init__("Memoized (Tabulation) solution for the Minimum Coin Change problem.")
    
    def execute(self, coins, target_sum):
        """
        Optimized bottom-up dynamic programming solution that reduces space complexity 
        by using a 1D table instead of a 2D table for the coin change problem.

        Parameters:
        coins (list): List of available coin denominations.
        target_sum (int): The sum for which the minimum number of coins is to be calculated.

        Returns:
        int: Minimum number of coins needed, or -1 if it's not possible to form the sum.
        """
        dp = [float('inf')] * (target_sum + 1)
        dp[0] = 0

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, target_sum + 1):
                take = float('inf')
                noTake = float('inf')

                # If we take coins[i] coin
                if j - coins[i] >= 0 and coins[i] > 0:
                    take = dp[j - coins[i]]
                    if take != float('inf'):
                        take += 1

                if i + 1 < len(coins):
                    noTake = dp[j]

                dp[j] = min(take, noTake)

        return dp[target_sum] if dp[target_sum] != float('inf') else -1

    
if __name__ == "__main__":
    # Instantiate the recursive minimum coin change class
    rec_mnc = MC_OPT()

    # Define test cases
    test_cases = [
        {"coins": [1, 2, 5], "target_sum": 11, "expected": 3},  # 5+5+1
        {"coins": [2], "target_sum": 3, "expected": -1},        # Not possible
        {"coins": [1, 2, 3], "target_sum": 4, "expected": 2},   # 3+1 or 2+2
        {"coins": [5, 10, 25], "target_sum": 30, "expected": 2} # 25+5
    ]

    # Test each case
    for idx, test_case in enumerate(test_cases, start=1):
        coins = test_case["coins"]
        target_sum = test_case["target_sum"]
        expected = test_case["expected"]

        print(f"Test Case {idx}: Coins = {coins}, Target Sum = {target_sum}")
        result = rec_mnc.execute(coins, target_sum)

        # Verify the result
        if result == expected:
            print(f"PASSED: Expected {expected}, Got {result}")
        else:
            print(f"FAILED: Expected {expected}, Got {result}")