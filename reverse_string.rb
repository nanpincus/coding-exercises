# Reverse a String three different ways - Enter a string and the program will reverse it and print it out.

# Use the built-in method call
def reverse1(word)
	word.reverse
end

# Iterate over each character, prepending as we go
def reverse2(word)
	reversedWord = ""

	word.split("").each do |i|
		reversedWord = reversedWord.prepend(i)
	end

	reversedWord
end

# Iterate by word instead of by letter
def reverse3(sentence)
	reversedSentence = ""

	sentence.split(" ").each do |i|
		reversedSentence = reversedSentence.prepend(i + " ")
	end

	reversedSentence
end


puts "Type a string!"
user_input = gets.chomp
puts reverse2(user_input)

puts "Type another string!"
user_input = gets.chomp
puts reverse2(user_input)

puts "Now type a sentence!"
user_input = gets.chomp
puts reverse3(user_input)

puts "You're done!"