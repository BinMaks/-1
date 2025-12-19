x = int(input("x = "))
y = int(input("y = "))
result = 0
for _ in range(abs(y)):
    result += abs(x)
if (x < 0) ^ (y < 0):
    result = -result
print(f"x * y = {result}")