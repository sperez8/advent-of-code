import re
import numpy as np
from scipy import ndimage

RE_MSAMS_PATTERN = r"M.S.A.M.S"
x_mas_both_forward = re.compile(RE_MSAMS_PATTERN)

RE_MMASS_PATTERN = r"M.M.A.S.S"
x_mas_one_forward = re.compile(RE_MMASS_PATTERN)

def solve(file):
    # convert to a matrix
    matrix = np.genfromtxt(file, dtype=str, delimiter=1)

    count = 0

    # we iterate through 3x3 portions of the matrix
    for i in range(matrix.shape[0]-2):
        for j in range(matrix.shape[1]-2):
            submatrix = matrix[i:i+3,j:j+3]
            # flatten and detect
            if bool(re.search(re.compile(r"M.S.A.M.S"), "".join(submatrix.flatten()))):
                count += 1
            if bool(re.search(re.compile(r"M.M.A.S.S"), "".join(submatrix.flatten()))):
                count += 1
            if bool(re.search(re.compile(r"S.M.A.S.M"), "".join(submatrix.flatten()))):
                count += 1
            if bool(re.search(re.compile(r"S.S.A.M.M"), "".join(submatrix.flatten()))):
                count += 1

    return count
        
        
if __name__ == "__main__":
    # Open the file in read mode
    with open('input_day4.txt', 'r') as file:
        result = solve(file)
        print(f"And the answer is {result}")
