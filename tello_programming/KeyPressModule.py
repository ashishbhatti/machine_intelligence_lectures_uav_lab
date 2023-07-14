import pygame

# creating the window
def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

# get keypresses
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()         # update pygame screen
    return ans                      # if key pressed return True
    
def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")


    
if __name__ == '__main__':
    init()
    # Upon running the window pops up and closes.
    # In the final application we would want it to stay open.

    while True:
        main()