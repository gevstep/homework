# Task 1
sentence = input("Enter a sentence: ")
def words_count(sentence):
	count = 0
	for i in range(0, len(sentence)):
		if sentence[i] == " ":
			count += 1
	print("You enter", count + 1, "words: ")

	
 words_count(sentence)

# Task 2
user_phone_number = input("Enter your phone number: ")
try:
	user_phone_number = int(user_phone_number)
	prefix = user_phone_number / 100000
	prefix = prefix // 10
	prefix = int(prefix)
	if prefix == 77 or prefix == 94 or prefix == 93 or prefix == 98:
		print("Your operator is vivacell")
	elif prefix == 91 or prefix == 96 or prefix == 99 or prefix == 43 or prefix == 33:
		print("Your operator is beeline")
	elif prefix == 55 or prefix == 41 or prefix == 95 or prefix == 44:
		print("Your operator is ucom")	
except TypeError:
	print("Please enter number: ")
except ValueError:
	print("Enter correct value")

# Task 3
user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
attempt = 0
for attempt in range(0, 5):
	try:
		print(user_surname, user_name)
	except TypeError:
		print("You entered a number: ")
else:
	print("You are a robot: ")






