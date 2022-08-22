import socket

host_name = socket.gethostname()
IP_addres = socket.gethostbyname(host_name)
print("Host IP Address is:" + IP_addres)