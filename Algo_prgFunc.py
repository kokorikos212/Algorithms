import random as rd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import time, os 

import pprint

    
def Tester(algorithm_inst):
    def wraper(Sequence):
        algorithm = algorithm_inst(Sequence)
        start_time = time.time()
        sorted_data = algorithm.Sort()
        end_time = time.time()
        recorted_time = end_time - start_time
        return {"sorted_data":sorted_data, "recorted_time":recorted_time}
        print(f"{sorted_data}, {recorted_time}")
    return wraper
    
class Algorithms: # Masterclass Algo
    # implementing a Strategy Pattern for storing sorting algorithms
    def __init__(self, A):
        self.A = A
    
    def __repr__(self):
        print("__repr__")
        return self.A
    
@Tester
class Heapsort(Algorithms):
    """
    Takes a sequence in the form of a list and returns it modified by the Heap Sort algorithm.
    """
    # Αυτή είναι η αναπαράσταση του αλγόριθμου ταξινόμησης σωρού.

    def Left(self, i):
        "returns the left child node."
        return 2 * i

    def Right(self, i):
        "returns the right child node"
        return 2 * i + 1
    # Αυτή που δεν έχει μέσα κλήση άλλων συναρτίσεων πέραν itterations θα είναι η συνάρτιση κλήσε

    def Build_max_heap(self):
        """
        It traverses the remaining nodes of the tree and performs MAX HEAPIFY on each one.
        """
        n = len(self.A)
        
        # Start from the last non-leaf node and perform max-heapify for each
        for i in range(n // 2 - 1, -1, -1):
            self.Max_hepify(i, n - 1)

    def Max_hepify(self, i, n):
        """
        Maintain the max-heap property for a binary heap represented by array A.

        Parameters:
        - A: The array representing the binary heap.
        - i: The index of the current node to consider.
        - n: The size of the heap (number of element
        """
        
        l = self.Left(i)
        r = self.Right(i)
        largest = i

        if l <= n and self.A[l] > self.A[i]:
            largest = l

        if r <= n and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]  # Swap A[i] and A[largest]
            self.Max_hepify(largest, n)


    def Sort(self):
        """
        It takes as an argument only the sequence A in the form of a list.
        It uses BUILD MAX HEAP and MAX HEAPIFY to sort the given sequence."""
        self.Build_max_heap()
        n = len(self.A)
        
        # Activate Heapsort
        for i in range(n - 1, 0, -1):
            # Swap the root (maximum value) with the last element of the heap
            self.A[0], self.A[i] = self.A[i], self.A[0]
            
            # Reduce the heap size (exclude the last element which is now sorted)
            self.Max_hepify(0, i - 1)
        return self.A

@Tester
class Mergesort(Algorithms):
    """ 
    A class representing the Merge Sort algorithm.
    This class inherits from the 'Algorithms' superclass and provides an
    implementation of the Merge Sort sorting algorithm.
    """

    def __init__(self, array, output_dir='plots'):
        """ Initializes the MergeSort with an array to sort and a directory to save plots. """
        self.A = array
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    def visualize_sort(self, current_sequence, step):
        """ 
        Visualizes the current state of the array during the sort and saves the plot to a file.
        
        Args:
        current_sequence (list): The current state of the array to visualize.
        step (int): The step number for the current sorting stage, used for naming the file.
        """
        plt.figure(figsize=(8, 6))  # Set the figure size here
        plt.scatter(range(len(current_sequence)), current_sequence, marker='.', color='r', s=5)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title(f'Sequence of Length {len(current_sequence)} at Step {step}')
        plt.grid()
        plt.savefig(os.path.join(self.output_dir, f'step_{step}.png'))  # Save the plot as a PNG file
        plt.close()  # Close the plot to free memory

    def Merge(self, p, q, r, step, plot=0):
        """
        Merges two subarrays of A[p..r].
        First subarray is A[p..q]
        Second subarray is A[q+1..r]

        Args:
        p (int): The index of the first element in the left subarray.
        q (int): The index of the last element in the left subarray.
        r (int): The index of the last element in the right subarray.
        step (int): The step number for the current sorting stage, used for naming the file.
        """
        # Calculate the sizes of the two subarrays to be merged.
        n1 = q - p + 1  # Size of the left subarray.
        n2 = r - q      # Size of the right subarray.

        # Create temporary arrays L and R to hold the subarrays to be merged.
        L = [0] * (n1 + 1)  # L will hold the left subarray.
        R = [0] * (n2 + 1)  # R will hold the right subarray.

        # Copy data from the original array 'A' to the temporary arrays L and R.
        for i in range(n1):
            L[i] = self.A[p + i]
        for i in range(n2):
            R[i] = self.A[q + i + 1]

        # Set sentinel values at the end of the temporary arrays to simplify the merging.
        L[n1] = float("inf")  # Sentinel for the left subarray.
        R[n2] = float("inf")  # Sentinel for the right subarray.

        # Initialize indices for the temporary arrays and the main array.
        i = 0  # Index for the left subarray.
        j = 0  # Index for the right subarray.

        # Merge the two subarrays back into the original array 'A'.
        for k in range(p, r + 1):
            if L[i] <= R[j]:
                self.A[k] = L[i]  # The current element in the left subarray is smaller.
                i += 1
            else:
                self.A[k] = R[j]  # The current element in the right subarray is smaller.
                j += 1
        if plot:
            # Visualize the current state of the array after merging
            self.visualize_sort(self.A, step)

    def MergeSort(self, p, r, step=0):
        """
        Sorts an array using the Merge Sort algorithm.
        
        Args:
        p (int): The index of the first element in the subarray.
        r (int): The index of the last element in the subarray.
        step (int): The step number for the current sorting stage, used for naming the file.
        """
        # Check if the left index 'p' is less than the right index 'r', indicating a valid subarray.
        if p < r:
            # Calculate the midpoint 'q' of the subarray.
            q = (p + r) // 2

            # Recursively sort the left and right subarrays.
            self.MergeSort(p, q, step + 1)       # Sort the left subarray.
            self.MergeSort(q + 1, r, step + 1)   # Sort the right subarray.

            # Merge the sorted left and right subarrays.
            self.Merge(p, q, r, step)

    def Sort(self):
        """ Sorts the array using the Merge Sort algorithm and saves visualizations. """
        self.MergeSort(0, len(self.A) - 1)
        # print("Sorting complete. ")
        return self.A

class Set_creation:
    """ This class hase a single function for creating a random sequence with given length and range of whicht the values are retrieved."""
    def __init__(self, value_range):
        """
        Args:
        value_range (2d vector): The boundaries of the domain.
        length (int): The desired self.length of the sequence.
        """
        self.value_range = value_range
        # self.length = length

    def __repr__(self):
        print("__repr__")
        return self.value_range 
    
    def get_random_seq(self, size):
        """
        Returns:
        List: A list containing random elements within the specified range.
        """
        
        if size < 1:
            return []  # Return an empty list for an invalid self.length.

        start, end = self.value_range[0], self.value_range[1]
        rd_seq = []
        for i in range(size):
            rd_seq.append(rd.randint(start, end) )
        return rd_seq
    
    def get_multiple_random_seq(self, Sizes):
        """Creates multiple sequence in the given interval with possibly differend sizes given as a list.
        args
        Sizes: The list with the sizes of each random sequence
        returns the sequences as a list of lists.
        """
        Sequences =[]
        for size in Sizes:
            rd_seq = self.get_random_seq(size)
            Sequences.append(rd_seq)
        return Sequences 

# value_range, length = [0,1000] , 10000
# data = Set_creation(value_range).get_random_seq(length) 
# print(data == sorted(data) )

# merge_sort_instance = Mergesort(data)
# # heap_sort_instance = Heapsort(data)    
# print(merge_sort_instance["sorted_data"] == sorted(merge_sort_instance["sorted_data"])) 

# print(merge_sort_instance["recorted_time"]) 
# print(heap_sort_instance["recorted_time"]) 

