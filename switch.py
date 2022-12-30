import board
import neopixel
import time
pixelCount = 150
pixels = neopixel.NeoPixel(board.D18, pixelCount)

while True:
    time.sleep(1)
    pixels.fill((0,255,0))
    time.sleep(1)
    pixels.fill((0,0,255))


