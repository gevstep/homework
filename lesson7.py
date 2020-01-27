# Task 1
user_input = int(input("Input a number: "))
i = 1
while i < 11:
	y = user_input * i
	print(user_input, "*", i,"=", y)
	i += 1
# Task 2 
s = "*"
for i in range(0,6):
	x = i * s
	print(x)
for j in range(4,0, -1):
	y = j * s
	print(y)
# Task 3 
number_inputed = input("Enter number: ")
for i in range(0, int(number_inputed)):
	if   i % 2 !=0:		
		print(i)

	