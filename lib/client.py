from socket import *
from tkinter import *
from time import ctime

class Client(object):
    def __init__(self, host, port, name):
        self.__host = host
        self.__port = port
        self.__address = (self.__host, self.__port)
        self.__client = None
        self.__name = name



    def connect(self):
        if self.__client is None:
            self.__client = socket(AF_INET, SOCK_STREAM)
            self.__client.connect(self.__address)

    def work(self):
        while True:
            mess = f"[{self.__name}]>>>>" + input('Введите сообщение:')
            data = str.encode(mess)
            self.connect()
            self.__client.send(data)
            print('Сообщение отправлено')

            data = self.__client.recv(1024)
            response = bytes.decode(data)
            print(response)

            self.__client.close()
            self.__client = None

            stop = input('Продолжить программу? y/n ')
            if stop == 'n':
                break


