import pygame as pg
import netObjects as nt

def run(brain):
    pg.init()
    display = pg.display.set_mode((1300,800))
    pg.display.set_caption("Net Display")
    
    while True:
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False

        display.fill((255,255,255))

        for index in range(128):
            x = int((((1300-20)/128) * index) + 10)
            pg.draw.circle(display, (255,0,0), (x,200), 4)

        for index in range(128):
            x = int((((1300-20)/128) * index) + 10)
            pg.draw.circle(display, (0,255,0), (x,600), 4)

        for connection in brain.connections:
            adr_a = connection.adr_a
            adr_b = connection.adr_b
            if adr_b < 128:
                adr_b += 256

            xa = int((((1300-20)/128) * (adr_a%128)) + 10)
            ya = int((adr_a//128)*200)+200
            xb = int((((1300-20)/128) * (adr_b%128)) + 10)
            yb = int((adr_b//128)*200)+200

            pg.draw.line(display, (0,0,0), (xa,ya), (xb,yb))
        
        pg.display.update()