# Task 1
my_list = ["aba", 'acc', 'zxz', '1221', 'aavvaa']
list_for_print = []
for i in my_list:
	element = i
	if element[0] == element[-1]:
		list_for_print.append(element)

print(len(list_for_print))
# Task 2
my_list = []
if len(my_list) == 0:
	print("List is empty: ")
else:
	print("List is not empty: ", my_list)
# Task 3
my_list = ['asd', 'asdasd', 'asdas','asdasdasdasd']
length_of_elements = []
for i in my_list:
	element = i
	length_of_elements.append(len(element))
	index_of_max_list = length_of_elements.index(max(length_of_elements))

print(my_list[index_of_max_list])
# Task 4
list_one = ['asd', '123', 'Gevorg', 'Stepanyan']
list_two = ['qwe', '456', 'Armen', 'asdasd']
common_list = []
def common_element(list_one, list_two, common_list):

		for i in list_one:
			for j in list_two:
				if i == j:
					common_list.append(i)
		if len(common_list) > 0:
			return True, common_list
		else:
			return False, common_list
						
	


print(common_element(list_one, list_two, common_list))

