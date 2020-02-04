sentence = input("Enter a sentence: ")


def words_count(sentence):
	count = 0
	for i in range(0, len(sentence)):
		if sentence[i] == " ":
			count += 1
	print("You enter", count + 1, "words: ")

	
words_count(sentence)

