import numpy as np
import matplotlib.pyplot as plt
import time


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

def memory_opt_max_non_intersecting_segments(indices_a, indices_b):
    """
    Optimized implementation using a single row for the DP table.
    """
    n = len(indices_a)
    
    # Use a single row for DP, initialized to 0
    prev_row = [0] * (n + 1)

    for i in range(1, n + 1):
        current_row = [0] * (n + 1)
        for j in range(1, n + 1):
            if indices_a[i - 1] == indices_b[j - 1]:
                current_row[j] = prev_row[j - 1] + 1
            else:
                current_row[j] = max(prev_row[j], current_row[j - 1])
        prev_row = current_row

    # The result is in the last cell of the last row
    return prev_row[n]


# Function to generate synthetic data
def generate_test_case(n, intersect_ratio=0.5):
    indices_a = np.arange(1, n + 1)
    indices_b = np.copy(indices_a)
    if intersect_ratio < 1:
        num_to_shuffle = int(n * (1 - intersect_ratio))
        np.random.shuffle(indices_b[:num_to_shuffle])
    return indices_a.tolist(), indices_b.tolist()

def experiment():
    input_sizes = [10, 50, 100, 200, 300, 500, 1000]
    intersect_ratios = [0.1, 0.5, 0.9]
    execution_times = []

    for size in input_sizes:
        for ratio in intersect_ratios:
            indices_a, indices_b = generate_test_case(size, intersect_ratio=ratio)
            start_time = time.time()
            memory_opt_max_non_intersecting_segments(indices_a, indices_b)
            end_time = time.time()
            execution_times.append((size, ratio, end_time - start_time))
    
    return execution_times

def plot_results(execution_times):
    sizes = list(set(x[0] for x in execution_times))
    ratios = list(set(x[1] for x in execution_times))
    
    # Graph 1: Execution time vs. input size
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    for ratio in ratios:
        times = [x[2] for x in execution_times if x[1] == ratio]
        plt.plot(sizes, times, label=f"Intersect Ratio {ratio}")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs. Input Size")
    plt.legend()
    
    # Graph 2: Execution time vs. intersect ratio
    plt.subplot(1, 3, 2)
    for size in sizes:
        times = [x[2] for x in execution_times if x[0] == size]
        plt.plot(ratios, times, label=f"Size {size}")
    plt.xlabel("Intersect Ratio")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs. Intersect Ratio")
    plt.legend()
    
    # Graph 3: Heatmap of execution time
    plt.subplot(1, 3, 3)
    heatmap_data = np.zeros((len(ratios), len(sizes)))
    for size, ratio, time in execution_times:
        i = sizes.index(size)
        j = ratios.index(ratio)
        heatmap_data[j, i] = time
    plt.imshow(heatmap_data, aspect="auto", cmap="viridis", extent=(min(sizes), max(sizes), min(ratios), max(ratios)))
    plt.colorbar(label="Execution Time (s)")
    plt.xlabel("Input Size")
    plt.ylabel("Intersect Ratio")
    plt.title("Heatmap of Execution Time")
    
    plt.tight_layout()
    plt.show()

# Run Experiment and Plot
execution_times = experiment()
plot_results(execution_times)


# def test_max_non_intersecting_segments():
#     """
#     Testing suite for the max_non_intersecting_segments function.
#     """
#     # Test Case 1: Simple matching case
#     indices_a = [1, 2, 3]
#     indices_b = [1, 2, 3]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 3, "Test Case 1 Failed"

#     # Test Case 2: Completely mismatched indices
#     indices_a = [1, 2, 3]
#     indices_b = [4, 5, 6]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 2 Failed"

#     # Test Case 3: Partial matching
#     indices_a = [1, 3, 5, 7]
#     indices_b = [7, 3, 5, 1]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 2, "Test Case 3 Failed"

#     # Test Case 4: Random permutation of points (no matches)
#     indices_a = [2, 4, 6]
#     indices_b = [1, 3, 5]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 4 Failed"

#     # Test Case 5: Single point in both sets (matching)
#     indices_a = [1]
#     indices_b = [1]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 1, "Test Case 5 Failed"

#     # Test Case 6: Single point in both sets (non-matching)
#     indices_a = [1]
#     indices_b = [2]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 6 Failed"

#     # Test Case 7: Random order with some matches
#     indices_a = [1, 5, 3, 7, 9]
#     indices_b = [9, 3, 1, 7, 5]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 2, "Test Case 7 Failed"

#     # Test Case 8: All points in reverse order
#     indices_a = [5, 4, 3, 2, 1]
#     indices_b = [1, 2, 3, 4, 5]
#     assert max_non_intersecting_segments(indices_a, indices_b) == 1, "Test Case 8 Failed"

#     # Test Case 9: Edge Case: Empty input
#     indices_a = []
#     indices_b = []
#     assert max_non_intersecting_segments(indices_a, indices_b) == 0, "Test Case 9 Failed"

#     # Test Case 10: Large input (this case ensures scalability)
#     indices_a = list(range(1, 1001))
#     indices_b = list(range(1000, 0, -1))  # Reverse order
#     result = max_non_intersecting_segments(indices_a, indices_b)
#     assert result == 1, "Test Case 10 Failed"

#     print("All test cases passed successfully!")

# # Run the tests
# test_max_non_intersecting_segments()
