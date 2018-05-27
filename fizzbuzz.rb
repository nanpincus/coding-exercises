# Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number and 
# for the multiples of five print “Buzz”. For numbers which are multiples 
# of both three and five print “FizzBuzz”.

for i in 1..100
	if i % 3 == 0 && i % 5 == 0 then puts "FizzBuzz" 
	elsif i % 3 == 0 then puts "Fizz"
	elsif 1 % 5 == 0 then puts "Buzz"
	else puts i
	end
end