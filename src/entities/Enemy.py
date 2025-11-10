import pygame as pg
import math
import random



class Enemy (pg.sprite.Sprite):
    def __init__(self, groups="enemy"):
        super().__init__()
        images = ["assets/images/Zombie1.png","assets/images/Zombie2.png","assets/images/Zombie3.png"]
        self.original_image = pg.image.load(random.choice(images)).convert_alpha()
        self.size = 75
        self.image = pg.transform.scale(self.original_image, (self.size, self.size))
        self.pos = pg.Vector2(300,300)
    
        self.rect = self.image.get_rect(center=self.pos)
        
        self.speed = 25
        self.hp = 4
        self.dmg = 1

        

    def spawn(self, player_pos):
        angle = random.randint(0,359)
        angle_to_rad = angle * math.pi / 180.0

        spawn_x = math.cos(angle_to_rad)
        spawn_y = math.sin(angle_to_rad)

        spawn_close = 350
        spawn_far = 500
        distance = random.randint(spawn_close, spawn_far)

        self.pos = player_pos + pg.Vector2(distance*spawn_x, distance*spawn_y)


    def update(self, delta, player_pos):        
        direction = (player_pos - self.pos).normalize() 
        if direction.length() != 0:
            direction = direction.normalize()
            self.pos += direction*self.speed*delta
            self.rect.center = self.pos