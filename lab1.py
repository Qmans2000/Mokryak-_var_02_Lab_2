import sys
print("Введіть список неменьш з 5 чисел")
data = list(map(int, input().split()))
if len(data) < 5:
    print("Потрібно ввести не менше 5 чисел.")
    sys.exit(1)
else:
    data.sort(reverse=True) 
    result = sum(x**3 for x in data[:5])
    print(result)
