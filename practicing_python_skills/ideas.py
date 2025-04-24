from random import choices, choice, shuffle
import random 

container_list = [1,2,3,4,5]
container_dict = {
        0:1,
        1:0,
        2:1,
        3:0,
        4:1,
    }

# LONG FORM
def main():
    try:
        matrix_2 = []
        row = [i for i in container_list[:]]  # make a copy
        shuffle(row)                 # shuffle in place             # shuffle in place
        matrix_2.append(row)
        print(matrix_2)
    except Exception:
        raise ValueError

# SHORT HAND
def main_2():
    matrix = [shuffle(row := container_list[:]) or row for _ in range(4)]
    # The walrus operator assigns a copy of container_list to 'row' and shuffles it in place.
    # The 'or row' ensures that the shuffled 'row' (not 'None', which the shuffle() object/function returns) is added to the matrix.
    # We repeat the process 4 times by using 'for _ in range(4)'.
    print(matrix)

    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    list_of_rows = [row_1,row_2,row_3,row_4]
    for l in list_of_rows:
        row_list = l
    var = [f for f in range(len(l))] # len gives me the list of indecies. Im looking for the first index of each row to create a column
    print('var: ', var)

        
main_2()