import pygame as pg
# from classes import *
pg.init()


# VARIABLES -------------------------------------------------
width, length = 800, 600
fps = 60
clock = pg.time.Clock()
x,y = width // 2, length // 2
screen = pg.display.set_mode((width,length))
map_d = [
    '11111111111111111111',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10000000000000000000',
    '10001000000000000000',
    '10001000000000000000',
    '10001000000000000000',
    '11111111111111111111'
] 
blocks = []
tile = 40
offset_x = 0
offset_y = 500
rows = len(map_d)
cols = (len(map_d[0]))
# CLASSES ---------------------------------------------------
class Blocks:
    def __init__(self, x,y, w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.blockHB = pg.Rect(self.x, self.y, self.width, self.height)

class Entity:
    def __init__(self,x,y, hp, vel, jh, t_x, t_y):
        self.x = x
        self.y = y
        self.tile_x = t_x
        self.tile_y = t_y
        self.health = hp 
        self.velocity = vel
        self.jump_height = jh
        self.hitbox = pg.Rect(self.x,self.y,self.tile_x,self.tile_y)
        self.vel_y = 0
        self.on_ground = False

    def gravity(self):
        self.vel_y += 0.3
        self.on_ground = False

        # пробуем сдвинуться вниз
        self.hitbox.y += self.vel_y
        idx = self.hitbox.collidelist([b.blockHB for b in blocks])
        if idx != -1:
            block = blocks[idx]
            if self.vel_y > 0:                     # падаем — встаём на верх блока
                self.hitbox.bottom = block.blockHB.top
                self.on_ground = True
                self.vel_y = 0
            elif self.vel_y < 0:                   # летим вверх — бьёмся головой
                self.hitbox.top = block.blockHB.bottom
                self.vel_y = 0


class Player(Entity):
    def __init__(self,x,y, hp,vel,jh, t_x, t_y,sat,mp):
        super().__init__(x,y,hp,vel,jh, t_x, t_y)
        self.mana_points = mp
        self.saturation = sat
        self.vel_x = 0



    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.hitbox.x > 0 or keys[pg.K_LEFT] and self.hitbox.x > 0:
            self.vel_x -= 5
        elif keys[pg.K_d] and self.hitbox.x < width or keys[pg.K_RIGHT] and self.hitbox.x < width:
            self.vel_x += 5
        else:
            self.vel_x *= 0.8
        if keys[pg.K_w] and self.on_ground or keys[pg.K_UP] and self.on_ground:
            self.vel_y = -self.jump_height
            self.on_ground = False

        self.vel_x = max(-self.velocity, min(self.velocity,self.vel_x))
        self.hitbox.x += self.vel_x

        idxs = self.hitbox.collidelistall([b.blockHB for b in blocks])
        
        for idx in idxs:
            block = blocks[idx]
            if self.vel_x > 0:
                self.hitbox.right = block.blockHB.left
            elif self.vel_x < 0:
                self.hitbox.left = block.blockHB.right
        

class Enemy(Entity):
    pass


player1 = Player(x,y,100, 3, 10,20,40,100,100)
for row_i, row in enumerate(map_d):
    for col_i, char in enumerate(row):
        if char == "1":
            bx = col_i * tile
            by = row_i * tile
            blocks.append(Blocks(bx,by, tile, tile))

def add_block(x,y):
    print("Tryin to add block")
    for b in blocks:
        if b.x == x and b.y == y:
            return

    blocks.append(Blocks(x,y,tile,tile))

def remove_block(x,y):
    print("Trying to delete block")
    for b in blocks:
        if b.x == x and b.y == y:
            blocks.remove(b)
            break
# MAINLOOP --------------------------------------------------
def mainloop():
    run = True
    while run:
        screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                print("Klick", event.pos, event.button)
                mouse_x, mouse_y = event.pos 
                grid_x = mouse_x // tile
                grid_y = mouse_y // tile

                bx = grid_x * tile 
                by = grid_y * tile 

                if 0 <= grid_x < cols and 0 <= grid_y < rows:
                    if event.button == 3:
                        add_block(bx,by)
                    elif event.button == 1:
                        remove_block(bx,by)
        pg.draw.rect(screen, "green", player1.hitbox)
        player1.movement()
        player1.gravity()
        for b in blocks:
            pg.draw.rect(screen, 'grey', b.blockHB)
        pg.display.flip()
        clock.tick(fps)
    quit()

mainloop()