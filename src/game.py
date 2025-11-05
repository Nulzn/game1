# Example file showing a circle moving on screen
import pygame as pg
import pygame_gui as pgg
from config import HEIGHT, WIDTH, FPS, MOVEMENT_SPEED, PLAYER_SIZE, GAME_SOUNDTRACK
from utils.Sound import GetSoundById

### ENTITIES ###
from entities.Player import Player
from entities.Enemy import Enemy1, Enemy2
from entities.Boss import Boss

### GUI ###
from gui.Label import Label

### SCENES ###
level_1 = "src/scenes/background.png"

### PYGAME SETUP ###
pg.init()
pg.mixer.init()

### MUSIC SETUP ###
pg.mixer.music.load(GetSoundById(GAME_SOUNDTRACK))
pg.mixer.music.set_volume(.025)

pg.mixer.music.play()


screen = pg.display.set_mode((HEIGHT, WIDTH))
pg.display.set_caption('Game V1')

background = pg.image.load(level_1)
manager = pgg.UIManager((HEIGHT, WIDTH))
score = Label("000000", pg.Vector2(20, 20), screen)


clock = pg.time.Clock()
running = True

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2) # Player start position

<<<<<<< HEAD
# BULLET SETTINGS
bullet_color = (255, 0, 0)
bullet_speed = 7
bullets = []

# Bullet autoskjut timing
shoot_delay = 300  # Shoot Delay (Milliseconds)
=======
# bullet inställningar
bullet_color = (255, 50, 50)
bullet_radius = 6.  # storlek på bullet
bullet_speed = 400  # pixels per second
bullets = []

# bullet  timing
shoot_delay = 400  # millisekunder mellan skott
>>>>>>> 3de907650f990fcefd008dd5c8e90e6332a02205
last_shot_time = pg.time.get_ticks()
last_move_direction = pg.Vector2(0, -1)  

dt = 0 # Delta Time

score = 0


while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        manager.process_events(event)
    
    manager.update(dt)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    # Fill the screen with a color to wipe away anything from last frame
    #screen.fill("lightblue")

    pg.draw.circle(screen, "yellow", player_pos, PLAYER_SIZE)

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and player_pos.y > (PLAYER_SIZE):
        player_pos.y -= MOVEMENT_SPEED * dt
        score += 10
    if keys[pg.K_s] and player_pos.y < screen.get_height()-(PLAYER_SIZE):
        player_pos.y += MOVEMENT_SPEED * dt
    if keys[pg.K_a] and player_pos.x > (PLAYER_SIZE):
        player_pos.x -= MOVEMENT_SPEED * dt
    if keys[pg.K_d] and player_pos.x < screen.get_width()-(PLAYER_SIZE):
<<<<<<< HEAD
        player_pos.x += MOVEMENT_SPEED * dt

    # Automatic Shooting
=======
        player_pos.x += 300 * dt

    #skjut beroende på rörelse
>>>>>>> 3de907650f990fcefd008dd5c8e90e6332a02205
    current_time = pg.time.get_ticks()

    # få rörelse riktning
    movement = pg.Vector2(0, 0)
    if keys[pg.K_w]: movement.y = -1
    if keys[pg.K_s]: movement.y = 1
    if keys[pg.K_a]: movement.x = -1
    if keys[pg.K_d]: movement.x = 1

    # uppdatera senaste rörelseriktning
    if movement.length() != 0:
        movement = movement.normalize()
        last_move_direction = movement

    # skjut om last_shot_time är högre än shoot_delay
    if current_time - last_shot_time >= shoot_delay:
        bullet_pos = player_pos.copy()
        bullets.append({"pos": bullet_pos, "dir": last_move_direction.copy()})
        last_shot_time = current_time

<<<<<<< HEAD
        #Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed

        if bullet.bottom < 0:
            bullets.remove(bullet)

    for bullet in bullets:
        pg.draw.rect(screen, bullet_color, bullet)
=======
    # uppdatera bullet positioner
    for bullet in bullets[:]:
        bullet["pos"] += bullet["dir"] * bullet_speed * dt
        if (
            bullet["pos"].x < 0 or bullet["pos"].x > WIDTH
            or bullet["pos"].y < 0 or bullet["pos"].y > HEIGHT
        ):
            bullets.remove(bullet)

    # rita bullets
    for bullet in bullets:
        pg.draw.circle(screen, bullet_color, bullet["pos"], bullet_radius)

>>>>>>> 3de907650f990fcefd008dd5c8e90e6332a02205

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pg.quit()

#Hejsan
#hej
