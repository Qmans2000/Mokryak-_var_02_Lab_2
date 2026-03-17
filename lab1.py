import sys
import math

print("Введіть координати чотирьох точок (x1 y1 x2 y2 x3 y3 x4 y4):")
data = list(map(float, input().split()))
if len(data) != 8:
    print("Потрібно 8 чисел.")
    sys.exit(1)
pts = [(data[i], data[i+1]) for i in range(0, 8, 2)]

# центр 
cx = sum(p[0] for p in pts) / 4
cy = sum(p[1] for p in pts) / 4

pairs = []
for i in range(4):
    for j in range(i+1, 4):
        mx = (pts[i][0] + pts[j][0]) / 2
        my = (pts[i][1] + pts[j][1]) / 2
        if abs(mx - cx) < 1e-9 and abs(my - cy) < 1e-9:
            pairs.append((i, j))

if len(pairs) != 2: 
    print("Введені точки не утворюють паралелограм.") 
    sys.exit(1)

(i1, j1), (i2, j2) = pairs

# діагоналі
d1x = pts[i1][0] - pts[j1][0]
d1y = pts[i1][1] - pts[j1][1]
d2x = pts[i2][0] - pts[j2][0]
d2y = pts[i2][1] - pts[j2][1]

len1 = math.hypot(d1x, d1y)
len2 = math.hypot(d2x, d2y)

# площа
area = 0.5 * abs(d1x * d2y - d1y * d2x)

print(f"{area:.3f}")
print(f"{len1:.3f} {len2:.3f}")