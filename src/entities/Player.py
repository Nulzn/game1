import pygame
from config import WIDTH, HEIGTH

class Player (pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)      #Creata a circle that represents the character
        
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius)       #Draw a circle on the surface of the character (red)

        self.rect = self.image.get_rect(center = (x,y))     #Rect for collision and posision

        self.health = 3                                     #Player health
        self.speed = 4                                      #Movementspeed

        self.last_shot = 0                                  #Time since last shot (to relagate shotspeeed)
        self.shoot_delay = 300                              #Time between shots, in ms

        self.direction = pygame.Vector2(0, -1)              #Default direction, up
    

    def Move(self, keys):
        movement = pygame.Vector2(0,0)

        if keys [pygame.K_a]:
            movement.x = -1                                  #Player move left, when pressing a

        if keys [pygame.K_d]:
            movement.x = 1                                   #Player move right, when pressing d

        if keys [pygame.K_w]:
            movement.y = -1                                  #Player move up, when pressing w

        if keys [pygame.K_s]:
            movement.y = 1                                   #Player move down, when pressing s

        #When player moves, update the direction
        if movement.length() > 0:
            movement = movement.normalize()
            self.direction = movement

        self.rect.x += movement.x * self.speed
        self.rect.y += movement.y * self.speed


        #Keep character within the window
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.x.WIDTH))
        self.rect.y = max(0, min(self.rect.y, HEIGTH - self.rect.y.HEIGTH))

    
    def Sprint(self, keys):
        if keys [pygame.K_LSHIFT]:                             #When pressing leftshift, player sprints. Gets more movementspeed
            self.speed = 6
        else: 
            self.speed = 4

        

    def Shoot(self, bullet_group):
        current_time = pygame.time.get_ticks()                  #Time since gamestart

        #A shot is fired if the time since last shot is greater than the delay.
        if current_time - self.last_shot >= self.shoot_delay:
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction)       #Create new bullet
            bullet_group.add(bullet)                                                    #Add bullet to the spritegroup
            self.last_shot = current_time                                               #Save when the lastest shot fired



#Class for the bullets
class Bullet (pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()

        self.image = pygame.Surface((8,8))                      #Create a rect that represents the bullet
        self.image.fill ((255, 0, 0))                           #Colour the bullet red

        self.rect = self.image.get_rect(center = (x,y))         #Keep the rect on the screen



        self.speed = 8                                          #Bulletspeed
        self.direction = direction                              #Save which direction the bullet will travel in

    def update (self):
        self.rect.x += self.direction.x * self.speed            #Move the bullet in the direction of the playermovement
        self.rect.y += self.direction.y * self.speed

        if (self.rect.x < 0 or self.rect.x > WIDTH) or (self.rect.y < 0 or self.rect.y > HEIGTH):
            self.kill()                                         #If the bullet leaves the screen, remove it





    