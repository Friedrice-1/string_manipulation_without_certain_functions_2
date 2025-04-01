# ask user to input a statement
user_input = input("Please enter a statement: ")
# find the last non space character
index = len(user_input) - 1
while index >= len(user_input) and user_input[index] == ' ':
    index -= 1
# create the new string without the spaces at the right side
user_input = user_input[:index+1]
# print output
print("Statement without spaces at the end")
print(f"'{user_input}'")