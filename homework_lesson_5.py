#Task 1
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_age = int(user_age)
print(user_name,"to 100 years left", 100 - user_age,"years: ")
#Task 2
first_input = input("Enter first number: ")
second_input = input("Enter second number: ")
third_input = input("Enter third number: ")
first_input = int(first_input)
second_input = int(second_input)
third_input = int(third_input)
print("Are entered numbers equal: ", first_input == second_input and first_input == third_input)
print("Are two numbers equal: ", first_input == second_input or first_input == third_input or second_input ==third_input)
#Task 3
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
first_number = int(first_number)
second_number = int(second_number)
print("Entered number is greater 5: ", first_number + second_number > 5)
print("Entered number is less 5: ", first_number + second_number < 5)
print("Entered number is less 5: ", first_number + second_number == 5)
#Task 4
user_mark = input("Enter your mark: ")
user_mark = int(user_mark)
print("You pass exam: ", user_mark > 35)