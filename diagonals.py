n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

result1 = 0
result2 = 0
diagolal1 = []
diagonal2 = []


for x in range(n):
    result1 += matrix[x][x]
    diagolal1.append(matrix[x][x])

for x in range(n):
    result2 += matrix[x][n - x - 1]
    diagonal2.append(matrix[x][n - x - 1])

print(f"First diagonal: {', '.join([str(x) for x in diagolal1])}. Sum: {result1}")
print(f"Second diagonal: {', '.join([str(x) for x in diagonal2])}. Sum: {result2}")