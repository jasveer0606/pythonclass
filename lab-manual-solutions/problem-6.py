import socket
import threading
import subprocess

HOST = ''
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(8)
lock = threading.Lock()

##CREDENTIALS START
login_username = "admin"
login_password = "password"
##CREDENTIALS END

# Super clumsy way to get IPv4 on Windows, but it works.
def get_address():
    text = subprocess.check_output("ipconfig")
    subs = "IPv4 Address. . . . . . . . . . . : "
    return text[text.find(subs)+len(subs):text.find(subs)+len(subs)+12]


class Client:

    def __init__(self, socket_con, address):
        self.socket = socket_con
        self.address = address
        self.data = ""
        self.authenticated = False
        self.is_connected = False


class Server(threading.Thread):

    def __init__(self, address, port):
        threading.Thread.__init__(self)
        self.address = address
        self.port = port
        self.username = login_username
        self.password = login_password
        self.clients = []
        self.threads = 4

    def handle_connect(self):
        client = Client(*sock.accept())
        client.is_connected = True
        self.clients.append(client)
        self.authenticate_client(client)
        while client.is_connected:
            client.is_connected = self.serve_client(client)

    def serve_client(self, client):
        try:
            client.socket.send("\n>> ")
            client.data = client.socket.recv(1024).strip()
            lock.acquire()
            client.socket.send(client.data)

            if client.data.startswith("$ "):
                self.parse_command(client, client.data)
                print "%s:%s" % client.address + " issued : " + client.data
                lock.release()
                return 1
            else:    
                print "%s:%s" % client.address + " says : " + client.data
                lock.release()
                return 1
        except:
            print '::'.join(map(str, client.address)), "is disconnected."
            return 0


    def parse_command(self, client, data):
        output = subprocess.check_output(data.lstrip("$ "), shell=True)
        client.socket.send("\n"+output)

    def authenticate_client(self, client):
        print '\n' + '::'.join(map(str, client.address)), "is trying to authenticate."
        client.socket.send("Username:")
        username = client.socket.recv(1024)
        client.socket.send("Password:")
        password = client.socket.recv(1024)

        if username.strip() == self.username and password.strip() == self.password:
            client.authenticated = True
            print '::'.join(map(str, client.address)), "is now authenticated."
        else:
            client.authenticated = False
            client.socket.send("\nAuthentication failed.\n")
            self.clean(client)

    def persist(self):
        for _ in range(self.threads):
            try:
                lock.acquire()
                connect_thread = threading.Thread(target=self.handle_connect)
                connect_thread.start()
                lock.release()
            except:
                pass

    def clean(self, client):
        self.clients.remove(client)
        print '::'.join(map(str, client.address)), "is disconnected."
        client.socket.close()

    def update_clients(self):
        duplicate_list = self.clients
        for client in duplicate_list:
            if not client.is_connected:
                self.clean(client)

def test_server(*args):
    print "  Server is up on "+get_address()
    print "  Listening on tcp/"+str(PORT)
    print "==============================="
    tcp_serve = Server(get_address(), PORT)
    tcp_serve.persist()

if __name__ == '__main__':
    test_server([0, 0, 0])

