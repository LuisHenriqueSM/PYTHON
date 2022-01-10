import codecs
import socket
import binascii

from datetime import time
from typing import Union

START = "499602d2"
TAM_40 = "00000028"
FLOW_ID_0 = "00000000"
START_MENU_RAC = "00000001"
STOP_MENU_RAC = "00000000"
MenuValor = "00000001"
MENU_SELEC_STOP = "00000000"
UNUSED_RAC = "0000000000000000"
POSTAMBLE = "b669fd2e"

valor1 = (START+TAM_40+FLOW_ID_0+STOP_MENU_RAC+MenuValor+UNUSED_RAC+POSTAMBLE)
print(valor1)



#INICIANDO CONVERSÃO DE HEX PARA INT

serie1= '0x49'
a = int(serie1, 16)

serie2= '0x96'
b = int(serie2, 16)

serie3= '0x02'
c = int(serie3, 16)

serie4= '0xd2'
d = int(serie4, 16)

valorInt = ([a]+[b]+[c]+[d])
print(valorInt)

#INICIANDO CONVERSÃO DE INT PARA ASCII

asc1 = 73
conv1 = chr(asc1)

asc2 = 150
conv2 = chr(asc2)

asc3 = 2
conv3 = chr(asc3)

asc4 = 210
conv4 = chr(asc4)

valorAscii = (conv1+conv2+conv3+conv4)
print(valorAscii)


# Iniciando conexâo SOCKET



    #s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s2.connect(('10.163.155.106', 3001))
s.connect(('10.163.155.106', 3003))


    #comando_cortex = codecs.encode('\x49\x96\x02\xd2\x00\x00\x00\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\
    #\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\xb6\x69\xfd\x2e')

valor = b'\x49\x96\x02\xd2\x00\x00\x00\x28\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb6\x69\xfd\x2e'.hex()

print(valor)




    # ESTE EXEMPLO POSSO ENVIAR MENSAGEM EM HEXA, ELE CONVERTE PARA ASCII, PORÉM, ENVIA O DADOS EM HEXA
    #msg = s.send(bytes(valor, 'ascii'))

    #Outra forma de enviar o dado em Hexa SEM CONVERTER para ASCII
#msg = s.send(codecs.encode(valor))
msg = s.send(bytes.fromhex(valor))
s.close()

print(msg)




    #print("Falha ao conectar ou enviar o comando para o cortex")
    #s.close()
    #s2.close()





#jj=input()
#print(msg)

#print(msg)



