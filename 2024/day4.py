import re
import numpy as np
from scipy import ndimage

RE_XMAS_PATTERN = r"XMAS"
xmas = re.compile(RE_XMAS_PATTERN)

def count_xmas_in_row(line):
    return len(re.findall(xmas, "".join(line)))

def count_xmas_accross_rows(matrix):
    return np.apply_along_axis(count_xmas_in_row, axis=1, arr=matrix).sum()

def count_xmas_accross_diagonals(diags):
    return sum([count_xmas_in_row(l) for l in diags])

def mirror(matrix):
    return np.flip(matrix)

def flip_vertically(matrix):
    return np.flip(matrix, axis=0)

def transpose(matrix):
    return np.transpose(matrix)

def get_diagonals(matrix):
    # assuming a square?
    diagonals = []
    n_offsets = max(matrix.shape)
    for o in range(1-n_offsets, n_offsets):
        diagonals.append(matrix.diagonal(offset=o))
    return diagonals

def solve(file):
    # convert to a matrix
    matrix = np.genfromtxt(file, dtype=str, delimiter=1)

    # transform the matrix such that we can count the number of "XMAS" along rows for each
    count = 0
    
    # horizontal xmas
    count += count_xmas_accross_rows(matrix)

    # mirror image for horizontal backwards xmas
    count += count_xmas_accross_rows(mirror(matrix))

    # transposed for vertical top to bottom xmas
    count += count_xmas_accross_rows(transpose(matrix))

    # transposed and mirror for vertical bottom to top xmas
    count += count_xmas_accross_rows(transpose(mirror(matrix)))

    # Get \ diagonal top to bottom xmas
    count += count_xmas_accross_diagonals(get_diagonals(matrix))

    # Get / diagonal top to bottom xmas
    count += count_xmas_accross_diagonals(get_diagonals(mirror(matrix)))

    # Get / diagonal bottom to top xmas
    count += count_xmas_accross_diagonals(get_diagonals(flip_vertically(matrix)))

    # Get \ diagonal bottom to top xmas
    count += count_xmas_accross_diagonals(get_diagonals(flip_vertically(mirror(matrix))))

    return count
        
        
if __name__ == "__main__":
    # Open the file in read mode
    with open('input_day4.txt', 'r') as file:
        result = solve(file)
        print(f"And the answer is {result}.")
