
# Author: Dante LoPriore
# Date: November 15, 2023
# NUID: 002155180
# Fundamentals of Networks Final Project

'''
									Read Me File:

Introduction and General Purpose of the Project:

      - The primary objective of this project and program was to demonstrate my understanding of the communication protocols seen within a client-server application architecture. 
	 	- I was tasked to implement the communication protocols on the network's client side that were compatible with the existing server's specifications. 
		- The project emphasized my applying my knowledge upon the fundamentals of networks to establish the client-server communication.
	- The overall goal of this project was to establish secure and efficient communication between the client application and the remote server. 
		- I was able to confirm and validate the functionality of the client-side implementation within the established network architecture by finding 
		  a secret flag output, which is a hexdecimal string, that signifys the end of the communication session

Brief Overview of the Application Layer Protocol Within the Client-Server Communication:

	Application and Application Layer Protocol Overview:
		- In client-server communication, the application layer protocol defines the standards and conventions for reliable data exchange 
		between the client and server applications.
		- In this sceanario, the application consists of the remote evaluation of simple arithmetical expressions such as: '+', '-', '*', and '/'
		- After the initial message sent by the client to establish the client-server communication,  the server asks the client to evaluate an 
		unspecified number of expressions consecutively. Each expression is sent as a separate message from the server to the client.
	
      Client's Requirements and Responbilities:
            - to start the initial connection to the server by sending an initial greeting message to the server.
            - to recieve the arithmetic expressions that was sent by the server, and then, evaluate each expression and respond to the server with the computed result.
            - to ask the server to send a unique secret flag to the client after sucessfully evaluating all the expressions.
            - to get and recieve the unique secret flag to the client

      Client's Interaction With the Server
            - to send arithmetic expressions to the client for the client to evaluate, 
                  - Then, the server expects response messages with the results from the client
            - to send the unique flag to the client if it's confirmed all expressions were properly evaluated 
            and connection between the client-server was sucessfully completed
            - to close the communication session when a result is reached.

Client Program Structure and Procedure:

      1) Initiate Communiciation with the Server:
            - The client setup a TCP connection with the server
                  - A TCP connection ensures a reliable data transfer within a network that is connection-oriented, congestion control, and ordered segments.
            - I created a client socket that allows data packets to be sent and recieved.
            - Then, the client would send the inital message to the server, where the server should respond with an expression message.
                  - Uses Format: 'EECE2540 INTR 002155180'

      2) Evaluate the Expression and Send Results to the Server
            - The server would send a expression to the client to be evaluated
                  - Uses Format: 'EECE2540 EXPR expression'
            - I would extract the expression to preform the desired math operation on the two given values
                  - Then, I would send the results of that math expression to the server to be further processed
                  - Uses Format: 'EECE2540 RSLT result'
      
      3) Recieve Feedback from the Server Reviewing the Results
            - the program would determine to continue the communication with the server
              based on the server's feedback from the client's calculated results.
            
            Results that Can Occure
                  (Case 1) Failure Message - the expression was evaluated incorrectly
                        - Uses Format: 'EECE2540 FAIL'
                         - then the communication would terminate
                  (Case 2) Success Message - application sucessfully evaluated all expressions
                        - Uses Format: 'EECE2540 SUCC flag'
                        - the communciate between the client and the server was sucessful, and ends program
                  (Case 3) Invalid Input Message
                        - Invokes an error
                  (Case 4) Continue Communication with the Server
                        - This occurs when the server wants the client to compute more expressions needed to be correctly solved.

      4) Close Communication Connection with the Server
            - Close the client socket and terminate program.

Testing:
      Checking Creation of Client Socket Was Sucessful: 
            - I was able to make sure that the client-side of the program was fully operationallly 
            by first seeing if the client socket was properly created and it could start communiciations with the server.
            - The test would work if the client-server communication was established 
            - The test would not work if the socket of the client was not properly initialized to connect to the server.

      Checking if the Client-Server Communication was Sucessful:
            - I was able to check this requirement through sending a message to the server and see how the server would 
            interpt the message to send the feedback to the client 
                  - I did this by preparing the intial message to start communications with the server 'EECE2540 INTR 002155180'
                  - Then, sending the initial message to the server. Then, I see if the client recieved the feedback from the Server "EECE2540 EXPR"
            - The test would work if the server and client properly communicate with each other.
            - The test would work not work if the program throws an outbounds error.

      Checking Multiple Expressions:
            - I was able to check multiple expressions from the message comming from the server by checking multiple cases, 
            which include if the expression was invalid, successful, failed, and countinue communcation with the server.
                  - This was possible by using a while loop to check each any possible cases based on a given expression over time
            - The test would work if the communication was successful and outputed the secret flag
            - The test would not work if the communicstion failed or invalid result and input.
      
      Checking Closing the Client-Socket Work
            - I was able to test if the client-socket properly closed the communication ended between the client and server.
            - The test would work if the program stops running sucessfully
            - The test would not work if the program crashes or goes into an infinite loop.

Final Results:
      - Here are the final results using the northeastern remote server
      
      Secret Flag: a16b245955dfdd886d4352f60813ee82fec4e3e64b27e144ae5d374e42af6776

'''

# to display that the program has started for the client
print('Client program started.')


### Imports --------------------------------------------------
import hashlib
import random
# Import socket package.
import socket 
import sys


### Constants --------------------------------------------------

# initalize the variable for the remote sever using northeastern IP address 
server_hostname = '129.10.131.26'

# initalize server port number
default_server_port = 12007

# initalize the client/server link
buffer_size = 4096

secret_key = "This sample key is secret".encode()
server_identifier = (server_hostname, default_server_port)

print( 'Client socket created.' )
### Functions --------------------------------------------------

# function to run client connection
def run_client():
    '''Set up client sockets and handle incoming communications.'''
    # Create client socket.
    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    # Connect client socket.
    client_socket.connect(server_identifier)
    print('Client socket connected.')
     
    # to prepare the intial message to start communications with the server
    introductory_message_to_server = 'EECE2540 INTR 002155180'

    # Convert input string to message.
    message_to_server = introductory_message_to_server.encode()

    # Send client's initailize message to server to establish a connection
    client_socket.send(message_to_server)
    print('Client sent message to server')


    # Start communication loop.
    while True:
           
          # Receive message from server.
          expression_message_from_server = client_socket.recv(buffer_size)
          print('Client received message from server')

          # Convert message to string.
          expression_from_server = expression_message_from_server.decode()

          # to check if the expression from the sever is a expr
          if(expression_from_server.startswith("EECE2540 EXPR")):
                
                # allow user to see arithmatic operation being preformed 
                print(expression_from_server)

                # to recieve the message from the sever to compute and solve
                list_expression = expression_from_server.split(" ")[2:5]
                expression = " ".join(list_expression)
                
                # to convert input string to message.
                exp_result = eval(expression)
                str_result_expression = str(exp_result)

                # to prepare the result message to be sent to the server
                result_message_to_server = 'EECE2540 RSLT ' + str_result_expression
                rslt_message_to_server = result_message_to_server.encode()

                # to send client's result message to server.
                client_socket.send(rslt_message_to_server)
                print(f'Sent Result Message')

          # to check if the expression from the sevrer is successful
          elif(expression_from_server.startswith("EECE2540 SUCC")):
                # Receive secret flag message from server.
                secret_flag_message_from_server = expression_from_server.split(" ")[2]
                print(f'Secret Flag: {secret_flag_message_from_server}')
                break
          
          # to check if the expression from the sever is failed
          elif(expression_from_server.startswith("EECE2540 FAIL")):
                print("Recieved a FAIL message from the server")
                break
          else:
                print("Error: Invalid input from the server")
                break


    # Close the client socket.
    client_socket.close()
    print('Client socket closed.')
    print('Client program terminated.')


### Program entry point  --------------------------------------------------
if __name__ == '__main__':
    run_client()