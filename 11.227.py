
lengths = list(map(float, input("Длины (12 значений): ").split()))
widths = list(map(float, input("Ширина (12 значений): ").split()))
heights = list(map(float, input("Высоты (12 значений): ").split()))
for i in range(12):
    volume = lengths[i] * widths[i] * heights[i]
    print(f"Объем {i+1}-го параллелепипеда: {volume}")