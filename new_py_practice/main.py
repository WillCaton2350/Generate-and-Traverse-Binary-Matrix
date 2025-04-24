import logging
import traceback
from random import shuffle


class singleton:
    __instance = None
    container = [0,1,2,3]
    result = []

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(singleton,cls).__new__(cls)
        return cls.__instance
    
    @classmethod
    def main(cls): # generate matrix
        try:
            cls.matrix = [shuffle(val:=cls.container[:]) or val for i in range(4)]
            print(cls.matrix)
            return cls.matrix
        except ValueError as e:
            logging.error(e)

    @classmethod
    def traversal(cls): # States 
        # set bounds

        # first_bound is the top point of the matrix at (0,y=0) y axis
        top = 0
        # second_bound is the last row in the matrix. the full length of it
        bottom = len(cls.matrix)

        # third_bound is the futhest left point of the matrix at (x=0,0) x-axis
        left = 0
        # fourth_bound are the columns in the matrix set from the frist row of the matrix
        right = len(cls.matrix[0])

        # (Behaviors)
        # Next we set the base case for the traversal algo 
        # the += operator appends multiple items to the list  (list comprehension)
        try:
            while top < bottom and left < right:
                # Traverse the top from left to right
                cls.result += [cls.matrix[top][i] for i in range(left,right)]
                top += 1

                # Traverse the right column from top to bottom
                cls.result += [cls.matrix[right-1][x] for x in range(top,bottom)]
                right -= 1

                # re establish the BaseCase
                if top < bottom:
                    # Traverse the bottom from right to left
                    cls.result += [cls.matrix[bottom-1][j] for j in range(right,left)]
                    bottom -= 1

                if left < right:
                    # Traverse the left column from bottom to top
                    cls.result += [cls.matrix[left][y] for y in range(bottom,top)]         
                    left += 1
            print(cls.result)
            return cls.result
        except IndexError:
            traceback.print_exc(file=None,chain=None,limit=None)

if __name__ == "__main__":
    singleton.main()
    singleton.traversal()

