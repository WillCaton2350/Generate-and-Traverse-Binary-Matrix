from random import shuffle
import logging
import traceback


class singleton:
    __instance = None
    container_list = [0,1,0,1]

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(singleton,cls).__new__(cls)
        return cls.__instance
    
    @classmethod
    def main(cls):
        try:
            # generate random binary matrix

            cls.matrix = [shuffle(root:=cls.container_list[:]) or root for i in range(4)]
            #####cls.matrix = [[z for z in cls.container_list] for x in cls.container_list]
            print(cls.matrix)
            return cls.matrix
        except ValueError as e:
            logging.error(e)

    @classmethod
    def traversal(cls):       
        result = []
        # step 1: (STATES)  Identify and set the bounds of the matrix: top, botton, right, left
        # step 2: (STATES)  Set the BaseCase
        top = 0 # The Top Row
        bottom = len(cls.matrix) # Last Possible Row / Bottom Row

        left = 0 # The First left column
        right = len(cls.matrix[0])# The columns start from the top row or index 0 of the matrix

        try:
            while top < bottom and left < right: # BaseCase
                # At the end of the matrix, the top row becomes the bottom. so there is no longer a top row (means: top < bottom)
                # At the end of the matrix, the left column becomes the right column. so there is no longer a left column (means: left < right)

                # Traverse top row from left to right
                for i in range(left,right):
                    result.append(cls.matrix[top][i])
                top += 1 # Move down to the next row (row one of the matrix is complete)

                # Traverse right column from top to bottom
                for x in range(top,bottom):
                    result.append(cls.matrix[right-1][x])
                right -= 1 # Move left to the next column (The furthest column in the matrix is complete)

                # Traverse bottom row from right to left
                if top < bottom: # Recreate the BaseCase
                    for y in range(right-1,left-1,-1):
                        result.append(cls.matrix[bottom-1][y])
                    bottom -= 1

                # Traverse left row from bottom to top
                if left < right:
                    for z in range(bottom-1,top-1,-1):
                        result.append(cls.matrix[left][z])
                    left += 1
            print(result)
            return result
        except (IndexError,TypeError) as e:
            logging.error(e)
            traceback.print_exc(file=None,chain=None,limit=None)

if __name__ == "__main__":
    singleton.main()
    singleton.traversal()



