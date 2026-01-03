c = [float(input(f"c{i+1} = ")) for i in range(15)]
sum_c = -sum(c[i] for i in range(0, 15, 2))  
print("Сумма -c₁ - c₃ - ...:", sum_c)