tolerance = 0.01
numerator1, denominator1 = 1, 1
numerator2, denominator2 = 2, 1
print(f"1-й член: {numerator1}/{denominator1} = {numerator1/denominator1}")
print(f"2-й член: {numerator2}/{denominator2} = {numerator2/denominator2}")
n = 3
while True:
    next_numerator = numerator1 + numerator2
    next_denominator = denominator1 + denominator2
    next_value = next_numerator / next_denominator
    prev_value = numerator2 / denominator2
    print(f"{n}-й член: {next_numerator}/{next_denominator} = {next_value}")
    if abs(next_value - prev_value) <= tolerance:
        print(f"Первый член, отличающийся не более чем на {tolerance} от предыдущего: {next_numerator}/{next_denominator}")
        break
    numerator1, denominator1 = numerator2, denominator2
    numerator2, denominator2 = next_numerator, next_denominator
    n += 1