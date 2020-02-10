# Task 1
user_input = int(input("Enter a number: "))
if user_input in range(0,100):
	print("Your number is in range: ")
else:
	print("Your number is not in range: ")
# Task 2
user_input = input("Enter a text: ")
low_letter_count = 0
upper_letter_count = 0

for i in user_input:
	if i.isupper() == True:
		upper_letter_count += 1
		
print("Upper letters count: ", upper_letter_count)

for j in user_input:
	if j.islower() == True:
		low_letter_count += 1

print("Low letters count: ", low_letter_count)
# Task 3
my_list = [1, 4, 7, 'a', 'aa', 'zz', 1, 'aa']
uniqe_list = []
count = 0
for i in my_list:
	if my_list.count(i) < 2 :
		uniqe_list.append(i)
		

print(uniqe_list)

# Task 4
user_number = int(input("Enter a number: "))
if user_number % 2 == 0 or user_number % 3 == 0:
	print("Your number is not prime: ")
else:
	print("Your number prime: ")

