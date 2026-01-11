def find_taxicab_number():
    cubes = [i**3 for i in range(1, 100)]
    sums = {}
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            s = cubes[i] + cubes[j]
            if s not in sums:
                sums[s] = []
            sums[s].append((cubes[i], cubes[j]))
    for s in sorted(sums.keys()):
        if len(sums[s]) >= 2:
            return s, sums[s]
    return None
result = find_taxicab_number()
if result:
    print("Наименьшее число:", result[0])
    print("Способы представления:", result[1])