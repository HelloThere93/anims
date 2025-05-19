import pgzrun
import random

WIDTH = 800
HEIGHT = 450
apple = Actor("appleimg.png")
apple.pos = (48, 225)

def startAnim():
    animate(apple, pos = (752,225), duration = 5)
    
def draw():
    screen.clear()
    screen.blit("bg.jpg",(0,0))
    apple.draw()

startAnim()


pgzrun.go()

