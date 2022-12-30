import board
import neopixel
pixelCount = 150
pixels = neopixel.NeoPixel(board.D18, pixelCount)

for x in range(0,pixelCount):
    if(x%2==0):
        pixels[x] = (255,0,0)
    else:
        pixels[x] = (0,0,255)