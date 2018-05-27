# Fibonacci Sequence - Enter a number and have the program find the Nth Fibonacci number using three different methods,
# and compare the time it took for each.

import time
import math

def fibonacciToNthIterative(nth):

	index = 0
	fib_sequence = []

	previous_value = 1
	current_value = 1

	while index < int(nth):
		
		if index == 0:
			fib_sequence.append(0)
		elif index == 1:
			fib_sequence.append(1)
		else:
			temp = current_value
			current_value = current_value + previous_value
			previous_value = temp

			fib_sequence.append(current_value)
		index += 1

	return fib_sequence
	
def recursiveFibonacci(nth):
	if nth == 0:
		return 0
	elif nth == 1:
		return 1
	else:
		return (recursiveFibonacci(nth - 1) + recursiveFibonacci(nth - 2))

def fibonacciToNthRecursive(nth):
	fib_sequence = []

	for i in range(nth + 1):
		fib_sequence.append(recursiveFibonacci(i))

	return fib_sequence

def nth_fibonacci_iterative(nth):
	return fibonacciToNthIterative(nth)[-1]

def nth_fibonacci_recursive(nth):
	return fibonacciToNthRecursive(nth)[-1]

# Defined here: https://en.wikipedia.org/wiki/Golden_ratio
def golden_ratio():
	return (1 + math.sqrt(5)) / 2

# Binet's formula: Xn = (G^n - (1-G)^n) / sqrt(5) where Xn is the Nth number of the Fibonacci sequence and G is the golden ratio
# Source: https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
def nth_fibonacci_binet(nth):

	phi = golden_ratio()

	try:
		nth_value = (phi ** nth - (1 - phi) ** nth) / math.sqrt(5)

	except OverflowError:
		print("Whoops! The result was too big to calculate with Binet's formula!")
		return -1

	# Round the result as Binet's formula provides an approximation, and the Fibonacci sequence has only integers
	return round(nth_value)


input_string = ""

# Let the user terminate the loop with either "Quit", "quit" or "Quit!!"
while not input_string.lower().startswith("quit"):
	
	parsed_input = ""

	while not parsed_input:

		try:
			input_string = input("Type in a number N to find the Nth number of the Fibonacci sequence and see which method of calculation gets the fastest result. You can type \"Ctrl-D\" to quit.\n")
			parsed_input = int(input_string)

		except ValueError:
			print("We were looking for a number.")
			parsed_input = 0

	start = time.time()
	iterative_value = nth_fibonacci_iterative(parsed_input)
	end = time.time()
	iterative_technique_time_elapsed = (end - start)

	print("Using the iterative method, we got the number " + str(iterative_value) + " in " + str(iterative_technique_time_elapsed) + " seconds.")

	if parsed_input < 32:
		start = time.time()
		recursive_value = nth_fibonacci_recursive(parsed_input)
		end = time.time()
		recursive_technique_time_elapsed = (end - start)

		print("Using the recursive method, we got the number " + str(recursive_value) + " in " + str(recursive_technique_time_elapsed) + " seconds.")
	else:
		print("It'd probably take too long to get that number using the recursive strategy.")

	start = time.time()
	binet_value = nth_fibonacci_binet(parsed_input)
	end = time.time()
	binet_technique_time_elapsed = (end - start)

	if binet_value >= 0:
		print("Using the Binet's formula method, we got the number " + str(binet_value) + " in " + str(binet_technique_time_elapsed) + " seconds.")
