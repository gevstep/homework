# Task 1
user_string = input("Input text: ")
space = " "
print("User input sentence: ", space in user_string)
#Task 2
user_input = input("Input number: ")
user_input = int(user_input)
print("Inputed number divisible 5 and 11 is: ", user_input % 5 == 0 and user_input % 11 == 0)
#Task 3
year_input = input("Input year: ")
year_input = int(year_input)
print("Year is leap: ", year_input % 4 == 0 or year_input % 100 == 0)



