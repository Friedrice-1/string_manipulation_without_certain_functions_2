# ask user to input a statement
user_input = input("Please enter a statement: ")
# convert the statement into lowercase
lowercase_user_input = ""
for char in user_input:
    if 'A' <= char <= 'Z':
        lowercase_user_input += chr(ord(char) + 32)
    else:
        lowercase_user_input += char
# check if the statement is the same as the converted one
if user_input == lowercase_user_input:
# print result
    print("The statement is in lowercase")
else:
# print result
    print("The statement is not in lowercase")