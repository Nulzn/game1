import pygame as pg
from pygame import *
import math
import random

class Enemy (sprite.Sprite):
    def __init__(self, groups="enemy"):
        #super()._init_(groups)
    

        colors = ["red","orange","pink"]
        self.color = colors[random.randint(0, len(colors)-1)]
        self.pos = pg.Vector2(300,300)
        self.size = 30
        
        self.speed = 10

        

    def spawn(self, player_pos):
        
        p_x = player_pos.x
        p_y = player_pos.y
        
        angle = random.randint(0,359)
        angle_to_rad = angle * math.pi / 180.0


        spawn_x = math.cos(angle_to_rad)
        spawn_y = math.sin(angle_to_rad)

        spawn_close = 350
        spawn_far = 500
        distance = random.randint(spawn_close, spawn_far)


        #h = pg.Vector2(p_x,p_y)
        self.pos = player_pos + pg.Vector2(distance*spawn_x, distance*spawn_y)
        

        pass

    def update(self, delta, player_pos):        
        direction = (player_pos - self.pos).normalize() 
        self.pos += direction*self.speed*delta


    def draw(self, screen):
        pg.draw.circle(screen,"red", self.pos, self.size)
