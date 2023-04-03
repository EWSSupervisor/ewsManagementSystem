import socket
import time


class BRClient():
    def __init__(self):
        self.HOST_NAME = "localhost"
        self.PORT = 8080
        self.timer = 0
        self.first_flag = True
        self.timeout_sec = 100

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.HOST_NAME,self.PORT))

    def send_data(self):
        while True:
            data = input()
            self.sock.send(data.encode("utf-8"))
            if data == "q":
                break

    def close_sock(self):
        self.sock.close()

    def wait_server(self):
        while True:
            try:
                self.create_socket()
                print("After {} sec, connected to server.".format(self.timer))
                break

            except ConnectionRefusedError as e:
                if self.first_flag:
                    print("{}. Can't connect with Server.".format(e))
                    self.first_flag = False

                time.sleep(1)
                self.timer += 1

                if self.timer == self.timeout_sec:
                    print("ERROR TimeOut")
                    self.close_sock()
                    exit()

    def recv_data_from_server(self):
        rcv_data = self.sock.recv(1024)
        print("receive data : {}".format(rcv_data.decode()))

    
if __name__ == "__main__":
    br_client = BRClient()
    try:
        br_client.wait_server()
        br_client.send_data()
    
    except KeyboardInterrupt:
        print("ctl-C")

    finally:
        br_client.close_sock()