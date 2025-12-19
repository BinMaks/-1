fib = [1, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
print("Члены с 3 по 10:", fib[2:10])