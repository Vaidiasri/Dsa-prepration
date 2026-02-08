import math

# Todo: Count the number of integer in the number
num = 4555
n = abs(int(num))
count = 0

if n == 0:
    count = 1

while n > 0:
    n = n // 10
    count += 1

print(count)  # 4
