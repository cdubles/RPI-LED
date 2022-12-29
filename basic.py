import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 1) #initialize light strip

pixels.fill((0, 255, 0)) #turn all lights green