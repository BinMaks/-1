k = int(input("Введите номер дня в году (1-365):"))
n_a = k % 7
n_b = (k+1) % 7
d = int(input("Введите d (1-7):"))
shift = (k + d - 2) % 7
n_c = 0 if shift == 6 else shift + 1
print("a) День недели (1 янв - пн): ", n_a)
print("б) День недели (1 янв - вт): ", n_b)
print("в) День недели (1 янв - d-й день)", n_c)