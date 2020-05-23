from sense_hat import SenseHat
sense = SenseHat()
import time
barrometer = False
Z = (0, 0, 0)
Y = (255, 214, 0)
y = (255, 255, 0)
G = (48, 48, 64)
B = (0, 0, 255)
W = (255, 255, 255)
donderwolk =  [
    Z, Z, Z, G, G, Z, Z, Z,
    Z, Z, G, G, G, Z, Z, Z,
    Z, G, G, G, G, G, Z, Z,
    Z, G, G, Y, G, G, G, Z,
    G, G, G, G, Y, G, G, G,
    Z, G, G, Y, Y, G, G, Z,
    Z, Z, Z, Y, Z, Z, Z, Z,
    Z, Z, Z, Z, Y, Z, Z, Z
    ]

regen =  [
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, G, G, Z, Z, Z,
    Z, Z, G, G, G, G, G, Z,
    Z, G, G, G, G, G, G, Z,
    Z, G, G, G, G, G, G, Z,
    Z, Z, Z, Z, B, Z, Z, Z,
    Z, Z, B, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, B, Z, Z
    ]

bewolkt =  [
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, G, G, Z, Z, Z,
    Z, Z, G, G, G, G, G, Z,
    Z, G, G, G, G, G, G, Z,
    Z, G, G, G, G, G, G, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z
    ]

normaal =  [
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, W, W, Z, Z, Z,
    Z, Z, W, W, W, W, W, Z,
    Z, W, W, W, W, W, W, Z,
    Z, W, W, W, W, W, W, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z
    ]

zon =  [
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, W, W, Z, Z, Z,
    Z, Z, W, W, W, y, y, Z,
    Z, W, W, W, W, y, y, Z,
    Z, W, W, W, W, W, W, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z
    ]

zonnig =  [
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, y, y, Z, Z,
    Z, Z, Z, y, y, y, y, Z,
    Z, Z, Z, y, y, y, y, Z,
    Z, Z, Z, Z, y, y, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z,
    Z, Z, Z, Z, Z, Z, Z, Z
    ]
    
def luchtdruktonen():    
    p = sense.get_pressure()
    p = round (p , 1)
    p = int(p)
    if p < 976 :
        pixels = donderwolk
    elif p < 992 :
        pixels = regen
    elif p < 1009 :
        pixels = normaal
    elif p < 1026 :
        pixels = zon
    else:
        pixels = zonnig

        
    sense.set_rotation(180)
    sense.set_pixels(pixels)
    
