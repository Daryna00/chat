from threading import Thread
from tkinter import Label, Entry
from lib.server import Server
from lib.client import Client

class MyServerThread(Thread):
    def __init__(self, server: Server, label: Label):
        super(MyServerThread, self).__init__()
        self.__server = server
        self.__label = label

    def run(self) -> None:
        self.__server.work_gui(self.__label)





