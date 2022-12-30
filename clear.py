import board
import neopixel
pixelCount = 150
pixels = neopixel.NeoPixel(board.D18, pixelCount)

pixels.fill((0,0,0))