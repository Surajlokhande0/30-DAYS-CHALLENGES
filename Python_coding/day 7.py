MY_CONSTANT = 10

print("Original constant value:", MY_CONSTANT)

# Attempt to change the value of the constant
MY_CONSTANT = 20  # This will raise an error

# Attempt to change the value using a different variable
new_value = 30
MY_CONSTANT = new_value  # This will also raise an error

print("Updated constant value:", MY_CONSTANT)


