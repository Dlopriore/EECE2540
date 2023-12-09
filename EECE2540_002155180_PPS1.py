import math
import csv

"""
Please fill in the functions below
- DO NOT change the function signatures
- Be sure that you have the correct return type listed in the assignment
"""


# Author: Dante LoPriore

# to represent the packet class
class PacketClass:

	# constructor
	def __init__(self, packet_t):
		#add initialization code here 
		self.packet_id = packet_t[0]
		self.destination = packet_t[1]
		self.source = packet_t[2]
		self.data = packet_t[3]
		self.parity_bit = packet_t[4]
		self.ParityValid = -1
    
	# to check the recieved parity of a given packet was correct
	def check_parity(self, data, rcvd_parity):
		num_ones_count = data.count('1') # to check the amount of ones in the data string 

		# to determine the count of ones in string will lead to the Parity being Valid
		if (((num_ones_count % 2 == 0) and (rcvd_parity == '0'))): 
			self.ParityValid = True # true if even or odd
		else:
			self.ParityValid = False 

    # to display the parse packet's parity check and recieved packet number from a specific node.
	def parsed_packet(self):
		return f'Recieved Packet Number {self.packet_id} from node {self.source}. Parity Check returns {self.ParityValid}'

# String -> String
# to determine whether an input is a string and 
# output reverse of the string based on the given string input
def problem_one(string_to_be_reversed):
	if isinstance(string_to_be_reversed, str): # checks if input is a string 
		return string_to_be_reversed[::-1] # reverses the string
	else:
		return None


# Int List -> bool
# to check if the numbers and data in the list are integers in the list 
# to determine whether a given number is seen in the given list
def problem_two(number_to_find, list_to_check):
	for item in list_to_check:
		if not(isinstance(item, int)):  # check if the items in the list are numbers
			return None

	if (isinstance(number_to_find, int)): # check if the given number inputed is a number
		for item in list_to_check:
			if(number_to_find == item): # iterating through the whole list to see if the number is there
				return True
		return False
	return None


# Int -> Int
# to determine if the given integer is positive and
# to output the calculation the sum of the given integer from n to 0
def problem_three(integer_to_sum_to):
	sum = 0
	if (not(isinstance(integer_to_sum_to, int))): # check if the given number inputed is a number
		return None
	
	if ((integer_to_sum_to <= 0)): # check if the given number is positive
		return None
	
	for i in range(integer_to_sum_to+1): # perform the summation of every number from n to 0
		sum += i # adds each number to the sum 
	return sum


# List List -> List
# to concatenate two given lists with no duplicate data
def problem_four(left_list, right_list):
	if((not isinstance(left_list, list)) | (not isinstance(right_list, list))): # to check if the lists are lists
		return None
	
	concatlist = left_list + right_list # to combine the two lists
	nodupset = set(concatlist) # to check for no duplicates
	noduplicatelist = list(nodupset) # put back into a list
	return noduplicatelist
	

# Int -> Int
# to compute the area of the circle based on the given radius input
def problem_five(radius):
	if (not isinstance(radius, (int, float))): # to determine if it is a valid input
		return None
	
	if (radius < 0): # to determine if the number is positive
		return None
	
	circle_area = math.pi*(radius*radius) # formula for area of the circle
	format_circle_area = "{:.8f}".format(circle_area) # to format the area by the number of digits

	return format_circle_area

# CSV file -> List of a list of integers
# to produce a matrix based on the given inputs seen in the csv file.
# Recieved Help from Sara to understand syntax on how to open, read, write files in python.
def problem_six(filename):
	matrix_form = []
	try:
		with open(f'{filename}.csv', 'r') as cur_file: # open the given csv file
			for row in csv.reader(cur_file): # goes through each row of matrix seen in csv file 
				matrix_row = [item for item in row] # adds each item into row 
				matrix_form.append(matrix_row) # add each row in new matrix
			return matrix_form
	except FileNotFoundError: 
		return None #throws an error if the file is not compatable


# Str - > Str
# to produce the correct ascii table string result from the given hexadecimal value as a string
def problem_seven(hex_string):

	# checks to see if the type of the given hexadecimal string is a string
	if not isinstance(hex_string, str):
		return None
	
	# to determine if the length of the hex string is odd 
	# as no string literal can be produced if the hexadecimal input has a odd length
	out_string_literal = ""
	if (len(hex_string) % 2 == 1):
		return None
	
	# to initialize a list of splitting the hexadecimal string into the pairs of the two hex characters. Example ["1A", "2B"]
	# the purpose to split up the characters used to help the process for their conevrsion as a string literal
	list_hexadecimal_character_pairs = [hex_string[index: index+2] for index in range(0, len(hex_string), 2)]
	
	# iterate through the pairs of the hexadecimal character pairs
	for given_char in list_hexadecimal_character_pairs:
		decimal_form = int(given_char, 16) # covert the hexadecimal to decimal
		character_from_ascii_table = chr(decimal_form) # convert the decimal to a string literal charcter seen using the ascii table
		out_string_literal += character_from_ascii_table # add the string literal charcter to the output string.
	
	return  out_string_literal # the conversion from hexadecimal to a string literal


# Matrix of Integers -> Matrix of Integers, where matrix means list of a list
# to double the last number in each row of a 2-dimensional array of numbers
def problem_eight(list_of_lists):

	# to determine whether the given input is a list of a list
	if (not isinstance(list_of_lists, list)):
		return None
	
	# iterate through each row to determine if the row input is a valid list
	for given_row in list_of_lists:
		if (not isinstance(given_row, list)):
			return None
		
		# iterate through each item in the row to determine if the input is a int or float
		for item in given_row:
			if (not isinstance(item, (float, int))):
				return None
	
	# iterate through each row and double the last item in the row
	for given_row in list_of_lists:
		if (len(given_row) > 0):
			given_row[-1] *= 2
	
	return list_of_lists # output the changed matrix with the final number in each row doubled


# List of Strings -> List of Strings
# to produce a list of unique domain and extensions 
# based on the given list of email addresses
def problem_nine(list_of_email_addresses):

	if not isinstance(list_of_email_addresses, list): # checks if the list of emails is a list
		return None
	
	for item in list_of_email_addresses: # checks if the items in the list of emails are strings
		if not isinstance(item, str):
			return None
		
	# initalize a variable for the unique domains
	unique_domains = set() 

	# initailize placeholders for domain and extensions
	domain = ''
	extensions = ''

	# iterates through email list and splits the string into 2 based on the placement of the character '@'
	for email in list_of_email_addresses:
		email_components = email.split('@') 
		if (len(email_components) == 2):
			domain, extensions = email_components[1].split('.') # splits the domain and extension from the '.'
		unique_domains.add(f'{domain}.{extensions}') # adds new domain to the non-duplicate list 
	return list(unique_domains) # returns new list of email domain that are not duplicate

# Tuple -> String		
# to process a packet given the tuple input 
# to output the characteristics that make up the packet.
def problem_ten(packet_t):
	# to create a packet class given the inputs
	pkt_o = PacketClass(packet_t)

	# check recieved parity was correct
	pkt_o.check_parity(pkt_o.data, pkt_o.parity_bit)

	return pkt_o.parsed_packet()



# Program entry point.
if __name__ == '__main__':

	print("-------------------------------------")
	print("Problem #1")
	print("-------------------------------------")
	# Problem #1 Tests
	print(problem_one("Hello World!")) # Output - "!dlroW olleH"
	print(problem_one("ecin")) # Output - "nice"
	print(problem_one(0)) # Output - None
	print()

	print("-------------------------------------")
	print("Problem #2")
	print("-------------------------------------")
	# Problem #2 Tests
	print(problem_two(8, [1, 2, 3, 4, 5])) # Output - False
	print(problem_two(1, [1, 2, 2])) # Output - True
	print(problem_two(2, [1, 2, 2])) # Output - True
	print(problem_two(7, ["word", "salad"])) # Output - None
	print(problem_two("based", [9, 90])) # Output - None
	print()


	print("-------------------------------------")
	print("Problem #3")
	print("-------------------------------------")
	# Problem #3 Tests
	print(problem_three(6)) # Output - 21
	print(problem_three(4)) # Output - 10
	print(problem_three(0)) # Output - None
	print(problem_three(-2)) # Output - None
	print(problem_three('Abcd')) # Output - None
	print()

	print("-------------------------------------")
	print("Problem #4")
	print("-------------------------------------")
	# Problem #4 Tests
	print(problem_four([1, 2, 3], [2, 3, 4])) # Output - [1, 2, 3, 4]
	print(problem_four([], [23, 34])) # Output - [23, 34]
	print(problem_four(432, [9, 23])) # Output - None
	print(problem_four(['a', 'b', 'c'], ['a', 'b', 'c'])) # Output - ['b', 'c', 'a']
	print(problem_four(['a', 'b', 'c', 1], ['a', 'b', 'c', 2])) # Output - [1, 2, 'a', 'b', 'c']
	print()


	print("-------------------------------------")
	print("Problem #5")
	print("-------------------------------------")
	# Problem #5 Tests
	print(problem_five(0)) # Output - 0.00000000
	print(problem_five(3)) # Output - 28.27433388
	print(problem_five(3.0)) # Output - 28.27433388
	print(problem_five(-4)) # Output - None
	print(problem_five('A')) # Output - None
	print()

	print("-------------------------------------")
	print("Problem #6")
	print("-------------------------------------")
	# Problem #6 Tests
	given_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #define a matrix
	given_matrix_rand = [['a', 2, 'c'], [4, 'f', 6], [7, 'd', 9]] #define a matrix
	# Specify the filename for your CSV file
	known_file_name = "matrix.csv"
	known_file_name_rand = "matrix_rand.csv"
	
	# to write a matrix into the CSV file
	with open(known_file_name, 'w', newline='') as csvfile:
		matrix_csv = csv.writer(csvfile)
		matrix_csv.writerows(given_matrix) # write each row of the matrix onto the file

	with open(known_file_name_rand, 'w', newline='') as csvfile:
		matrix_csv = csv.writer(csvfile)
		matrix_csv.writerows(given_matrix_rand) # write each row of the matrix onto the file

	print(problem_six(0)) # Output - None
	print(problem_six("matrix")) # Output - [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(problem_six("matrix_rand")) # Output = ['a', '2', 'c'], ['4', 'f', '6'], ['7', 'd', '9']]
	print()
	
	print("-------------------------------------")
	print("Problem #7")
	print("-------------------------------------")
	# Problem #7 Tests
	print(problem_seven("48656c6c6f20576f726c6421")) # Output - 'Hello World'
	print(problem_seven("66756e64696573")) # Output - 'fundies'
	print(problem_seven("66756e6469657")) # Output - None
	print(problem_seven("")) # Output - " "
	print(problem_seven(45678)) # Output - None
	print()

	print("-------------------------------------")
	print("Problem #8")
	print("-------------------------------------")
	# Problem #8 Tests
	print(problem_eight([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output - [[1, 2, 6], [4, 5, 12], [7, 8, 18]]
	print(problem_eight([['a', 2, 3], [4, 5, 6], [7, 8, 9]])) # Output - None
	print(problem_eight(['mia', [4, 5, 6], [7, 8, 9]])) # Output - None
	print(problem_eight([[1, 6], [7, 9]])) # Output - [[1, 12], [7, 18]]
	print(problem_eight([[], [7, 9]]))  # Output - [[], [7, 18]]
	print()

	print("-------------------------------------")
	print("Problem #9")
	print("-------------------------------------")
	# Problem #9 Tests
	print(problem_nine(['cats@gmail.com', 'Hello World!', 'dogs@gmail.com', 'cows@yahoo.com'])) # Output - ['gmail.com', 'yahoo.com']
	print(problem_nine([])) # Output - []
	print(problem_nine([5432, 'Hello World!', 'dogs@gmail.com', 'cows@yahoo.com']))  # Output - None
	print()

	print("-------------------------------------")
	print("Problem #10")
	print("-------------------------------------")
	# Problem #10 Tests
	print(problem_ten(('2','10', '5', '01100101011000101011001001110110', '1'))) # Output - "Recieved Packet Number 2 from node 5. Parity Check returns False"
	print(problem_ten(('2','10', '5', '01100101011000101011001001110110', '0'))) # Output - "Recieved Packet Number 2 from node 5. Parity Check returns True"
	print(problem_ten(('2','10', '5', '0', '0'))) # "Output - "Recieved Packet Number 2 from node 5. Parity Check returns True"
	print(problem_ten(('2','10', '5', '0', '1'))) # "Output - "Recieved Packet Number 2 from node 5. Parity Check returns False"
	print(problem_ten(('3','21', '4', '11011', '0'))) # "Output - "Recieved Packet Number 3 from node 4. Parity Check returns True"
	print(problem_ten(('0','6', '2', '001', '1'))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns False"
	print(problem_ten(('0','6', '2', '001', '0'))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns False"
	print(problem_ten(('0','6', '2', '11', '1'))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns False"
	print(problem_ten(('0','6', '2', '11', '0'))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns True"
	print(problem_ten(('0','6', '2', '11', '2'))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns False"
	print(problem_ten(('0','6', '2', '11', ''))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns False"
	print(problem_ten(('0','6', '2', ' ', '0'))) # "Output - "Recieved Packet Number 0 from node 2. Parity Check returns False"
	print()