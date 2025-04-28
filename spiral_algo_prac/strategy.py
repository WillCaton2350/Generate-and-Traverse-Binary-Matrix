from abc import ABC, abstractmethod
from random import shuffle
import traceback
import logging

# STRATEGY PATTERN

# STEP 1: Abstract class and methods
# STEP 2: sub-class(es) with instance methods and functionality
# STEP 3: The actual strategy pattern's ability to switch between the family of algorithms
# STEP 4: Instantiate for dynamically switching between algos

# Explanation: We use a strategy pattern to cycle through different generated matrices and traverse each one using a spiral traversal algorithm.

class Abstract_Class(ABC):
    container = [1,0,1,0]
    result = []
    @abstractmethod
    def main(self):
        pass

    def spiral_traversal(self,matrix):
        try:
            top = 0
            bottom = len(matrix)
            left = 0
            right = len(matrix[0])
            while top < bottom and left < right: # Base Case
                # write a list comprehension with the += operand to iterate over the top row
                # traverse the top row from left to right then shift down after completion
                self.result += [matrix[top][i] for i in range(left,right)]
                top += 1
                
                self.result += [matrix[right-1][x] for x in range(top-1,bottom-1,-1)]
                right -= 1
                # re establish the Base Case
                if top < bottom:
                    self.result += [matrix[bottom-1][y] for y in range(right-1,left-1,-1)]
                    bottom -= 1
                
                if left < right:
                    self.result += [matrix[left][z] for z in range(bottom,top)]
                    left += 1
            return self.result
        except (ValueError,TypeError,IndexError) as err:
            logging.error(f'{err}')

class Generate(Abstract_Class):
    def main(self):
        try: # generate binary matrix (nested)
            matrix = [[ i for i in self.container] for i in self.container]
            print(f'Matrix 1: {matrix}')
            self.result = self.spiral_traversal(matrix) # Call stack
            print(f'Result 1: {self.result}')
            return self.result
        except (ValueError,TypeError,IndexError) as err:
            logging.error(f'{err}')

class Reversed(Abstract_Class):
    def main(self): # generate reversed binary matrix
        try:
            matrix = [[ i for i in reversed(self.container)] for i in reversed(self.container)]
            print(f'Matrix 2: {matrix}')
            self.result = self.spiral_traversal(matrix) # Call Stack
            print(f'Result 2: {self.result}')
            return self.result
        except (ValueError,TypeError,IndexError) as err:
            logging.error(f'{err}') 

class Transpose(Abstract_Class):
    def main(self):
        try:
            matrix = [[ i for i in self.container] for i in self.container]
            # generate a nested matrix
            transposed_matrix = [list(x) for x in zip(*matrix,strict=True)]
            # first we need to separate / pop all of the values out of the lists / matrix.
            # The zip() function pairs elements from each list based on their indices. (Transposing / Transforming)
            # new we need to write the expression which converts the tuple of values created by the zip() function into a list. (list(x))
            print(f'Matrix 3: {transposed_matrix}')
            self.result = self.spiral_traversal(transposed_matrix)
            print(f'Result 3: {self.result}')
            return self.result
        except ValueError as err:
            logging.error(f'{err}')

class Randomized(Abstract_Class):
    def main(self): # generate randomized binary matrix
        try:
            matrix = [shuffle(val:=self.container[:]) or val for i in range(4)]
            print(f'Matrix 4: {matrix}')
            self.result = self.spiral_traversal(matrix)
            print(f'Result 4: {self.result}')
            return self.result
        except (ValueError,TypeError,IndexError) as err:
            logging.error(f'{err}')  

       
class Strategy_Pattern: # Switch between strategies (The ability to choose and execute each strategy)
    def __init__(self,strategy: Abstract_Class):
        # Behavior for the Strategy pattern class when its used to set the first pattern. or Sub class.
        self.strategy = strategy
        self.set_strategy()
        # States
    def set_strategy(self):
        self.call_strategy = self.strategy
    
    def execute_strategy(self):
        return self.strategy.main()
    
if __name__ == "__main__":
    try:
        # Call each strategy dynamically (one at a time or the result list compounds (almost like concatenating values))
        #situation = Strategy_Pattern(Generate())
        #situation.execute_strategy()

        #situation = Strategy_Pattern(Reversed())
        #situation.execute_strategy()

        situation = Strategy_Pattern(Transpose())
        situation.execute_strategy()

        #situation = Strategy_Pattern(Randomized())
        #situation.execute_strategy()

    except KeyboardInterrupt:
        traceback.print_exc(limit=None,chain=None,file=None)
        
