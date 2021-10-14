def console_input():
    """
    prompt for console input of the matrix
    :return: dimension, int, dimension of the equation (R^n)
    :return: num_rows, int, number of equations (number of rows)
    :return: matrix, list, matrix
    """
    dimension = int(input("Enter the Dimension: "))
    num_rows = int(input("Enter the number of Rows: "))
    matrix = []
    for _ in range(num_rows):
        matrix += [list(map(lambda x: float(x), input().split()))]
    return dimension, num_rows, matrix


def console_print_matrix(matrix):
    """
    print matrix to console
    :param matrix: list, matrix
    :return: Void
    """
    for row in matrix:
        print("|\t" + "\t".join(list(map(str, row))[:-1]) + "\t|\t" + str(row[-1]) + "\t|")


def swap_rows(matrix, index_1, index_2):
    """
    switch the position of two rows in matrix by index
    :param matrix: list, matrix
    :param index_1: int, index for row 1
    :param index_2: int, index for row 2
    :return: matrix, list, matrix with rows swapped
    """
    matrix[index_1], matrix[index_2] = matrix[index_2], matrix[index_1]
    return matrix


def multiply_row(matrix, row_index, factor):
    """
    multiply every element of the row in matrix by the factor
    :param matrix: list, matrix contain all equations
    :param row_index: int, index of the row to be modified
    :param factor: double, factor
    :return: matrix
    """
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] *= factor
    return matrix


def add_rows(matrix, base_row_index, add_row_index, subtract=False):
    """
    add one row to another, store the new values at the "base_row"
    :param matrix: list, matrix
    :param row_base_index: int, index of row that will soon be repace wih new value
    :param row_add_index: int, index of the row being added to the other
    :param subtract: boolean, True if subtraction, set to false as default
    :return: matrix
    """
    subtract_factor = -1 if subtract else 1
    for i in range(len(matrix[base_row_index])):
        matrix[base_row_index][i] += matrix[add_row_index][i] * subtract_factor
    return matrix


def check_RREF(matrix):
    """
    check if:
        a) Each leading entry is a 1 (leading one)
        b) Each leading one is the only nonzero entry in its column
    :param matrix: list, matrix
    :return: 0 if all requirements meet,
            else return index, int if at the first row that no longer satisfied the rules
    """
    for i in range(len(matrix)):
        # a)
        leading_one_met = True if matrix[i][i] == 1.0 else False
        # b)
        only_nonzero_met = True
        for k in range(len(matrix)):
            if k != i and matrix[k][i] != 0:
                only_nonzero_met = False
        if not leading_one_met or not only_nonzero_met:
            return i
    return 0


if __name__ == "__main__":
    # input
    dimension, num_rows, matrix = console_input()
    console_print_matrix(matrix)
    print("\n")
