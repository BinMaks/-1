n = int(input("Введите количество школьников N:"))
k = int(input("Введите количество яблок  k:"))
apples_per_student = k//n
apples_in_basket = k%n
print("Каждому школьнику достанется:", apples_per_student, "яблок(а)")
print("В корзинке останется:", apples_in_basket, "яблок(a)")