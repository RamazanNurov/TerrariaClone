from pygame import *
# VARIABLES -------------------------------------------------
width, length = 800, 600
fps = 60
clock = time.Clock()
x,y = width // 2, length // 2
tile = 30
screen = display.set_mode((width,length))

# CLASSES ---------------------------------------------------
class Blocks:
    def __init__(self, x,y, w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.blockHB = Rect(self.x, self.y, self.width, self.height)

class Entity:
    def __init__(self,x,y, hp, vel, jh, t_x, t_y):
        self.x = x
        self.y = y
        self.tile_x = t_x
        self.tile_y = t_y
        self.health = hp 
        self.velocity = vel
        self.jump_height = jh
        self.hitbox = Rect(self.x,self.y,self.tile_x,self.tile_y)
        self.vel_y = 0
        self.on_ground = False

    def gravity(self):
            g_force = 1
            self.vel_y += g_force
            self.hitbox.y += self.vel_y 
            self.on_ground = False
            if self.hitbox.colliderect(block1.blockHB):
                if self.vel_y>0:
                    self.hitbox.bottom = block1.blockHB.top
                    self.on_ground = True
                    self.vel_y = 0

class Player(Entity):
    def __init__(self,x,y, hp,vel,jh, t_x, t_y,sat,mp):
        super().__init__(x,y,hp,vel,jh, t_x, t_y)
        self.mana_points = mp
        self.saturation = sat



    def movement(self):
        keys = key.get_pressed()
        if keys[K_a] and self.hitbox.x > 0:
            self.hitbox.x -= self.velocity
        if keys[K_d] and self.hitbox.x < width:
            self.hitbox.x += self.velocity
        if keys[K_w] and self.on_ground:
            self.vel_y = -self.jump_height
            self.on_ground = False
        

class Enemy(Entity):
    pass



# OBJECTS ---------------------------------------------------

player1 = Player(x,y,100, 3, 15,20,40,100,100)

block1 = Blocks(x,y+40, 100, 20)