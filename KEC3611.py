def is_palindrome(value):
    """
    Function to check if a given string or number is a palindrome.

    Args:
        value: A string or number to check for palindrome property.

    Returns:
        bool: True if the input is a palindrome, False otherwise.
    """
    # Convert the input to a string to handle both string and numeric inputs
    value_str = str(value)

    # Compare the string with its reverse
    return value_str == value_str[::-1]

if __name__ == "__main__":
    # Get input from the user
    user_input = input("Enter a string or number to check if it's a palindrome: ")

    # Normalize input: remove non-alphanumeric characters and convert to lowercase
    normalized_input = ''.join(char.lower() for char in user_input if char.isalnum())

    # Check if the input is a palindrome
    if is_palindrome(normalized_input):
        print(f"The input '{user_input}' is a palindrome.")
    else:
        print(f"The input '{user_input}' is not a palindrome.")
