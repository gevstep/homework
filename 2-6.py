# Task 1
class ListElementsSum:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def list_elements_sum(self):
        elements_sum = []
        for k in numbers:
            for j in numbers:
                if k + j == target and numbers.index(k) and k != j:
                    elements_sum.append(numbers.index(k))
                    elements_sum.append(numbers.index(j))
                    print(elements_sum)
                    break



def inputed_instance():
    global numbers, list_count, target
    list_count = int(input("Enter how many elements you want input: "))
    target = int(input("Enter a target number: "))
    numbers = []
    i = 0
    while i < list_count:
        list_element = int(input("Enter the list element: "))
        numbers.append(list_element)
        i += 1



ListElementsSum.list_elements_sum(inputed_instance())
# Task 2
class MyClass:
    def __init__ (self, class_name):
        self.class_name = class_name

    def __name__ ():
        return __name__
    

print(MyClass.__name__)
# Task 3
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)

print(Point3D.__repr__(my_point))

