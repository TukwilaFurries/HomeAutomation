#!/usr/bin/python

class cbListener:
    cblist = []


    def __init__(self):
        print 'cbtestObject created'

    def addCB(self, cbIn):
        self.cblist.append(cbIn)
        print 'attempting callback'
        cbIn('callback from listener')
        