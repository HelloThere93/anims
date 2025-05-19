import pgzrun
import random

WIDTH = 800
HEIGHT = 450
apple = Actor("appleimg.png")
apple.pos = (48, 225)
deb = False
def startAnim():
    global deb
    deb = True
    animate(apple, pos = (752,225), duration = 5, on_finished = endAnim)
 

def endAnim():
    global deb
    deb = False
    animate(apple, pos = (0, 225), duration = 5, on_finished = startAnim) 
   
def draw():
    screen.clear()
    screen.blit("bg.jpg",(0,0))
    apple.draw()

def on_key_down(key):
    global deb
    if key == keys.SPACE and deb == False:
        startAnim()


pgzrun.go()

