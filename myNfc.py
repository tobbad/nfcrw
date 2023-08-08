#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    ????
    Created on ??.??.????
    @author: Tobias Badertscher

"""
import sys
import os
import inspect
import serial

thisModule = sys.modules[__name__]
pythonVersion=sys.version_info[0:3]

class CMDS:
    GET_READER_TYPE = 0x10
    GET_READER_SERIAL = 0x11
    GET_SERIAL_NUMBER = 0x40
    GET_HARDWARE_VERSION = 0x2A
    GET_FIRMWARE_VERSION = 0x29
    GET_BUILD_NUMBER = 0x2B
    READER_KEY_WRITE = 0x12
    USER_DATA_READ = 0x1B
    USER_DATA_WRITE = 0x1C
    READER_KEYS_LOCK = 0x27
    READER_KEYS_UNLOCK = 0x28







class packet:
    CMD_HEADER = 0x55
    CMD_TRAILER = 0xAA
    ACK_HEADER = 0xAC
    RESPONSE_HEADER = 0xDE
    ERR_HEADER = 0xEC
    def __init__(self, cmd):
        self._cmd = cmd

    def serialize(self):
        res = [packet.CMD_HEADER, self._cmd, packet.CMD_TRAILER, 0 ,0 ]
        resb = bytearray(res)
        print(res)
        print(resb)
        xor = resb[0]
        for b in resb[1:]:
            xor ^= b
            print(xor)
        resb.append(xor+7)

        return resb

    def __str__(self):
        return str(self.serialize())
class nfcDev:
    dev = "/dev/ttyUSB0"
    def __init__(self):
        self.serial = serial.Serial(nfcDev.dev, 1000000, timeout=1)
        print("Open tty")

    def GET_READER_TYPE(self):
        p = packet(CMDS.GET_READER_TYPE)
        print("Send %s"% p)
        self.serial.write(p.serialize())
        res = self.serial.read()
        print(res)


    def __str__(self):
        return str(self.serial)


if __name__ == "__main__":
    n = nfcDev()
    n.GET_READER_TYPE()
