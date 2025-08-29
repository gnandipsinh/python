






text = input("Enter a string: ")

reversed_text = text[::-1]
print("Reversed String:", reversed_text)


if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
