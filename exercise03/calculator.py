import arithmetic

def calculator(input):

	token = input.split(" ")

	if token[0] == "+":
		print arithmetic.add(int(token[1]), int(token[2]))

	if token[0] == "-":
		print arithmetic.subtract(int(token[1]), int(token[2]))

	if token[0] == "*":
		print arithmetic.multiply(int(token[1]), int(token[2]))

	if token[0] == "/":
		print arithmetic.divide(int(token[1]), int(token[2]))

	if token[0] == "square":
		print arithmetic.square(int(token[1]), int(token[2]))

	if token[0] == "cube":
		print arithmetic.cube(int(token[1]), int(token[2]))

	if token[0] == "power":
		print arithmetic.power(int(token[1]), int(token[2]))

	if token[0] == "mod":
		print arithmetic.mod(int(token[1]), int(token[2]))

print "{+, -, *, /, square, cube, power, mod} a b"
print "q to quit"

while True:
	
	input = raw_input('> ')

	if input == 'q':
		break
	else:
		calculator(input)