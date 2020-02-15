class Test:
	def __init__(self, first_number, second_number):
		self.first_number = first_number
		self.second_number = second_number

	def numbers_sum(self):
		x = self.first_number + self.second_number
		return  x

	def numbers_div(self):
		return self.first_number / self.second_number

numbers = Test(first_number = int(input("Enter a first number: ")), second_number = int(input("Enter a secnd number: ")))
print(Test.numbers_sum(numbers))
print(Test.numbers_div(numbers))
# f = open("test.txt", "w")
# f.write()
# f.close()