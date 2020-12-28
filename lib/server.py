from socket import *
from time import ctime
from tkinter import Label

class Server(object):
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__listener = socket(AF_INET, SOCK_STREAM)

    def config(self):
        self.__listener.bind(self.__address)
        self.__listener.listen(15)

    def work(self):
        self.config()
        while True:
            print('Сервер находиться в режиме ожидания запросов на соеденение ...')
            conn, client = self.__listener.accept()
            print(f'{ctime()}: получен запрос на соеденение от {client}')

            data = conn.recv(1024)
            mess = bytes.decode(data)
            print(mess)
            name = mess[1:mess.find('>>>')-1]
            text = mess[mess.find('>>>') + 3:]
            print(f'{name} => {text}')

            response = f'Сообщение от клиента {name}: [{text}] - успешно доставлено.'
            data = str.encode(response)
            conn.send(data)

            conn.close()
            if text == 'StopServer2020111':
                print('Сервер остановлен по команде администратора')
                break

    def work_gui(self, label: Label):
        self.config()

        def _append_label_text(new_text: str):
            current_text = label.cget('text')
            current_text += '>>>' + new_text + '\n'
            label.configure(text=current_text)

        while True:
            _append_label_text('Сервер находиться в режиме ожидания запросов на соеденение ...')
            conn, client = self.__listener.accept()
            _append_label_text(f'{ctime()}: получен запрос на соеденение от {client}')

            data = conn.recv(1024)
            mess = bytes.decode(data)

            name = mess[1:mess.find('>>>') - 1]
            text = mess[mess.find('>>>') + 3:]

            _append_label_text(f'{name} => {text}')

            response = f'Сообщение от клиента {name}: [{text}] - успешно доставлено.'
            data = str.encode(response)
            conn.send(data)

            conn.close()
            if text == 'StopServer2020111':
                print('Сервер остановлен по команде администратора')
                break


