import logging
import traceback
from random import shuffle

class singleton:
    __instance = None
    container = [0,1,2,3,4]
    result = []

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(singleton,cls).__new__(cls)
        return cls.__instance
    
    @classmethod
    def main(cls): # generate random matrix
        try:
            cls.matrix = [shuffle(root:=cls.container[:]) or root for i in range(5)]
            return cls.matrix
        except ValueError as e:
            logging.error(e)
    
    @classmethod
    def algo(cls):
        top = 0 # y-axis (0,0)
        bottom = len(cls.matrix)

        left = 0 # x-axis (0,0)
        right = len(cls.matrix[0]) # columns via first row

        try:
            # BaseCase
            while top < bottom and left < right:
                cls.result += [cls.matrix[top][i] for i in range(left,right)]
                top += 1

                cls.result += [cls.matrix[right-1][x] for x in range(top-1,bottom-1,-1)]
                right -= 1

                if top < bottom:
                    cls.result += [cls.matrix[bottom-1][j] for j in range(right-1,left-1,-1)] 
                    bottom -= 1

                if left < right:
                    cls.result += [cls.matrix[left][y] for y in range(bottom,top)]
                    left += 1
            return cls.result
        except (IndexError, TypeError):
            traceback.print_exc(limit=None,chain=None,file=None)

if __name__ == "__main__":
    singleton.main()
    singleton.algo()