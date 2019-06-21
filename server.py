#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    AUDIO = sys.argv[3]
except (IndexError, ValueError):
    sys.exit("Usage: python3 server.py IP port audio_file")

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))
            linea = line.decode('utf-8').split(" ")
            method = linea[0]
            print(linea)

            try:
                if method == 'INVITE':
                    self.wfile.write(b"SIP/2.0 100 Trying "
                                     b"SIP/2.0 180 Ringing "
                                     b"SIP/2.0 200 OK \r\n\r\n")
                if method == 'ACK':
                    aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + FICH
                    print("Vamos a ejecutar", aEjecutar)
                    os.system(aEjecutar)
                    print("Enviamos cancion")
                if method == 'BYE':
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            except method != ('INVITE' or 'BYE' or 'ACK'):
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', PORT), EchoHandler)
    print("Listening...")
    serv.serve_forever()
