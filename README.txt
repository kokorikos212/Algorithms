
# README

---

## Project: Algorithmic Solutions and Testing Framework

**Completed as part of the course "Algorithm Design and Analysis" offered by the Department of Applied Mathematics at the University of Crete.**

This project showcases various algorithmic solutions and testing utilities. It focuses on solving classic dynamic programming problems, providing a modular and extensible framework for experimentation and performance evaluation.

---

## Overview

The core of this project lies in **Masterclass Algorithms** and the **Tester magic function**:

1. **Masterclass Algorithms**:
   - A set of dynamic algorithm implementations designed to solve problems like the **Minimum Coin Change** problem.
   - These classes follow a modular structure, enabling easy expansion or adaptation to other problems.
   - Includes recursive, memoization-based, and optimized dynamic programming approaches.

2. **Tester Magic Function**:
   - A powerful decorator that wraps algorithm classes to seamlessly measure and benchmark performance.
   - Allows developers to test algorithms without modifying the core logic.
   - Facilitates quick comparison of different algorithmic solutions.

---

## Key Features

### Masterclass Algorithms

The framework supports dynamic expansion of algorithmic solutions:
- **Structure**:
  - Each algorithm inherits from a common base class.
  - Implementations share a unified interface for execution, ensuring compatibility across testing and visualization tools.
- **Extensibility**:
  - New algorithms can be added by subclassing and implementing the `execute` method.
  - Examples include **recursive**, **memoization**, and **bottom-up dynamic programming** techniques.

### Tester Magic Function

- **Purpose**:
  - Simplifies performance testing by intercepting calls to the `execute` method.
  - Logs execution time without altering the algorithm’s implementation.

- **How It Works**:
  - Use the `Tester` decorator to wrap an algorithm class.
  - Call the `time_execution` method to execute and measure performance.
  
- **Example**:
  ```python
  @Tester
  class MC_OPT:
      ...
  result, execution_time = MC_OPT().time_execution(coins, target_sum)
  print(f"Result: {result}, Time: {execution_time}")
  ```

---

## Project Structure

### 1. Algorithm Implementations

#### **MC_Recursive**
- Baseline recursive solution for the **Minimum Coin Change** problem.
- Explores all combinations, making it intuitive but inefficient for large inputs.

#### **MC_Memo**
- Memoized dynamic programming solution for improved efficiency.
- Uses caching to avoid redundant calculations.

#### **MC_OPT**
- Optimized bottom-up dynamic programming approach.
- Reduces both time and space complexity, suitable for large-scale inputs.

---

### 2. Experiment and Visualization

The project includes tools for:
- Generating synthetic test cases for diverse scenarios.
- Benchmarking algorithm performance under varying input sizes and conditions.
- Visualizing results using graphs and heatmaps.

#### Example Workflow
```python
# Run experiments
execution_times = experiment()

# Visualize results
plot_results(execution_times)
```

---

## Instructions for Use

1. **Wrap Algorithms for Testing**:
   - Decorate any algorithm class with the `Tester` function.
   - Use `time_execution` to measure runtime and results.

2. **Expand the Framework**:
   - Implement new algorithms by subclassing the base class.
   - Ensure compatibility with the testing and visualization tools.

3. **Analyze Performance**:
   - Generate synthetic data using utilities provided.
   - Benchmark algorithms and compare their efficiency.

---

## Future Work

This project forms the foundation for the next phase (**Erg3**), where the focus will shift to extending the framework with new problems.
