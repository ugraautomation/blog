# -*- coding: utf-8 -*
__author__ = 'b9om'


import telnetlib
from inv_utils import *



def grab_telnet(host,username='budnik'.encode(),password = 'SEsqN4rW'.encode()):
    tn = telnetlib.Telnet(host)
    tn.read_until("Username:".encode())
    tn.write(username+"\n".encode())
    tn.read_until("Password:".encode())
    tn.write(password+"\n".encode())
    tn.write("terminal length 0".encode()+"\n".encode())
    tn.write("sh inv".encode()+"\n".encode())
    tn.write("exit".encode()+"\n".encode())
    output=tn.read_all()
    inv = Inv(output)
    s = ""
    for twin in inv.get_inventory():
        pid, sn = twin[0], twin[1]
        s = s + pid + ' ' + sn + '\n'
    return s



print(grab_telnet('10.10.118.1'))