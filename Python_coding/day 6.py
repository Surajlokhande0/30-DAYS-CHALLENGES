#print middle element of linklist/array


def find_middle_element(arr):
    if not arr:
        return None

    middle_index = len(arr) // 2
    return arr[middle_index]

# Test case
my_array = [1, 2, 3, 4, 5]
middle_element = find_middle_element(my_array)
print("Middle Element:", middle_element)
