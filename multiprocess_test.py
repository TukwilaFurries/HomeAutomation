#!/usr/bin/python3

import multiprocessing as mp
from multiprocessing.managers import BaseManager

class MyManager(BaseManager): pass

def Manager():
    m = MyManager()
    m.start()
    return m

class cls:
    def __init__(self):
        self.var = "A"
    def get_var(self):
        return self.var
    def set_var(self, var):
        self.var = var

class PiLights:
    def __init__(self):
        self.color = ""
        self.value = 0

    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color

    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value

def set_color(lights, color, value):
    lights.set_color(color)
    lights.set_value(value)

def get_color(lights):
    return lights.get_color()

def foo1(qIn, qOut):
    cont = True
    while(cont):
        newVar = qIn.get()
        print(newVar)
        print("Got %s " % newVar)
        if newVar ==  "None":
            qOut.put("EXITING PROGRAM")
            cont = False
        else:
            qOut.put(newVar)
def setProcessName(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0,0,0)

def testPiLights(qIn, qOut, pi):
    import setproctitle as spt
    spt.setproctitle("MyProcessName")
    print("testPiLights() {")
    i = 10000000
    while (i > 0): 
        i = i - 1
    print("Name: %s" % mp.current_process().name)
    while(qIn.get()):
        print("== Got a message")
        qOut.put(pi.get_color())
    else:
        print ("== Did not get a message")
    print("} testPiLights()")

if __name__ == '__main__':
    mp.set_start_method('spawn')

    qIn = mp.Queue()
    qOut = mp.Queue()

    MyManager.register('PiLights', PiLights)
    manager = Manager()
    pi = manager.PiLights()
    p = mp.Process(target=testPiLights, args=(qIn, qOut, pi), name="TESTNAME")
    p.name = "NAME"
    print(p.name)
    p.start()
    
    pi.set_color("Blue")
    qIn.put(True)
    print(qOut.get())
    
    pi.set_color("Green")
    qIn.put(True)
    print(qOut.get())
    from time import sleep
    i = 1000
    while (i > 0):
        i = i - 1
    pi.set_color("Red")
    qIn.put(True)
    print(qOut.get())
    qIn.put(False)
    
    p.join()
