# Task 1
my_list = [10, 20, 30, 40, 50]
list_for_print = []
for i in my_list[::-1]:
    list_for_print.append(i)
print(list_for_print)
# Task 2
input_number = int(input("Enter a number: "))
number_for_print = 100 - input_number
print(input_number,"--------",number_for_print)
# Task 3
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            print(a,b,c)