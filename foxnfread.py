#!/usr/bin/env python
import threading
import struct
import socket
import time
import datetime
import sys
import bz2

#################################################################################
def s2int(d):
    return ord(d[0])*256*256*256+ord(d[1])*256*256+ord(d[2])*256+ord(d[3])
#################################################################################
def b2int(d):
    return d[0]*256*256*256+d[1]*256*256+d[2]*256+d[3]
#################################################################################
def s2ip(d):
    return str(ord(d[0]))+"."+str(ord(d[1]))+"."+str(ord(d[2]))+"."+str(ord(d[3]))
#################################################################################
#################################################################################
#################################################################################
#################################################################################
if len(sys.argv)<2:
    print sys.argv[0],"foxnetflow.*.bz2"
    sys.exit(0)
for f in sys.argv[1:]:
    df =bz2.BZ2File(f,"r")
    while 1:
        try:
            st=df.read(29)
        except:
            break
        if not st: break
        print ord(st[0]),
        print s2ip(st[1:5]),
        print ord(st[5])*256+ord(st[6]),
        print s2ip(st[7:11]),
        print ord(st[11])*256+ord(st[12]),
        print s2int(st[13:17]),
        print s2int(st[17:21]),
        print datetime.datetime.fromtimestamp(struct.unpack("<f",st[21:25])[0]).strftime('%Y-%m-%d %H:%M:%S'),
        print datetime.datetime.fromtimestamp(struct.unpack("<f",st[25:29])[0]).strftime('%Y-%m-%d %H:%M:%S')
    df.close()
