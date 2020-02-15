# Task 1
class StringPrint:
    def __init__(self, user_sentence):
        self.user_sentence = user_sentence

    def get_string(self):
        return self.user_sentence
    def print_string(self):
        return self.user_sentence.upper()
sentence = StringPrint(input("Enter the sentence: "))

print(StringPrint.print_string(sentence))

# Task 2
class Vehicle:
    def __init__(self, name, color, cost):
        self.name = name
        self.color = color
        self.cost = cost
    def car_info(self):
        return self.name +" "+ self.color +" " + str(self.cost)

car1 = Vehicle("Fer", "red", 60000)
car2 = Vehicle("Jump", "blue", 10000)

print(Vehicle.car_info(car1))
