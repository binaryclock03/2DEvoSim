from math import sqrt
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

    conn = []
    for index in range(256):
        color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        conn.append(color)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            if event.type == pg.KEYDOWN:
                keydown = pg.key.get_pressed()
                if keydown[pg.K_1]:
                    inter = {}
                    for index in range(max_inter):
                        x = random.randrange(10,1790)
                        y = random.randrange(300,500)
                        inter.update({index+128:(x,y)})
                if keydown[pg.K_2]:
                    conn = []
                    for index in range(256):
                        color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                        conn.append(color)

        display.fill((255,255,255))
        font = pg.font.Font('freesansbold.ttf', 10)

        for index in range(max_input):
            x = int((((1800-20)/max_input) * index) + 10)
            if index%10 == 9:
                color = (0,0,255)
            else:
                color = (255,0,0)
            pg.draw.circle(display, color, (x,200), 5)

        for index in range(max_output):
            x = int((((1800-20)/max_output) * index) + 10)
            if index%10 == 9:
                color = (0,0,255)
            else:
                color = (0,255,0)
            pg.draw.circle(display, color, (x,600), 5)

        i = 0
        for connection in brain.connections:
            adr_a = connection.adr_a
            adr_b = connection.adr_b
            if adr_b < 128:
                adr_b += 256
                xb = int((((1800-20)/max_input) * (adr_b%128)) + 10)
                yb = 600
            else:
                xb, yb = inter.get(adr_b)

            if adr_a < 128:
                xa = int((((1800-20)/max_output) * (adr_a%128)) + 10)
                ya = 200
            else:
                xa, ya = inter.get(adr_a)

            color = conn[i]
            pg.draw.line(display, color, (xa,ya), (xb,yb), width=5)
            dx = xb-xa
            dy = yb-ya
            length = sqrt(dx**2 + dy**2)
            if length != 0:
                dx = dx/length
                dy = dy/length
                arrowPos = 0.6
                arrowWidth = 10
                arrowLength = 15
                pg.draw.polygon(display, color, [(xa+dx*length*arrowPos+dx*arrowLength,ya+dy*length*arrowPos+dy*arrowLength), (xa+dx*length*arrowPos+dy*arrowWidth,ya+dy*length*arrowPos+dx*-arrowWidth), (xa+dx*length*arrowPos+dy*-arrowWidth,ya+dy*length*arrowPos+dx*arrowWidth)])
            else:
                pg.draw.circle(display, color, (xa+7,ya-7), 12, width=4)
            i += 1

        for index in range(128, max_inter+128):
            coords = inter.get(index)

            text = font.render(str(index), True, (100,100,100))
            text_rect = text.get_rect()
            text_rect.center = coords

            pg.draw.circle(display, (255,0,255), coords, 5)
            display.blit(text, text_rect)
        
        pg.display.update()