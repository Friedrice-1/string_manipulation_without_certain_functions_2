# ask user to input a word
user_input = input("Please enter a word: ")
# ask user for a suffix to remove
suffix = input("Enter a suffix to remove: ")
# remove suffix
if user_input.endswith(suffix):
    new_user_input = user_input[:-len(suffix)]
# print output
print(new_user_input)