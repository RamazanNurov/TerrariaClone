from pygame import *
class Entity:
    def __init__(self,x,y, hp, vel, jh):
        self.x = x
        self.y = y
        self.health = hp 
        self.velocity = vel
        self.jump_height = jh

class Player(Entity):
    def __init__(self,x,y, hp,vel,jh,sat,mp):
        super.__init__(x,y,hp,vel,jh)
        self.mana_points = mp
        self.saturation = sat
        self.hitbox = Rect(self.x,self.y,30,10)

class Enemy(Entity):
    pass
