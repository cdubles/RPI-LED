import board
import neopixel
import random
pixelCount = 150
pixels = neopixel.NeoPixel(board.D18, pixelCount)

while True:
    for x in range(0,pixelCount):
        R = random.randint(0,255)
        G = random.randint(0,255)  
        B = random.randint(0,255)
        pixels[x] = (R,G,B)
