import pygame as pg  
pg.init()
win=pg.display.set_mode((600,355))
pg.display.set_caption("bigo")

walkleft=[pg.image.load("tile117.png"),pg.image.load("tile118.png"),pg.image.load("tile119.png"),pg.image.load("tile120.png"),pg.image.load("tile121.png"),pg.image.load("tile122.png"),pg.image.load("tile123.png"),pg.image.load("tile124.png"),pg.image.load("tile125.png")]
walkright=[pg.image.load("tile143.png"),pg.image.load("tile144.png"),pg.image.load("tile145.png"),pg.image.load("tile146.png"),pg.image.load("tile147.png"),pg.image.load("tile148.png"),pg.image.load("tile149.png"),pg.image.load("tile150.png"),pg.image.load("tile151.png")]
bg=pg.image.load("bg.png")
char=pg.image.load("tile032.png")

clock=pg.time.Clock()

x=int(50)
y=int(290)
width=64
height=64
vel=5
isjump=False
jumpcou=9
left,right=False,False
walkcount=0


def redraw():
    global walkcount
    win.blit(bg,(0,0))    
    if walkcount+1>=27:
        walkcount=0
    if left:
        win.blit(walkleft[walkcount//3],(int(x),int(y)))
        walkcount+=1
    elif right:
        win.blit(walkright[walkcount//3],(int(x),int(y)))
        walkcount+=1
    else:
        win.blit(char,(int(x),int(y)))
        
    pg.display.update()


run=True
while run:
    clock.tick(27)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False

    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT] and x>vel:
        x-=vel
        left=True
        right=False
    elif keys[pg.K_RIGHT] and x<600-width-vel:
        x+=vel
        left=False
        right=True
    else:
        left=False
        right=False
        walkcount=0
    if not(isjump):
        if keys[pg.K_SPACE]:
            isjump = True
            left=False
            right=False
            walkcount=0
    else:
        if jumpcou >= -9:
            neg=1
            if jumpcou<0:
                neg=-1
            y -= (jumpcou**2)*0.5*neg
            jumpcou -= 1
        else:
            isjump=False
            jumpcou=9
    redraw()



pg.quit()
