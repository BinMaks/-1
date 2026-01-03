students = [int(input(f"Число учеников в {i+1} классе: ")) for i in range(11)]
sum_odd = sum(students[i] for i in range(0, 11, 2))  
print("Число учеников в нечётных классах:", sum_odd)