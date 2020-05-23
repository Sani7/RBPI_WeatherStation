from sense_hat import SenseHat
sense = SenseHat()
from display import *

def leestemperatuur():
    #correctie temperatuur -10graden Celcius nagekeken met thermostaat
    return int(round(sense.get_temperature(),0)) - 10

def leestemperatuuralsdigits():
    temperatuur = leestemperatuur()
    temp0 = temperatuur % 10
    temp1 = temperatuur //10
    return temp0, temp1

def temperatuurtonen():
    
    zeefdruk = maakleegrooster()
    temp0, temp1 = leestemperatuuralsdigits()
    voegdigittoe(zeefdruk, temp0, 0)
    voegdigittoe(zeefdruk, temp1, 1)

    voeggradentekentoe(zeefdruk)
            
    rooster = maakkleurenrooster((0,0,200))
    roosterinkleuren(rooster, zeefdruk, (255, 255, 255))
    toonkleurenrooster(rooster)
