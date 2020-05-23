from sense_hat import SenseHat
sense = SenseHat()



pixelsvoordigit0 = [
    False, True,  False,
    True,  False, True,
    True,  False, True,
    True,  False, True,
    False, True,  False
]
    
pixelsvoordigit1 = [
    False, False, True,
    False, True,  True,
    False, False, True,
    False, False, True,
    False, False, True
]

pixelsvoordigit2 = [
    True,  True,  False,
    False, False, True,
    False, True,  True,
    True,  False, False,
    True,  True,  True
]

pixelsvoordigit3 = [
    True,  True,  True,
    False, False, True,
    False, True,  True,
    False, False, True,
    True,  True,  True
]

pixelsvoordigit4 = [
    True,  False, True,
    True,  False, True,
    True,  True,  True,
    False, False, True,
    False, False, True
]

pixelsvoordigit5 = [
    False, True,  True,
    True,  False, False,
    True,  True,  False,
    False, False, True,
    True,  True,  True
]

pixelsvoordigit6 = [
    True, True,  True,
    True, False, False,
    True, True,  True,
    True, False, True,
    True, True,  True
]

pixelsvoordigit7 = [
    True,  True,  True,
    False, False, True,
    False, False, True,
    False, False, True,
    False, False, True
]

pixelsvoordigit8 = [
    True, True,  True,
    True, False, True,
    True, True,  True,
    True, False, True,
    True, True,  True
]

pixelsvoordigit9 = [
    True,  True,  True,
    True,  False, True,
    True,  True,  True,
    False, False, True,
    True,  True,  True
]

pixelsvoordigits = [
    pixelsvoordigit0,
    pixelsvoordigit1,
    pixelsvoordigit2,
    pixelsvoordigit3,
    pixelsvoordigit4,
    pixelsvoordigit5,
    pixelsvoordigit6,
    pixelsvoordigit7,
    pixelsvoordigit8,
    pixelsvoordigit9
]

conversiemap_35naar88 = [
    [
        20, 21, 22,
        28, 29, 30,
        36, 37, 38,
        44, 45, 46,
        52, 53, 54
    ],
    [
        16, 17, 18,
        24, 25, 26,
        32, 33, 34,
        40, 41, 42,
        48, 49, 50
    ]
]

plaatsgradenteken = 7

def voegdigittoe(zeefdrukrooster, nummer, positie):
    if positie == 1 and nummer == 0:
        return
    pixels = pixelsvoordigits[nummer]
    conversie = conversiemap_35naar88[positie]
    n = 0
    while n < len(pixels):
        if pixels[n] == True:
            vakje = conversie[n]
            zeefdrukrooster[vakje] = True
        n += 1

def maakrooster(element):
    return [element] * 64

def maakleegrooster():
    return [False] * 64

def voeggradentekentoe(zeefdrukrooster):
    zeefdrukrooster[plaatsgradenteken] = True

def roosterinkleuren(kleurenrooster, zeefdrukrooster, kleur):
    n = 0
    while n < len(zeefdrukrooster):
        if zeefdrukrooster[n] == True:
            kleurenrooster[n] = kleur
        n += 1

def maakkleurenrooster(kleur):
    return maakrooster(kleur)

def toonkleurenrooster(kleurenrooster):
    sense.set_rotation(180)
    sense.set_pixels(kleurenrooster)



if __name__ == "__main__":
    i0 = 0
    while i0 < 10:
        i0 +=1
