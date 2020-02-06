# Task 1 version 1
user_input = input("Enter a text: ")
x = user_input[0]
y = user_input[1:len(user_input)]
print(x, y.replace(x, "$"))
# Task 2
user_input = input("Enter a word: ")
x = "ing"
y = "ly"
if len(user_input) < 3:
	print(user_input)
elif len(user_input) > 2 and user_input.endswith("ing"):
	print(user_input + y)
elif len(user_input) > 2:
	user_input.split()
	print(user_input + x)
# Task 3 version 1
my_string = input("Enter a sentence: ")
x =  my_string.find("not")
y = "good!"
if "not" in my_string and my_string.endswith("poor"):
	print(my_string[0: x] + y)
	
# Task 3 version 2
my_string = input("Enter a sentence: ")
x =  my_string.find("not that poor")
y = my_string[0: x]
z = "good!"
print(y + z)





	

	



		


