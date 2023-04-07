import socket
import time

class Server():
    def __init__(self, host="localhost", port=8080):
        self.HOST_NAME = host
        self.PORT = port
        self.connected = False
        self.have_sock = False


    def create_socket(self):
        # ipv4AF_INET  tcp/ip -> SOCK_STREAM
        #with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as self.sock :
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.HOST_NAME, self.PORT))
        self.sock.listen(1)
        self.have_sock = True
    
    def socket_accept(self):
        if self.have_sock:
            self.sock.settimeout(1) 
            try:
                if self.have_sock:
                    self.conn, self.addr = self.sock.accept()
                    print("accepted remote. remote_addr {}.".format(self.addr))
                    self.connected = True
            except:
                return

    def recv_data(self):
        if self.connected:
            return self.conn.recv(1024)

    def reconnect(self):
        self.clear_connection()
        print("trying reconnect to client, please wait")
        time.sleep(5)
        self.create_socket()
        self.socket_accept()

    def clear_connection(self):
        if self.connected:
            self.conn.close()
            self.sock.close()
        
        self.connected = False
        print("clear connection")

if __name__ == "__main__":
    server = Server()
    server.create_socket()
    server.socket_accept()
    try:
        while True:
            if not server.connected:
                server.reconnect()

            data = server.recv_data()
            print(data.decode())
            
            if data.decode() == "q":
                server.reconnect()

    except Exception as e:
        print("Error", e)
    
    except KeyboardInterrupt:
        print("ctl-C precced")

    finally:
        server.clear_connection()
