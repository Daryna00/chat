from tkinter import *
from lib.client import Client
from socket import *


class ClientWindow:
    def __init__(self):
        self.__root = Tk()
        self.__entry = Entry(self.__root)
        self.__entry2 = Entry(self.__root)
        self.__frame = Frame(self.__root)
        self.__label = Label(self.__frame)
        self.__label2 = Label(self.__frame)
        self.__chat = Label(self.__frame)

        self.__host = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]

        self.__port = 9001
        self.__client = socket(self.__host, self.__port)

    def config(self):
        self.__root.title('Клиент модуль')
        self.__root.geometry("600x900")
        self.__root.resizable(True, False)

        self.__label.config(text=str(self.__host), font='Arial 15', fg='purple')
        self.__chat.config(font='Arial 12', fg='navy', width=100, justify=LEFT)
        self.__entry.config()
        self.__label2.config(font='Arial 15', fg='purple')
        self.__entry2.config()

    def layout(self):
        self.__frame.pack(padx=15, pady=15)
        self.__label.pack(padx=15)
        self.__chat.pack(padx=15, pady=15)
        self.__entry.pack(padx=15)
        self.__label2.pack(padx=15)
        self.__entry2.pack(padx=15)

    def work_gui(self):
        while True:
            mess = self.__entry.get()
            data = str.encode(mess)
            self.connect()
            self.__client.send(data)
            print('Сообщение отправлено')

            data = self.__client.recv(1024)
            response = bytes.decode(data)
            self.__label.config(text=response)

            self.__client.close()
            self.__client = None

            self.__label2.config('Продолжить программу? y/n ')
            stop = self.__entry2.get()
            if stop == 'n':
                break


    def open(self):
        self.config()
        self.layout()
        self.work_gui()
        self.__root.mainloop()