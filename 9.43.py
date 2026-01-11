def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_list(nums):
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result
nums = list(map(int, input("Числа через пробел: ").split()))
print("НОД:", gcd_list(nums))