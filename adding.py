def is_palindrome(string):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function
test_string = input("Enter a string: ")
if is_palindrome(test_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
