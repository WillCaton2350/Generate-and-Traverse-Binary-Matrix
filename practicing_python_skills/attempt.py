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
    def rows(cls):       

        # get each row in the binary matrix

        try:
           for i in cls.matrix[0:1]:
               cls.row_1 = i
               print('Row 1: ',cls.row_1)
            
           for j in cls.matrix[1:2]:
               cls.row_2 = j
               print('Row 2: ',cls.row_2)

           for k in cls.matrix[2:3]:
               cls.row_3 = k
               print('Row 3: ',cls.row_3)

           for v in cls.matrix[3:4]:
               cls.row_4 = v
               print('Row 4: ',cls.row_4)
        except TypeError:
            traceback.print_exc(file=None,limit=None,chain=None)
    
    @classmethod
    def columns(cls):

        # get the first column of the binary matrix

        try:
            for h in cls.row_1:
                break 
            for s in cls.row_2:
                break 
            for d in cls.row_3:
                break 
            for c in cls.row_4:
                break 
            var = [h,s,d,c]
            print(f'Column 1: {var} ')
        except TypeError:
            traceback.print_exc(file=None,limit=None,chain=None)

if __name__ == "__main__":
    singleton.main()
    singleton.rows()
    singleton.columns()


