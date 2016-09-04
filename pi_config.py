#!/usr/bin/python

# Every module class MUST have a "getName()" method which returns if it is available on a RPi
class RGB:
    @staticmethod
    def getPinR():
        return 17

    @staticmethod
    def getPinG():
        return 22

    @staticmethod
    def getPinB():
        return 24
    @staticmethod
    def getName():
        return "RGB"

    @staticmethod
    def getLogLocation():
        from config import DIR
        return (DIR.LOGS + "rgb.log")

class GLOBAL:
    @staticmethod
    def getListenerPort():
        return 15555

    @staticmethod
    def getListenerAddress():
        return "10.0.0.98"

    @staticmethod
    def getServerAddress():
        return "10.0.0.99"
