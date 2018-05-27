# Pig Latin - Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant sound is transposed 
# to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).

string = ""

vowels = ["a", "e", "i", "o", "u", "y"]

while string != "quit":
	string = input("Type in a word. You can type \"quit\" to stop the loop.\n")

	# If the string begins with a vowel, we just add "ay"
	if string[0] in vowels:
		print(string + "ay")

	# If the string begins with consonants, we move the first group of consonants to the end and add "ay"
	else:
		index_of_first_vowel = 0

		for index, char in enumerate(string):
			if char in vowels:
				index_of_first_vowel = index
				break

		first_consonants = string[:index_of_first_vowel]

		rest_of_string = string[index_of_first_vowel:]

		print(rest_of_string + first_consonants + "ay")
