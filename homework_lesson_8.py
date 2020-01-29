# Task 1
first_input = int(input("Enter first number: "))
second_input = int(input("Enter second number: "))
third_input = int(input("Enter third number: "))
def number_bigger(first_input, second_input, third_input):
	if first_input > second_input and first_input > third_input:
		return "The biggest number is: ", first_input
	elif second_input > first_input and second_input > third_input:
		return "The biggest number is: ", second_input
	elif third_input > first_input and third_input > second_input:
		return "The biggest number is: ", third_input

print(number_bigger(first_input,second_input,third_input))
# Task 2
number_input  = int(input("Enter the number: "))
def fizz_buzz(number_input):
	if number_input % 3 == 0 and number_input % 5 == 0:
		return "FizzBuzz"
	elif number_input % 5 ==0:
		return "BUZZ"
	elif number_input % 3 == 0:
		return "Fizz"
	else:
		return number_input

print(fizz_buzz(number_input))

# Task 3
limit = int(input("Enter the limit: "))
def number_limit(limit):
	for i in range(0,limit):		
		if i % 2 == 0:
			print(i,"EVEN")
		else:
			print(i,"ODD")
				
			
number_limit(limit)
# Task 4
user_input = int(input("Enter a number: "))
def number_point(user_input):
	second = user_input * 11
	third = user_input * 111
	return user_input + second + third

print(number_point(user_input))

# Task 5
user_input = int(input("Enter a number: "))
def number_square_plus_one(user_input):
	x = user_input ** 2 +1
	return x

print(number_square_plus_one(user_input))