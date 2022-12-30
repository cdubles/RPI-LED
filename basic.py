import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 150) #initialize light strip

pixels.fill((0, 255, 0)) #turn all lights green