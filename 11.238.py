january = list(map(float, input("Осадки за январь (мм, 31 день): ").split()))
march = list(map(float, input("Осадки за март (мм, 31 день): ").split()))
sum_january = sum(january)
sum_march = sum(march)
if sum_january > sum_march:
    print("Больше осадков в январе: ", sum_january, "мм")
elif sum_march > sum_january:
    print("Больше осадков в марте: ", sum_march, "мм")
else:
    print("Осадков одинаково: ", sum_january, "мм")