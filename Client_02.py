
# Implement the same/ similar client script with a
# different equation on formula for generating the numbers

import socket
# + poly[1]x(n-2) + .. + poly[n-1]
def horner(poly, n, x):

	# Initialize result
	result = poly[0]

	# Evaluate value of polynomial
	# using Horner's method
	for i in range(1, n):

		result = result*x + poly[i]

	return result

# Driver program to
# test above function.


# Let us evaluate value of
# 2x3 - 6x2 + 2x - 1 for x = 3
poly = [2, -6, 2, -1]
x = 3
n = len(poly)

print("Value of polynomial is:", horner(poly, n, x))


#better to use the wireless LAN adapter wifi IP
#this is your device ip address

HOST = '127.0.0.1'

PORT = 9090

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))

#data = input("Enter data that you want to send")
#client.send(data.encode('utf-8'))

client.send("Hello World\n".encode(('utf-8')))

# client.send("Hello World again\n".encode(('utf-8')))
# client.send("Hello World again and again\n".encode(('utf-8')))
# client.send("Hello World again and again and again\n".encode(('utf-8')))



#print whatever you receive form the server
received_message = client.recv(1024).decode('utf-8')
print(received_message)

received_message = client.recv(1024).decode('utf-8')
print(received_message)
list = received_message.split(" ")
print(list)


generated_seed = horner(poly, n, x)
print(f"This is the generated seed: {generated_seed}")
client.send(f"{generated_seed}\n".encode(('utf-8')))



