# ask user to input a statement
user_input = input("Please enter an input: ")
# ask user to check what the statement starts with
starts_with = input("Enter to check if the statements starts with it: ")
# checks if it starts with the input entered
if starts_with == user_input[:len(starts_with)]:
# print result
    print(f"It starts with {starts_with}")
else:
# print result
    print(f"It does not starts with {starts_with}")