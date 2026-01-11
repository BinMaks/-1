import random

from collections import Counter
def roll_dice_n_times(n):
    return [random.randint(1, 6) for _ in range(n)]
def calculate_relative_frequency(rolls):
    counter = Counter(rolls)
    total = len(rolls)
    frequencies = {i: counter[i] / total for i in range(1, 7)}
    return frequencies
rolls_100 = roll_dice_n_times(100)
freq_100 = calculate_relative_frequency(rolls_100)
print("Относительная частота при 100 бросках:", freq_100)
rolls_1000 = roll_dice_n_times(1000)
freq_1000 = calculate_relative_frequency(rolls_1000)
print("Относительная частота при 1000 бросках:", freq_1000)