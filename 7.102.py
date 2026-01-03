
students = []
heights = []
n = int(input("Количество учеников: "))
for i in range(n):
    name = input(f"Имя ученика {i+1}: ")
    height = float(input(f"Рост ученика {i+1} (см): "))
    students.append(name)
    heights.append(height)

out_of_order = False
for i in range(1, len(heights)):
    if heights[i] > heights[i-1]:
        print(f"Ученики не перечислены в порядке убывания роста. Нарушение на {i+1}-м ученике")
        out_of_order = True
        break
if not out_of_order:
    print("Ученики перечислены в порядке убывания роста")