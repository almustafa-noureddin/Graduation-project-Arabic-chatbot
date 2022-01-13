import socket 
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 55555 
ADDR = (IP, PORT) 
HEADER = 64 
CODE = 'utf-8' 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connect(): 
    try:
        client.connect(ADDR) 
    except: 
        return None 
    return True 
def send(msg): 
    encoded_msg = msg.encode(CODE) 
    len_msg = len(encoded_msg) 
    send_msg = str(len_msg).encode(CODE) 
    send_msg += b' '*(HEADER - len(send_msg)) 
    client.send(send_msg) 
    client.send(encoded_msg) 
def recv(): 
    header = client.recv(HEADER).decode(CODE) 
    len_msg = int(header) 
    msg = client.recv(len_msg).decode(CODE) 
    return msg