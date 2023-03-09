from math import sqrt
import random
import time
from matplotlib.pyplot import show
import pygame as pg
import netObjects as nt
import genome as g
import functions as f
import util
 
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
            x = int((((1800-100)/(num_sensors)) * (num1)) + 50)
            y = 200
            neurons.update({key:(x,y)})
            num1 += 1
        elif key < 256:
            x = random.randrange(10,1790)
            y = random.randrange(300,500)
            neurons.update({key:(x,y)})
        else:
            x = int((((1800-100)/(num_actions-1)) * (num2)) + 50)
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
                text = font.render(str(round(connection.strength,2)), True, (0,0,0))
                text_rect = text.get_rect()
                text_rect.center = (xa+dx*length*arrowPos+dx*arrowLength,ya+dy*length*arrowPos+dy*arrowLength)
                display.blit(text, text_rect)
            else:
                pg.draw.circle(display, color, (xa+7,ya-7), 12, width=4)
            i += 1

        for key in neurons.keys():
            coords = neurons[key]

            if key in f.neuron_name_dict.keys():
                text = font.render(f.neuron_name_dict[key], True, (0,0,0))
            else:
                text = font.render(str(key), True, (255,255,255))
            text_rect = text.get_rect()
            text_rect.center = coords

            pg.draw.circle(display, (255,0,255), coords, 12)
            display.blit(text, text_rect)
        
        pg.display.update()

def play():
    with open("Playbacks/PYYY_380.csv") as f:
        gridsize = (128,128) 
        reader = f.readline()

        pg.init()
        display = pg.display.set_mode((800,800))
        pg.display.set_caption("Creatures Playback Display")

        time1 = time.time()
        time2 = time.time()
        while True:
            if (time2 - time1) > 0.1:
                time1 = time.time()
                reader = f.readline()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return False
                if event.type == pg.KEYDOWN:
                    keydown = pg.key.get_pressed()
                    if keydown[pg.K_1]:
                        pass

            display.fill((255,255,255))

            creatures = reader.split(",")
            del creatures[-1]

            for i in creatures:
                x = int(i) % gridsize[0]
                y = (int(i) - x)/gridsize[1]

                color = (0,0,0)
                pg.draw.circle(display, color, (x*6+16,y*6+16), 3)
            
            time2 = time.time()

            pg.display.update()

if __name__ == "__main__" and True:
    genes_string = "01830f55 8183f615 0003f615 00830931 0483b98d 8183b98d 800210f6 8102297d 8105297d 040234c6 0481a707 0281f24d 8103f24d 81039de3 83030315 05050315"
    re = g.Genome(16,genes=genes_string.split(" "))
    brain = nt.NeuralNet()
    brain.build_net(re)
    brain.optimize()
    show_brain(brain)

if __name__ == "__main__" and True:
    play()
