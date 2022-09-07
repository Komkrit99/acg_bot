import threading
import time
z = 0
c = 0
def ch():
    global z,c
    z = 1
    c = 1
def print_pls():
  while(True):
    print(z,c)
threading.Thread(target=print_pls).start()
time.sleep(3)
ch()