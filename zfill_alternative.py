# ask user to enter a number
user_input = input("Enter a number: ")
# ask user to enter zeros to adjust
width = int(input("Enter the the number of zeros: "))
# adjust the statement based on the amount zeros entered
if len(user_input) < width:
    user_input = "0" * (width - len(user_input)) + user_input
# print output
print(user_input)