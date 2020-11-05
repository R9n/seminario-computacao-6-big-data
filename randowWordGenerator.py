#!/usr/bin/env python3
# Desenvolvimento Aberto
# shell.py
 
# Importar modulo do sistema operacional
import os
# Importar modulo Random para obter elementos aleatórios da lista de textos
import random
# Importar modulo time para configurar tempo de espera entre os envios das mensagens
import time

import socket
 
# Usa o comando do shell ls

#Apaga a tela
os.system("clear")
 

texts =  [

"text text text text text text text ",

"text text text ",

"neque ac, pulvinar dapibus mi. Sed quis tincidunt dolor, vel hendrerit mauris. Vivamus varius varius neque, commodo euismod felis placerat vel. Quisque nec hendrerit arcu. Ut non fermentum nisi, a lobortis erat. Fusce tortor justo, facilisis sit amet sagittis vitae,",

"text text ",
"text text text text text ",
"nisi volutpat dictum. Pellentesque ac neque lobortis, malesuada justo pellentesque, viverra est. Pellentesque sem ligula, sollicitudin nec ",
"text text text text text text text text text text text text ",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ",

"text text text text text text text text text text text text text text text ",

"tincidunt at. Quisque luctus nec neque et vestibulum. Integer euismod iaculis eros, sit amet lobortis lorem mollis et. Nulla et gravida elit, "
"text text text text text text text text text text text text text text text text text text text text text text text text text text text text text text ",

"Duis bibendum eros a eros dapibus, eget vestibulum enim interdum. Pellentesque id felis quis tortor posuere maximus. Praesent molestie augue justo, eget egestas justo varius vitae. Integer euismod erat bibendum dolor hendrerit, ac viverra dui eleifend. Donec non placerat nisi. Phasellus ultrices mauris at molestie porttitor. In vitae urna non lacus vulputate mollis. Nunc gravida sollicitudin neque finibus interdum. Proin neque tortor, aliquet eget purus vel, elementum feugiat nulla. In vehicula tempor augue quis pellentesque. Nunc cursus non tellus quis ultrices. Suspendisse nisl lacus, ultricies vel mi sed, bibendum efficitur est.",

"Duis et mattis purus. Vivamus sapien augue, condimentum eget tellus eget, varius aliquet lorem. Maecenas purus magna, rutrum sit amet neque ac, pulvinar dapibus mi. Sed quis tincidunt dolor, vel hendrerit mauris. Vivamus varius varius neque, commodo euismod felis placerat vel. Quisque nec hendrerit arcu. Ut non fermentum nisi, a lobortis erat. Fusce tortor justo, facilisis sit amet sagittis vitae, pellentesque id purus. Mauris commodo efficitur turpis ac dignissim. Donec urna diam, fermentum eu lacinia id, interdum ac neque. "
]

#configurações de host e porta
netCatPort = 1027
netCatHost = "localhost"
timeInterval= 1.5





      # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((netCatHost, netCatPort))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while (True):
			time.sleep(timeInterval)
			text = random.choice(texts)+'\n';
			conn.sendall(text.encode())
			
	
	
