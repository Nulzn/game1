# Example file showing a circle moving on screen
import pygame as pg
import pygame_gui as pgg # pip3 install pygame_gui
from config import HEIGHT, WIDTH, FPS, MOVEMENT_SPEED, PLAYER_SIZE, GAME_SOUNDTRACK
from utils.Sound import GetSoundById
### ENTITIES ###
from entities.Player import Player
from entities.Enemy import Enemy
from entities.Boss import Boss

file = "assets/sounds/soundtrack.mp3"
file = "assets/sounds/soundtrack2.mp3"
# pg setup
pg.init()
pg.mixer.init()

### MUSIC SETUP ###
pg.mixer.music.load(GetSoundById(GAME_SOUNDTRACK))
pg.mixer.music.set_volume(.015)

#pg.mixer.music.play()
# pg.mixer.music.play()

level1 = "src/scenes/background.png"

background = pg.image.load(level1)

screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()
running = True

#Create sprite classes
all_sprites = pg.sprite.Group()
bullet_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()

#Create player
player = Player (WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)

#Spawn enemies (5)
for _ in range (5):                                             
    enemy = Enemy()
    enemy.spawn(player.pos)
    enemy_group.add(enemy)
    all_sprites.add(enemy)



while running:
    dt = clock.tick(FPS) / 1000
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0,0))

    #Player movement
    keys = pg.key.get_pressed()
    player.Move(keys)
    player.Sprint(keys)
    player.Shoot(bullet_group)

    #Update bullets
    bullet_group.update()
    enemy_group.update(dt, player.pos)


    #Check for collisions
    hits_player = pg.sprite.spritecollide(player, enemy_group, False)               #Collision between player and enemy
    if hits_player:
        player.health -= 1

    if player.health <= 0:
        running = False

    hits_enemy = pg.sprite.groupcollide(bullet_group, enemy_group, True, False)     #Collision between bullet and enemy
    for bullets, enemies in hits_enemy.items():
        for enemy in enemies:
            enemy.hp -= 1
            if enemy.hp <= 0:
                enemy.kill()

    #Draw 
    all_sprites.draw(screen)
    bullet_group.draw(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pg.quit()
