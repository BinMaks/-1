
heights = [float(input(f"Рост {i+1}-го юноши (см): ")) for i in range(12)]
count_short = sum(1 for height in heights if height < 165)
print("Количество юношей с ростом менее 165 см:", count_short)
