# ask user to enter a statement
user_input = input("Enter a string: ")
# ask user to enter a character to find
find = input("Enter the character you want to find: ")
# find the first occurrence of the character
position = -1
for i in range(len(user_input)):
    if user_input[i] == find:
        position = i
        break
# print output
if position != -1:
    print(f"The first occurrence of '{find}' is at index {position}")
else:
    print(f"'{find}' not found in the string")