import socket 
import threading 
import select 
HEADER = 64 
CODE = 'utf-8' 
def create_server(): 
    PORT = 55555 
    IP = socket.gethostbyname(socket.gethostname()) 
    ADDR = (IP, PORT)
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) 
    server_socket.bind(ADDR) 
    return server_socket 
def handle_client(conn, addr, conv, func): 
    global HEADER 
    global CODE 
    import time 
    now = time.time() 
    TIME_OUT = 120 
    conv = conv() 
    while time.time() <= now + TIME_OUT: 
        msg_len = conn.recv(HEADER).decode(CODE) 
        if msg_len: 
            msg = conn.recv(int(msg_len)).decode(CODE) 
            responce, conv = func(conv, msg) 
            responce = responce.encode(CODE) 
            resp_len = len(responce) 
            send_len = str(resp_len).encode(CODE) 
            send_len += b' ' * (HEADER - len(send_len)) 
            conn.send(send_len) 
            conn.send(responce) 
            now = time.time() 
    conn.close() 
    active_connections = threading.active_count() - 2 
    print(f'[CONNECTIN {addr} TERMINATED, ACTIVE CONNECTIONS: {active_connections}]') 
def start_server(server, conv, func): 
    server.listen() 
    print('[SERVER STARTED SUCCESSFULY]') 
    while True: 
        conn, addr = server.accept() 
        thread = threading.Thread(target=handle_client, args=(conn, addr, conv, func)) 
        thread.start() 
        active_connections = threading.active_count() - 1 
        print(f'[NEW CONNECTION: {addr} CONNECTED , ACTIVE CONNECTIONS: {active_connections}]') 
if __name__== '__main__': 
    pass