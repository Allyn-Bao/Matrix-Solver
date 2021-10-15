import math


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
    :param factor: float, factor
    :return: matrix
    """
    for i in range(len(matrix[row_index])):
        if matrix[row_index][i] != 0:
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


def row_operation_multiply(row, factor):
    """
    multiply all elements of the row by the factor
    :param row: list, row
    :param factor: float, factor
    :return: list, new row
    """
    return list(map(lambda x: x * factor if x != 0 else x, row))


def row_operation_addition(row1, row2, subtract=False):
    """
    add corresponding elements from row1 & row2, return the new row (list)
    :param row1: list, first row
    :param row2: list, second row
    :param subtract: boolean, true if subtraction, set to false as default
    :return: list, new row
    """
    new_row = []
    subtract_factor = -1 if subtract else 1
    for i in range(len(row1)):
        new_row.append(row1[i] + row2[i] * subtract_factor)
    return new_row


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


def row_in_REF(matrix, row_index):
    """
    check leading one's existence and position.
    if leading one exists and index of leading one == row_index => row is in REF
    or if all coefficients == 0, don't care about the constant (last element in list)
    :param matrix: list, matrix
    :param row_index: int, index of the row being examined
    :return: True if row is in REF from, otherwise False
    """
    for i in range(len(matrix[row_index]) - 1):
        if i < row_index and matrix[row_index][i] != 0:
            return False
        if i == row_index and (matrix[row_index][i] != 1 and matrix[row_index][i] != 0):
            return False
    return True


def locate_leading_coefficient_in_row(matrix, row_index):
    """
    return the index of the first non-zero coefficient in row
    return -1 if all elements in row == 0
    :param matrix: list, matrix
    :param row_index: int, row index
    :return: int, index of coefficient
    """
    for i in range(len(matrix[row_index])):
        if matrix[row_index][i] != 0:
            return i
    return -1


def all_elements_in_row_is_zero(matrix, row_index):
    """
    :param matrix: list, matrix
    :param row_index: int, index of row
    :return: boolean, True if all element in row == 0
    """
    for num in matrix[row_index][:-1]:
        if num != 0:
            return False
    return True


def has_no_solution(matrix):
    """
    check if system has no solution
    (if in a row, all coefficient == 0, while the constant is non zero)
    :param matrix: list, matrix
    :return: True if system has no solution
    """
    for i in range(len(matrix)):
        if all_elements_in_row_is_zero(matrix, i) and matrix[i][-1] != 0:
            return True
    return False


def infinite_solution(matrix):
    """
    return True if matrix has infinite solution
    (all zero in at least one row)
    :param matrix: list, matrix
    :return: boolean, True if system has infinite solution
    """
    for i in range(len(matrix)):
        if all_elements_in_row_is_zero(matrix, i) and matrix[i][-1] == 0:
            return True
    return False


def error_rounder(matrix):
    """
    for errors made due to rounding in calculation, round number extremely close to an integer to the next closest integer
    ex. 2.9999999999999996 => 3
    :param matrix: list, matrix
    :return: list, new matrix
    """
    # constant minimum threshold, any number smaller is considered to be an error
    MIN_THRESHOLD = math.pow(10, -10)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if 0 < abs(matrix[i][j] - math.ceil(matrix[i][j])) < MIN_THRESHOLD:
                matrix[i][j] = math.ceil(matrix[i][j])
            elif 0 < abs(matrix[i][j] - math.floor(matrix[i][j])) < MIN_THRESHOLD:
                matrix[i][j] = math.floor(matrix[i][j])

    return matrix


def matrix_solver(matrix):
    """
    solve the system of linear equations in matrix form, return the matrix in RREF form
    :param matrix: list, matrix
    :return: list, matrix in RREF form;
             int, 0 if NO SOLUTION, 1 if UNIQUE SOLUTION, 2 if INFINITE SOLUTION
    """
    # LEADING ONES
    for i in range(len(matrix)):
        while not row_in_REF(matrix, i):
            # eliminate calculation rounding errors
            matrix = error_rounder(matrix)
            # locate leading coefficient in row
            lc_index = locate_leading_coefficient_in_row(matrix, i)
            # in the case where all elements of the row == 0
            if lc_index == -1:  # no L.C. found
                break
            # reduce leading coefficient to a leading one - divide all elements of row by the L.C.
            lc = matrix[i][lc_index]
            matrix[i] = row_operation_multiply(matrix[i], 1 / lc)
            # if leading one index overlap with leading ones in prev rows
            if lc_index != i:
                # subtract row by prev row to eliminate current L.C.
                matrix = add_rows(matrix, i, lc_index, subtract=True)
    # RREF FORM
    for i in range(len(matrix)):
        # eliminate calculation rounding errors
        matrix = error_rounder(matrix)
        # go though all the coefficients after the leading one
        for j in range(i + 1, len(matrix[i]) - 1):
            if j < len(matrix[i]):
                matrix[i] = row_operation_addition(matrix[i],
                                                   row_operation_multiply(matrix[j], matrix[i][j]),
                                                   subtract=True)
    # check if no solution / infinite solutions / unique solution
    if has_no_solution(matrix):
        return matrix, 0
    elif infinite_solution(matrix):
        return matrix, 2
    else:
        return matrix, 1


if __name__ == "__main__":
    dimension, num_rows, matrix = console_input()
    console_print_matrix(matrix)
    print("\n")
    matrix, number_solutions = matrix_solver(matrix)
    console_print_matrix(matrix)
    if number_solutions == 0:
        print("NO SOLUTION")
    elif number_solutions == 1:
        print("UNIQUE SOLUTION")
    elif number_solutions == 2:
        print("INFINITE SOLUTION")
