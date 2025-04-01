# ask user to input a statement
user_input = input("Please enter a statement: ")
# convert each character from string to upper
uppercase_user_input = ""
for char in user_input:
    if 'a' <= char <= 'a':
        uppercase_user_input += chr(ord(char) - 32)
    else:
        uppercase_user_input += char
# print output
print(uppercase_user_input)