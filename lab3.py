import math

print("Введіть число N щоб вивисти список його дільників.")
N = input()
N = float(N)
N = math.ceil(N)
N = abs(N)
divisors = []
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)
print("Дільники числа", N, ":", divisors)
