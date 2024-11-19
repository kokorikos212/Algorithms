from class_Algorithms import *
from Tester import Tester

@Tester
class Heapsort(Algorithms):
    """
    A class representing the Heap Sort algorithm.
    This class inherits from the 'Algorithms' superclass and provides an implementation of the Heap Sort algorithm.
    """

    def __init__(self, array):
        """ Initializes the Heapsort with an array to sort. """
        super().__init__("Heap Sort")
        self.A = array

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
    
    def execute(self):
        """
        A wrapper for the `Sort` method to ensure compatibility with the Tester decorator.
        
        Returns:
            list: The sorted array.
        """
        return self.Sort()
    
if __name__ == "__main__":
    value_range, length = [0,1000] , 10000
    data = Set_creation(value_range).get_random_seq(length) 

    # Test the Heapsort class with Tester
    sorted_array = Heapsort(data).time_execution()
    print(f"Sorted Array: {sorted_array['result']}")
    print(f"Execution Time: {sorted_array['time']} seconds")