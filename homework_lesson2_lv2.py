# Task 1
my_dictionary = {"name": "Gevorg", "surname": "Stepanyan"}
print(my_dictionary)
my_dictionary.update({"year": "1991"})
print(my_dictionary)
# Task 2 Tarapanq
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
final_dic = {}
for i, j in dic1.items():
	i = str(i)
	j = str(j)
	final_dic.setdefault(i,j)

for a,b in dic2.items():
	a = str(a)
	b = str(b)
	final_dic.setdefault(a,b)

for x,z in dic3.items():
	x = str(x)
	z = str(z)
	final_dic.setdefault(x,z)

print(final_dic)
# Task 3
my_dict = {"name": 'Poghos', "surname": 'Poghosyan'}

x = my_dict.get("model")
x = str(x)
if x == "None":
	print("There are not the key: ")
else:
	print(x)
#Task 4
user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
user_year = input("Enter your birth year: ")
my_dict = {"name": user_name, "surname": user_surname, "birth year": user_year}
print(my_dict)
# Task 5
my_dict = {1: 10, 2: 30, 3: 80}

my_list = []
for i in my_dict.values():
	my_list.append(i)

print("Maximum value in dictionary is: ", max(my_list))
print("Minimum value in dictionary is: ", min(my_list))
#Task 6
x = ('I', 'S', 'T', 'C')
y = 1

my_dict = dict.fromkeys(x,y)

print(my_dict)