import socket
import json
import binascii
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    start = "499602d2"
    TAM_40 = "00000028"
    FLOW_ID_0 = "00000000"
    START_MENU_RAC = "00000001"
    STOP_MENU_RAC = "00000000"
    MenuValor = "00000001"
    MENU_SELEC_STOP = "00000000"
    UNUSED_RAC = "0000000000000000"
    POSTAMBLE = "b669fd2e"
    valor1 = (start+TAM_40+FLOW_ID_0+START_MENU_RAC+MenuValor+UNUSED_RAC+POSTAMBLE)
    s.connect(('10.163.155.106', 3003))
    #s.settimeout(10000)
    print("CONECTADO")
    #s.sendall(valor1.encode())
    #receber = s.recv(1024)
    #print(receber.decode())

    s.sendall("I–Ò(¶iý.".encode())
    #s.send(valor1.encode(ascii()))

    #s1.sendall(valor1.encode())


    print(valor1)

    print("Deseja desconectar")
    d = input("")




finally:

     exit()



