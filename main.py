from sense_hat import SenseHat
import time
from clock import *
from barometer import luchtdruktonen
from temperatuur import temperatuurtonen

sense = SenseHat()

def wachten():
    time.sleep (5)

def schermwissen():
    sense.clear()
  

try:
    while (True):
        temperatuurtonen()
        wachten()
        schermwissen()
        luchtdruktonen()
        wachten()
        schermwissen()
        kloktonen()
        wachten()
        schermwissen()
        
except KeyboardInterrupt:
    schermwissen()

