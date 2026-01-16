
heights = list(map(float, input("Росты учеников: ").split()))
is_ordered = all(heights[i] >= heights[i+1] for i in range(len(heights) - 1))
if is_ordered:
    print("Ученики перечислены в порядке убывания роста")
else:
    print("Ученики не перечислены в порядке убывания роста")