from itertools import chain
rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

def get_squares(matrix):
    squares = []
    for i in range(rows - 2):
        for j in range(cols - 2):
            square = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
            ]
            squares.append(square)
    return squares


def sum_squares(matrix):
    return sum(chain(*matrix))


def get_max_square(squares):
    max_square_sum = None
    max_square = None
    for square in squares:
        square_sum = sum_squares(square)
        if max_square_sum is None or square_sum > max_square_sum:
            max_square_sum = square_sum
            max_square = square
    return max_square

squares = get_squares(matrix)
max_square = get_max_square(squares)
print(f"Sum = {sum_squares(max_square)}")
print('\n'.join([' '.join(map(str, row)) for row in max_square]))