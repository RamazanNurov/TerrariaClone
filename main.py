from pygame import *
from variables import *
init()


def mainloop():
    run = True
    while run:
        screen.fill("black")
        for events in event.get():
            if events.type == QUIT:
                run = False
        draw.rect(screen, "green", player1.hitbox)
        player1.movement()
        display.flip()
        clock.tick(fps)
    quit()

mainloop()