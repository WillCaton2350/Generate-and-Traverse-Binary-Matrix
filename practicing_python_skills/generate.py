import logging
from random import shuffle

# The walrus operator assigns a function and/or value to a variable.

class singleton:
    __instance = None
    container_list = [1,2,3,4,5]
    container_dict = {
        0:1,
        1:0,
        2:1,
        3:0,
        4:0,
    }

    def __new__(cls,*args,**kwargs):
        try:
            if cls.__instance is None:
                cls.__instance = super(singleton,cls).__new__(cls)
            return cls.__instance
        except RuntimeError as err:
            logging.error("Singleton instance could not be created.")
            raise err
        
    @classmethod
    def main(cls): # GENERATE A MATRIX USING A NESTED LIST COMPREHENSION
        try:
            matrix_2 = [[i for i in cls.container_list] for x in cls.container_list]
            # the first/nested list comprehension becomes the expression for the outer list comprehension. Thats how you nest a list comprehension to create a matrix
            print(matrix_2)
        except ValueError:
            logging.error()

        try: # RANDOMIZING THE VALUES IN THE MATRIX
            matrix_3 = [shuffle(row := cls.container_list[:]) or row for i in range(5)]
            # Expresion : shuffle(row := cls.container_list[:]) or row
            # The walrus operator assigns a copy of container_list to 'row' and shuffles it in place.
            # The 'or row' ensures that the shuffled 'row' (not 'None', which the shuffle() object/function returns) is added to the matrix.
            # We repeat the process 4 times by using 'for _ in range(4)'. Creates 4 rows in the matrix
            print(matrix_3)
        except ValueError:
            logging.error()
            
        try:
            # Here we are using the walrus operator with the lambda variable vars to call the cls.container function once instead of twice like up above, increasing the speed of the list comprehension. 
            matrix_4 = (lambda vals: [[i for i in vals] for _ in vals])(vals := list(cls.container_dict.values()))
            print(matrix_4)
        except ValueError:
            logging.error()

if __name__ == "__main__":
    singleton.main()
