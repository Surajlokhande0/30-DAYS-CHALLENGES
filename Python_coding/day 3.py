# Input string
input_str = "Hello, World!"

# Initialize an empty string to store the reversed string
reversed_str = ""

# Iterate through the input string in reverse order
for i in range(len(input_str) - 1, -1, -1):
    reversed_str += input_str[i]

# Print the reversed string
print("Reversed String:", reversed_str)
