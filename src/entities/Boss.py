import pygame as pg
import math
import random

class Boss (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image = pg.image.load("assets/images/Boss1.png").convert_alpha()
        self.size = 200
        self.image = pg.transform.scale(image, (self.size, self.size))

        self.pos = pg.Vector2(300, 300)

        self.rect = self.image.get_rect(center=(self.pos))

        self.speed = 10
        self.hp = 20
        self.dmg = 1


    def spawn (self, player_pos):
        angle = random.randint(0,359)
        angle_to_rad = angle * math.pi / 180.0


        spawn_x = math.cos(angle_to_rad)
        spawn_y = math.sin(angle_to_rad)

        spawn_close = 350
        spawn_far = 500
        distance = random.randint(spawn_close, spawn_far)

        self.pos = player_pos + pg.Vector2(distance*spawn_x, distance*spawn_y)
        self.speed = 25

    def update (self, delta, player_pos):
        direction = (player_pos - self.pos).normalize() 
        if direction.length() != 0:
            direction = direction.normalize()
            self.pos += direction*self.speed*delta
            self.rect.center = self.pos
            self.speed = 25


        
        