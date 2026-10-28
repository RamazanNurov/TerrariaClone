from pygame import *
from variables import *



def mainloop():
    run = True
    while run:
        for events in event.get():
            if events.type == QUIT:
                run = False
        
        display.flip()
    quit()

mainloop()