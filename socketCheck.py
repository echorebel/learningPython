import socket
#TODO define constants
#s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
s = socket.socket(2, 1)

host = socket.gethostname()
target = socket.gethostbyname('sub.domain.tld')

print("host: ", host)
print("target:" + target)

s.bind((target,443))

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()                # Close the connection
