import math

try:
    nums = list(map(int, input("Введіть числа: ").split()))
except ValueError:
    print("Помилка: введіть тільки цілі числа")
    exit()

if len(nums) == 0:
    print("Помилка: порожній список")
    exit()

n = len(nums)
cols = math.ceil(math.sqrt(n))
matrix = []

for i in range(0, n, cols):
    row = nums[i:i+cols]
    matrix.append(row)

print("Матриця:")
for row in matrix:
    print(row)

symmetric = True
rows = len(matrix)

for i in range(rows // 2):
    if matrix[i] != matrix[rows - 1 - i]:
        symmetric = False
        break

if symmetric:
    print("Матриця%s є симетричною" %(" НЕ" if not symmetric else ""))