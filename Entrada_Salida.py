import threading
import time

x=0

def P1():
    global x
    while True:
        x += 1 #Entrada de visitante
        time.sleep(0.5)
        
def P2():
    global x
    while True:
        x -= 1 #Salida de visitante
        time.sleep(0.7)

t1 = threading.Thread(target=P1)
t2 = threading.Thread(target=P2)

t1.start()
t2.start()

while True:
    print(f"Visitantes actuales: {x}")
    time.sleep(1)