#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente que abre un socket a un servidor."""

import socket
import sys

try:
    METHOD = sys.argv[1]  # Método SIP
    RECEIVER = sys.argv[2].split(':')[0]   # Receptor@IP.
    IP = RECEIVER.split('@')[-1]  # Dirección IP.
    PORT = int(sys.argv[2].split(':')[1])  # PuertoSIP.

except (IndexError, ValueError):
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")


try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((IP, PORT))

        CODE = (METHOD + ' sip:' + RECEIVER + ' SIP/2.0\r\n\r\n')
        print(CODE)
        my_socket.send(bytes(CODE, 'utf-8'))
        data = my_socket.recv(1024)
        if METHOD == 'INVITE' and data.decode('utf-8').split()[-2] == '200':
            my_socket.send(bytes('ACK sip:' + RECEIVER + ' SIP/2.0\r\n\r\n',
                                 'utf-8'))
            print(data.decode('utf-8'))
        if method == 'BYE':
            print('FINISHING CONNECTION.')

except ConnectionRefusedError:
    print('CONNECTION ERROR')

except (IndexError, ValueError):
    sys.exit('Try: NAME@IP:PORT')
