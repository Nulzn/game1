import pygame as pg
from config import HEIGHT, WIDTH, FPS

pg.init()
screen = pg.display.set_mode((HEIGHT, WIDTH))
clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("lightblue") #Gör skärmen ljusblå

    pg.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pg.quit()