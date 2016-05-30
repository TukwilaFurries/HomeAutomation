#!/usr/bin/python

class cbtestObject:

    def __init__(self):
        print 'cbtestObject created'

    def cbPrint(self, toPrint):
        print 'about to print callback message'
        print toPrint