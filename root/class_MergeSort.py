from class_Algorithms import *
from Tester import Tester

@Tester
class Mergesort(Algorithms):
    """ 
    A class representing the Merge Sort algorithm.
    This class inherits from the 'Algorithms' superclass and provides an
    implementation of the Merge Sort sorting algorithm.
    """

    def __init__(self, array, output_dir='plots'):
        """ Initializes the MergeSort with an array to sort and a directory to save plots. """
        super().__init__("Merge Sort")
        self.A = array
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

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
        print("Sorting complete. ")
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
    sorted_array = Mergesort(data).time_execution()
    print(f"Sorted Array: {sorted_array['result']}")
    print(f"Execution Time: {sorted_array['time']} seconds")
