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
def ip2int(d):
    return int(d.split(".")[0])*256*256*256+int(d.split(".")[1])*256*256+int(d.split(".")[2])*256+int(d.split(".")[3])
#################################################################################
def ip2s(d):
    return chr(int(d.split(".")[0]))+chr(int(d.split(".")[1]))+chr(int(d.split(".")[2]))+chr(int(d.split(".")[3]))
#################################################################################
#################################################################################
if len(sys.argv)<3:
    print sys.argv[0],"<ip,ip,ip...> foxnetflow.*.bz2"
    sys.exit(0)
ips=sys.argv[1].split(",")
ipss=[]
for i in ips:
    ipss+=[ip2s(i)]
for f in sys.argv[2:]:
    df =bz2.BZ2File(f,"r")
    while 1:
        try:
            st=df.read(29)
        except:
            break
        if not st: break
#       print ipss, st[1:5]
        if st[1:5] in ipss or st[7:11] in ipss:
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
