from random import shuffle
import traceback
import logging

# SINGLETON PATTERN

# STEP 1: Create singleton instance
# STEP 2: Generate matrix
# STEP 3: Traverse the matrix
# Explanation: We use a singleton pattern to create a single instance that generates a randomized binary matrix and traverses it using a spiral traversal algorithm.

class singleton:
    __instance = None
    container = [0,1,0,1,0]
    result = []

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(singleton,cls).__new__(cls)
        return cls.__instance
    
    @classmethod
    def main(cls): # Generate Martrix
        # we have to make a list of list from the numbers in the container (matrix variable, list comp)
        try:
            cls.matrix = [shuffle(root:=cls.container[:]) or root for i in range(5)] # (5) because the number of items or integers in the list
            # slicing to use the length of the whole list
        except ValueError:
            traceback.print_exc(limit=None,chain=None,file=None)
        return cls.matrix

    @classmethod
    def spiral_matrix(cls): # first we need to set and id the bounds of the matrix
        top = 0
        bottom = len(cls.matrix)
        left = 0
        right = len(cls.matrix[0])
        try:
            # Now Set a BaseCase
            while top < bottom and left < right:
                # create the list comp. Use the += operator to assing multiple values to the same list (aka multiple values to the same result empty list)
                # traverse the (top) row from (left to right ) with the (iterator) and shift to the next (row) or column in this case its the (top) row. from top to bottom.
                cls.result += [cls.matrix[top][i] for i in range(left,right)]
                # At the end of the traversal of the top row we shift down because we have completed the first row of the matrix.
                top += 1 
                # traverse the far (right column) from (top to bottom) with the (iterator) and shift to the next column. (shift to the left -1)
                cls.result += [cls.matrix[right-1][x] for x in range(top-1,bottom-1,-1)] 
                right -=1 
                # re-enforce the BaseCase with a conditional statement.
                if top < bottom:
                    cls.result += [cls.matrix[bottom-1][y] for y in range(right-1,left-1,-1)]
                    bottom -= 1 
                # re-enforce the BaseCase with a conditional statement.
                if left < right:
                    cls.result += [cls.matrix[left][z] for z in range(bottom,top)] # Because left and right are columns, positive and negative are top to bottom and vise versa. 
                    left += 1
            # print / return the result
            return cls.result   
        except (IndexError,TypeError) as e:
            logging.error(e)       
    
if __name__ == "__main__":
    try:
        # instantiate
        instance = singleton()
        instance.main() 
        instance.spiral_matrix()
    except KeyboardInterrupt:
        traceback.print_exc(limit=None,chain=None,file=None)
