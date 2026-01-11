
for bulls in range(101):
    for cows in range(101):  
        calves = 100 - bulls - cows
        if calves >= 0 and 10 * bulls + 5 * cows + 0.5 * calves == 100:
            print(f"Быков: {bulls}, коров: {cows}, телят: {calves}")