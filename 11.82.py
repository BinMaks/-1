arr = [int(x) for x in input("Введите элементы массива: ").split()]
zero_ending_pairs = sum(1 for i in range(len(arr) - 1) if str(arr[i]).endswith('0') and str(arr[i+1]).endswith('0'))
print(f"Пар соседних элементов, оканчивающихся на 0: {zero_ending_pairs}")