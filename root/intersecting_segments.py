def max_non_intersecting_segments(indices_a, indices_b):
    """
    Finds the maximum number of non-intersecting segments between points
    on y=1 and y=-1 using dynamic programming.

    Args:
        indices_a (list): Indices of points on y=1.
        indices_b (list): Indices of points on y=-1.

    Returns:
        int: Maximum number of non-intersecting segments.
    """
    n = len(indices_a)
    
    # Initialize the DP table
    M = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the table bottom-up
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If indices match, we can draw a valid segment
            if indices_a[i - 1] == indices_b[j - 1]:
                M[i][j] = M[i - 1][j - 1] + 1
            else:
                # Otherwise, take the maximum from excluding either a or b
                M[i][j] = max(M[i - 1][j], M[i][j - 1])

    # The result is in M[n][n]
    return M[n][n]

def test_max_non_intersecting_segments():
    """
    Testing suite for the max_non_intersecting_segments function.
    """
    # Test Case 1: Simple matching case
    indices_a = [1, 2, 3]
    indices_b = [1, 2, 3]
    assert max_non_intersecting_segments(indices_a, indices_b) == 3, "Test Case 1 Failed"

    # Test Case 2: Completely mismatched indices
    indices_a = [1, 2, 3]
    indices_b = [4, 5, 6]
    assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 2 Failed"

    # Test Case 3: Partial matching
    indices_a = [1, 3, 5, 7]
    indices_b = [7, 3, 5, 1]
    assert max_non_intersecting_segments(indices_a, indices_b) == 3, "Test Case 3 Failed"

    # Test Case 4: Random permutation of points (no matches)
    indices_a = [2, 4, 6]
    indices_b = [1, 3, 5]
    assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 4 Failed"

    # Test Case 5: Single point in both sets (matching)
    indices_a = [1]
    indices_b = [1]
    assert max_non_intersecting_segments(indices_a, indices_b) == 1, "Test Case 5 Failed"

    # Test Case 6: Single point in both sets (non-matching)
    indices_a = [1]
    indices_b = [2]
    assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 6 Failed"

    # Test Case 7: Random order with some matches
    indices_a = [1, 5, 3, 7, 9]
    indices_b = [9, 3, 1, 7, 5]
    assert max_non_intersecting_segments(indices_a, indices_b) == 3, "Test Case 7 Failed"

    # Test Case 8: All points in reverse order
    indices_a = [5, 4, 3, 2, 1]
    indices_b = [1, 2, 3, 4, 5]
    assert max_non_intersecting_segments(indices_a, indices_b) == 1, "Test Case 8 Failed"

    # Test Case 9: Edge Case: Empty input
    indices_a = []
    indices_b = []
    assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 9 Failed"

    # Test Case 10: Large input (this case ensures scalability)
    indices_a = list(range(1, 1001))
    indices_b = list(range(1000, 0, -1))  # Reverse order
    result = max_non_intersecting_segments(indices_a, indices_b)
    assert result == 1, "Test Case 10 Failed"

    print("All test cases passed successfully!")

# Run the tests
test_max_non_intersecting_segments()
