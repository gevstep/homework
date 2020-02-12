# Task 1
f = open('new.txt', 'r')

words = []
for i in f:
	words.append(i)
	
print(words)
x = max(words)
for j in words:
	if j == x:
		print(j)




f.close()
# Task 2
f = open('new.txt', 'r')
count = 0
for i in f:
	count += 1

print(count)
	
	
f.close()
# Task 3
f = open('write.txt', 'w')
my_list = ['Gevorg', 'Stepanyan', True, 5, 10.8]
my_list = str(my_list)
f.write(my_list)

	
f.close()
# Task 4
f_read = open("new.txt", 'r')
f_write = open('file_for_read.txt', 'w')

x = f_read.read()
f_write.write(x)

f_read.close()
f_write.close()
# Task 5
user_number = int(input("Enter a number for check: "))
def is_number_in_range(user_number):
	if user_number in range(0, 100):
		print("Your number is in range:")
	else:
		print("Your number is not in range: ")

is_number_in_range(user_number)
