x = [int(input(f"x[{i+1}] = ")) for i in range(12)]
all_equal = all(elem == x[0] for elem in x)
print("Все элементы равны между собой" if all_equal else "Элементы не равны между собой")