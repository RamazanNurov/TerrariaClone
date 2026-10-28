from pygame import *
import variables as v
class Entity:
    def __init__(self,x,y, hp, vel, jh):
        self.x = x
        self.y = y
        self.health = hp 
        self.velocity = vel
        self.jump_height = jh

class Player(Entity):
    def __init__(self,x,y, hp,vel,jh,sat,mp):
        super().__init__(x,y,hp,vel,jh)
        self.mana_points = mp
        self.saturation = sat
        self.hitbox = Rect(self.x,self.y,30,10)


    def movement(self):
        keys = key.get_pressed()
        if keys[K_a] and self.hitbox.x > 0:
            self.hitbox.x -= self.velocity
        if keys[K_d] and self.hitbox.x < v.width:
            self.hitbox.x += self.velocity
        if keys[K_w] and self.hitbox.y > 0:
            self.hitbox.y -= self.velocity
        if keys[K_s] and self.hitbox.y < v.length:
            self.hitbox.y += self.velocity

class Enemy(Entity):
    pass
