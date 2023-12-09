print( 'Server program started.' )

# Dante LoPriore
# October 30, 2023
# Computing Assignment #2

# Import socket package.
from socket import *

# Initialise important variables to represent the local host
address = 'localhost'
port_number = 12005
identifier = (address, port_number)

# Create and bind server socket.
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind( identifier )
print( 'Server socket created and bound at:' , identifier )

# to allow the server to accept and listen up to 5 client connections.
server_socket.listen(5)
print( 'Server socket is now listening for connections.' )

# iterate through the loop.
is_looping = True
while is_looping:

	# to allow a new connection to be accepted
	connection_socket, client_address = server_socket.accept()
	print( 'Server created connection socket for client at:' , client_address )
	
	# to get message from the client.
	message_from_client = connection_socket.recv( 2048 )
	print( 'Server received message from client at:' , client_address)

	# Convert message to string.
	given_string_message_from_client = message_from_client.decode()
	print('Received string:', given_string_message_from_client)

	# to determine if the message is a stop or kill command.
	if 'kill' == given_string_message_from_client.lower():
		
		# if the kill command is true then the program will stop.
		print('Kill command given!')

		# Modify string.
		out_string = 'Killed!'

		# End loop.
		is_looping = False

	else:
		
		# splits the string based on the "-" character seen in the application-layer message 
		split_str_list = given_string_message_from_client.split('-')
		
        #initialize the list of integers
		integer_list = []
		
        # iterate through the list 
        # to convert the type of the list's data from string to integer
		for item in split_str_list:
			integer_list.append(int(item))
		
        # to sum all the integer numbers in the list	
		sum_integers = sum(integer_list)
		
        # to convert the sum result from int to string
		out_string = f'RESULT:{sum_integers}'
		
	# to convert the modified output string to be sent message to the client
	message_to_client = out_string.encode()
	print('Sent string:' , out_string)

	# to send the message to the client
	connection_socket.send( message_to_client)
	print('Server sent message to client at:' , client_address)

	# to close the connection socket.
	connection_socket.close()
	print('Server closed connection socket for client at:' , client_address)

# to close the server socket.
server_socket.close()
print('Server socket closed.')

print('Server program terminated.')