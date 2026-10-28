from pygame import *
import classes
width, length = 800, 600
x,y = width // 2, length // 2
screen = display.set_mode((width,length))
player1 = classes.Player(x,y,100,20,40,100,20)