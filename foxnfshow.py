#!/usr/bin/env python
import threading
import struct
import socket
import time
import sys
import bz2
#################################################################################
def s2int(d):
    return ord(d[0])*256*256*256+ord(d[1])*256*256+ord(d[2])*256+ord(d[3])
#################################################################################
def int2s(d):
    return chr((d>>24) & 0xff) + chr((d>>16) & 0xff) + chr((d>>8) & 0xff) + chr(d & 0xff)
#################################################################################
def b2int(d):
    return d[0]*256*256*256+d[1]*256*256+d[2]*256+d[3]
#################################################################################
def b2ip(d):
    return str(d[0])+"."+str(d[1])+"."+str(d[2])+"."+str(d[3])
#################################################################################
def s2ip(d):
    return str(ord(d[0]))+"."+str(ord(d[1]))+"."+str(ord(d[2]))+"."+str(ord(d[3]))
#################################################################################
def decodekey(st):
    print ord(st[0]),
    print s2ip(st[1:5]),
    print ord(st[5])*256+ord(st[6]),
    print s2ip(st[7:11]),
    print ord(st[11])*256+ord(st[12])
#################################################################################
def pdv1(d):
    key=d[38]+d[0:4]+d[32:34]+d[4:8]+d[34:36]
    nf_dpkts=d[16:20]
    nf_doctets=d[20:24]
    print decodekey(key),s2int(nf_dpkts),s2int(nf_doctets)
#################################################################################
def pdv5(d):
    key=d[38]+d[0:4]+d[32:34]+d[4:8]+d[34:36]
    nf_dpkts=d[16:20]
    nf_doctets=d[20:24]
    print decodekey(key),s2int(nf_dpkts),s2int(nf_doctets)
#################################################################################
def rhv1(d):
    nf_pl=48
    print "Version 1"
    for i in range((len(d)-16)/48):
        print "rec:",i
        pdv1(d[16+nf_pl*i:])
#################################################################################
def rhv5(d):
    nf_pl=48
    print "Version 5"
    for i in range((len(d)-23)/48):
        print "rec:",i
        pdv5(d[24+nf_pl*i:])
#################################################################################
def nfcap():
    while 1:
            s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.bind(("",9995))
            while 1:
                d,froms = s.recvfrom(1024)
                nf_ver = ord(d[0])*256+ord(d[1])
                if nf_ver == 1: rhv1(d)
                if nf_ver == 5: rhv5(d)
#################################################################################
nfcap()
