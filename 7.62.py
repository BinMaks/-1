n = int(input("Введите n: "))
p = int(input("Введите p: "))
k = int(input("Введите k: "))
a = [int(input(f"a{i+1} = ")) for i in range(n)]

count_greater_p = sum(1 for x in a if x > p)
count_ends_with_5 = sum(1 for x in a if x % 10 == 5)
count_divisible_k = sum(1 for x in a if x % k == 0)

print("а) Чисел > p:", count_greater_p)
print("б) Чисел, оканчивающихся на 5:", count_ends_with_5)
print("в) Чисел, кратных k:", count_divisible_k)