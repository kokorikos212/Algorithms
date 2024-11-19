import time 
import random as rd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import time, os 

import pprint
    
class Algorithms:
    """
    A central class for executing different algorithms dynamically based on their name.
    The specific algorithm functionality should be implemented in subclasses.
    
    Attributes:
        algorithm_name (str): Name of the algorithm to be executed.
    """
    
    def __init__(self, algorithm_name):
        """
        Initializes the algorithm with a given name.
        
        Args:
            algorithm_name (str): Name of the algorithm to execute.
        """
        self.algorithm_name = algorithm_name
    
    def execute(self, *args, **kwargs):
        """
        Executes the specified algorithm's main function dynamically.
        The algorithm should be implemented as a method in a subclass.
        
        Args:
            *args: Variable length argument list for the algorithm function.
            **kwargs: Arbitrary keyword arguments for the algorithm function.
        
        Returns:
            Any: Result of the algorithm's execution.
        
        Raises:
            NotImplementedError: If the specified algorithm is not implemented.
        """
        method_name = self.algorithm_name
        method = getattr(self, method_name, None)

        if callable(method):
            return method(*args, **kwargs)
        else:
            raise NotImplementedError(f"The algorithm {self.algorithm_name} is not implemented.")

    
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




