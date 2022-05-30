from math import sqrt
import random
import pygame as pg
import netObjects as nt

def show_brain(brain):
    pg.init()
    display = pg.display.set_mode((1800,800))
    pg.display.set_caption("Net Display")

    num_sensors = 0
    num_inters = 0
    num_actions = 0
    neurons = {}

    for key in brain.neurons.keys():
        if key <128:
            num_sensors += 1
        elif key <256:
            num_inters += 1
        else:
            num_actions += 1
    
    num1 = 0
    num2 = 0
    for key in list(brain.neurons.keys()):
        if key < 128:
            x = int((((1800-40)/(num_sensors-1)) * (num1)) + 20)
            y = 200
            neurons.update({key:(x,y)})
            num1 += 1
        elif key < 256:
            x = random.randrange(10,1790)
            y = random.randrange(300,500)
            neurons.update({key:(x,y)})
        else:
            x = int((((1800-40)/(num_actions-1)) * (num2)) + 20)
            y = 600
            neurons.update({int(key):(x,y)})
            num2 += 1

    conn = []
    for index in range(256):
        color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        conn.append(color)
    
    font = pg.font.Font('freesansbold.ttf', 12)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            if event.type == pg.KEYDOWN:
                keydown = pg.key.get_pressed()
                if keydown[pg.K_1]:
                    pass
                    # inter = {}
                    # for index in range(numInters):
                    #     x = random.randrange(10,1790)
                    #     y = random.randrange(300,500)
                    #     inter.update({index+128:(x,y)})
                if keydown[pg.K_2]:
                    conn = []
                    for index in range(256):
                        color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                        conn.append(color)

        display.fill((255,255,255))

        i = 0
        for connection in brain.connections:
            adr_a = connection.adr_a
            adr_b = connection.adr_b
                
            if adr_b < 128:
                adr_b += 256

            xb, yb = neurons[adr_b]
            xa, ya = neurons[adr_a]

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

        for key in neurons.keys():
            coords = neurons[key]

            text = font.render(str(key), True, (255,255,255))
            text_rect = text.get_rect()
            text_rect.center = coords

            pg.draw.circle(display, (255,0,255), coords, 12)
            display.blit(text, text_rect)
        
        pg.display.update()

def play():
    creatures = {1:["deadbeef","deadbeef"], 2:["00000000","00000000"], 3:["ffffffff","ffffffff"]}
    grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    pg.init()
    display = pg.display.set_mode((800,800))
    pg.display.set_caption("Creatures Playback Display")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            if event.type == pg.KEYDOWN:
                keydown = pg.key.get_pressed()
                if keydown[pg.K_1]:
                    pass

        display.fill((255,255,255))
        
        for x, row in enumerate(grid):
            for y, num in enumerate(row):
                color = creatures[grid[x][y]]

                pg.draw.circle(display, (100,100,100), (x*20,y*20), 10)
        
        pg.display.update()