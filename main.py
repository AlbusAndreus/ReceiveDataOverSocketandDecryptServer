import socket
from cryptography.fernet import Fernet

def loadKey():
    file = open("C:\\Users\\Aleka\\OneDrive\\Desktop\\KeyFile.key")
    key = file.read()
    return key


sock = socket.socket()
sock.bind(("localhost", 65000))
sock.listen(2)

conn, address = sock.accept()
key = loadKey()
fernet = Fernet(key)

message = conn.recv(1024)

print(fernet.decrypt(message.decode()).decode())

