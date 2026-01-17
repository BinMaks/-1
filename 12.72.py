sentence = input("Введите предложение: ").lower()
pos_c = sentence.rfind('с')
pos_t = sentence.rfind('т')  
if pos_c > pos_t:
    print("Буква 'с' встречается позже")
elif pos_t > pos_c:
    print("Буква 'т' встречается позже")
else:
    print("Буквы 'с' и 'т' встречаются на одинаковых позициях или отсутствуют")