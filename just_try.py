from collections import deque

rows_count, cols_count = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for _ in range(rows_count):
    matrix.append(["" for _ in range(cols_count)])

for row in range(rows_count):
        for col in range(cols_count):
            element = text.popleft()
            matrix[row][col] = element
            text.append(element)
for row in range(rows_count):
    if row % 2 != 0:
        result= list(reversed(matrix[row]))
        matrix[row] = result

for row in range(rows_count):
    print(''.join(matrix[row]))