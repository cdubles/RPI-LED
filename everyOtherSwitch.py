import board
import neopixel
pixelCount = 150
pixels = neopixel.NeoPixel(board.D18, pixelCount)
mod =0;
while True:
    for x in range(0,pixelCount):
        if((x+mod)%2==0):
            pixels[x] = (255,0,0)
        else:
            pixels[x] = (0,0,255)
    mod+=1