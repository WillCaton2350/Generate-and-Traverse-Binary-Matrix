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
    def main(cls): 
        try:
            cls.matrix = [shuffle(val:=cls.container[:]) or val for i in range(4)]
            return cls.matrix
        except ValueError as e:
            logging.error(e)

    @classmethod
    def traversal(cls): 
        top = 0
        bottom = len(cls.matrix)
        left = 0
        right = len(cls.matrix[0])
        try:
            while top < bottom and left < right:
                cls.result += [cls.matrix[top][i] for i in range(left,right)]
                top += 1
                cls.result += [cls.matrix[right-1][x] for x in range(top,bottom)]
                right -= 1
                if top < bottom:
                    cls.result += [cls.matrix[bottom-1][j] for j in range(right,left)]
                    bottom -= 1
                if left < right:
                    cls.result += [cls.matrix[left][y] for y in range(bottom,top)]         
                    left += 1
            return cls.result
        except IndexError:
            traceback.print_exc(file=None,chain=None,limit=None)
        except TypeError as err:
            logging.error(err)

if __name__ == "__main__":
    singleton.main()
    singleton.traversal()