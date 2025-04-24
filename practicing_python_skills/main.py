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
            cls.matrix = [shuffle(root:=cls.container_list[:]) or root for i in range(4)]
            return cls.matrix
        except ValueError as e:
            logging.error(e)

    @classmethod
    def traversal(cls):       
        cls.result = []
        top = 0 
        bottom = len(cls.matrix) 
        left = 0
        right = len(cls.matrix[0])
        try:
            while top < bottom and left < right:
                for i in range(left,right):
                    cls.result.append(cls.matrix[top][i])
                top += 1
                for x in range(top,bottom):
                    cls.result.append(cls.matrix[right-1][x])
                right -= 1
                if top < bottom: 
                    for y in range(right-1,left-1,-1):
                        cls.result.append(cls.matrix[bottom-1][y])
                    bottom -= 1
                if left < right:
                    for z in range(bottom-1,top-1,-1):
                        cls.result.append(cls.matrix[left][z])
                    left += 1
            return cls.result
        except (IndexError,TypeError) as e:
            logging.error(e)
            traceback.print_exc(file=None,chain=None,limit=None)

if __name__ == "__main__":
    singleton.main()
    singleton.traversal()