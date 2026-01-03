a = [int(input(f"a{i+1} = ")) for i in range(20)]
sum_a = sum(a[i] for i in range(1, 20, 2))  
print("Сумма a₂ + a₄ + ...:", sum_a)