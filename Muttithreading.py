import threading
from threading import Thread
from threading import *


class Hello:
    def run(Thread):
        for i in range(5):
            print("Hello")



class Hi:
    def run(Thread):
        for i in range(5):
            print("Hi")




t1= Hello()
t2= Hi()
t1.start()
t2.start()


