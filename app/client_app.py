from socket import*
from gui.client_window import on_closing

if __name__ == '__main__':

    ip = [(s.connect(('8.8.8.8', 55)), s.getsockname()[0], s.close()) for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]

    server_app = on_closing()
    server_app.open()

