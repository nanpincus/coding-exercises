# Given a sentence (or sentences) from user input, print a histogram showing the frequency of words in the text.

puts "Type in the sentence that you want a histogram of."

text = gets.chomp

# Remove all non-alphabetical characters
# [^ - Not matching..
# a-z] all lowercase alphabetical characters
words = text.split(" ").each { |word| word.gsub(/[^a-z]/, "")}

frequencies = Hash.new(0)

words.each { |word| frequencies[word] += 1 }

frequencies = frequencies.sort_by {|a, b| b }

frequencies.reverse!

frequencies.each { |word, frequency| puts word + " " + frequency.to_s }
