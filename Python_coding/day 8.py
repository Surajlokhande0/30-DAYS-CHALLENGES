def find_max_and_min(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    return max_num, min_num

# Test case
num1 = 15
num2 = 7

maximum, minimum = find_max_and_min(num1, num2)
print("Maximum:", maximum)
print("Minimum:", minimum)
