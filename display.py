import random
import pygame as pg
import netObjects as nt

def run(brain, max_input = 128, max_output = 128, max_inter = 128):
    pg.init()
    display = pg.display.set_mode((1800,800))
    pg.display.set_caption("Net Display")

    inter = {}
    for index in range(max_inter):
        x = random.randrange(10,1790)
        y = random.randrange(300,500)

        inter.update({index+128:(x,y)})
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False

        display.fill((255,255,255))
        font = pg.font.Font('freesansbold.ttf', 10)

        for index in range(max_input):
            x = int((((1800-20)/128) * index) + 10)
            if index%10 == 9:
                color = (0,0,255)
            else:
                color = (255,0,0)
            pg.draw.circle(display, color, (x,200), 5)

        for index in range(max_output):
            x = int((((1800-20)/128) * index) + 10)
            if index%10 == 9:
                color = (0,0,255)
            else:
                color = (0,255,0)
            pg.draw.circle(display, color, (x,600), 5)

        for connection in brain.connections:
            adr_a = connection.adr_a
            adr_b = connection.adr_b
            if adr_b < 128:
                adr_b += 256
                xb = int((((1800-20)/128) * (adr_b%128)) + 10)
                yb = 600
            else:
                xb, yb = inter.get(adr_b)

            if adr_a < 128:
                xa = int((((1800-20)/128) * (adr_a%128)) + 10)
                ya = 200
            else:
                xa, ya = inter.get(adr_a)

            pg.draw.line(display, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (xa,ya), (xb,yb), width=5)

        for index in range(128, max_inter+128):
            coords = inter.get(index)

            text = font.render(str(index), True, (100,100,100))
            text_rect = text.get_rect()
            text_rect.center = coords

            pg.draw.circle(display, (255,0,255), coords, 5)
            display.blit(text, text_rect)
        
        pg.display.update()