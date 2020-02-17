# Task 1
class SumOfThreeElements:
    def __init__(self, start_list):
        self.start_list = start_list
    def list_zero(self):
        empty_list1 = []
        empty_list2 = []
        empty_list3 = []
        empty_list = []
        for i in start_list:
            empty_list1.append(i)
            empty_list2.append(i)
            empty_list3.append(i)
        empty_list.append(empty_list1)
        empty_list.append(empty_list2)
        empty_list.append(empty_list3)
        my_list = []
        my_list1 = []
        my_list2 = []
        k = 0
        m = 0
        n = 0
        for k in empty_list1:
            for m in empty_list2:
                for n in empty_list3:
                    if k + m + n ==0:
                        my_list.append(k)
                        my_list.append(m)
                        my_list.append(n)
        p = 0
        q = 0
        for p in my_list:
            my_list1.append(p)
            if len(my_list1) == 3:
             break
        for q in my_list:
            my_list2.append(q)
            if len(my_list2) == 3:
             break
        final_list = []
        final_list.append(my_list1)
        final_list.append(my_list2)


        print(empty_list)
        print(my_list)
        print(my_list1)
        print(my_list2)
        print(final_list)



def start_list():
    global start_list
    start_list = [-25, -10, -7, -3, 2, 4, 8, 10]

SumOfThreeElements.list_zero(start_list())


# Task 2
class PowerNumber:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def number_to_power(self):
        y = pow(x, n )
        return y

def numbers_input():
    global  x, n
    x = int(input("Enter first number: "))
    n = int(input("Enter second number: "))

print(PowerNumber.number_to_power(numbers_input()))
# Task 3
class WordReverse:
    def __init__(self, sentence):
        self.sentence = sentence

    def revers_word_to_word(self):
        sentence_list = sentence.split()
        sentence_list.reverse()
        return str(sentence_list)

def input_sentence():
    global sentence
    sentence = input("Enter sentence: ")

print(WordReverse.revers_word_to_word(input_sentence()))
# Task 4
class StringPrint:
    def __init__(self, user_sentence):
        self.user_sentence = user_sentence

    def get_string(self):
        return self.user_sentence
    def print_string(self):
        return self.user_sentence.upper()
sentence = StringPrint(input("Enter the sentence: "))
# Task 5
class AreaRecangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area_of_recangle(self):
        A = width * length
        return  A

def input_width_and_length():
    global length, width
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))


print(AreaRecangle.area_of_recangle(input_width_and_length()))
