def find_second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    
    first_max = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])

    for num in arr[2:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    return second_max

# Test the function
my_array = [12, 35, 1, 10, 34, 1]
result = find_second_largest(my_array)
print("The second largest element is:", result)
