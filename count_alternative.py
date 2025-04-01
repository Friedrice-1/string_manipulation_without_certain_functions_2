# ask user to input a statement
user_input = input("Please enter a statement: ")
# ask user to input the character they want to count
find = input("Enter the character you want to count: ")
# count the characters
count = 0
for char in user_input:
    if find == char:
        count += 1
# print result
print(count)