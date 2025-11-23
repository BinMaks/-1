x=int(input("Сколько лет Тане? "))
y=int(input("Сколько лет Мите?"))
average_age = (x+y)/ 2
diff_tanya = abs(x - average_age)
diff_mitya = abs(y - average_age)
print(f"\n ---Результат---")
print(f"Средний возраст: {average_age: .1f} лет")
print(f"Таня отличается от среднего на {diff_tanya: .1f} года")
print(f"Митя отличается от среднего на {diff_mitya: .1f} года")
