
heights = list(map(float, input("Введите 25 ростов в убывающем порядке: ").split()))
i = int(input("Номер первого выбывшего (1-25): ")) - 1
j = int(input("Номер второго выбывшего (1-25): ")) - 1
heights.pop(j)
heights.pop(i)
print("Новый массив (23 элемента):", heights)

heights = list(map(float, input("Введите 25 ростов в убывающем порядке: ").split()))
h1 = float(input("Рост первого выбывшего: "))
h2 = float(input("Рост второго выбывшего: "))
heights.remove(h1)
heights.remove(h2)
print("Новый массив (23 элемента):", heights)