#string pelindrome without using inbuilt function

def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

# Test cases
string1 = "racecar"
string2 = "hello"

print(is_palindrome(string1))  # True
print(is_palindrome(string2))  # False
