# Example file showing a circle moving on screen
import pygame as pg
from config import HEIGHT, WIDTH, FPS, MOVEMENT_SPEED, PLAYER_SIZE

file = "assets/sounds/soundtrack.mp3"
# pg setup
pg.init()
pg.mixer.init()

pg.mixer.music.load(file)

pg.mixer.music.play()

screen = pg.display.set_mode((HEIGHT, WIDTH))
clock = pg.time.Clock()
running = True

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# bullet inställningar
bullet_color = (255, 0, 0)
bullet_speed = 7
bullets = []

# bullet autoskjut timing
shoot_delay = 300  # millisekunder mellan skott
last_shot_time = pg.time.get_ticks()


while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")

    pg.draw.circle(screen, "yellow", player_pos, PLAYER_SIZE)

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and player_pos.y > (PLAYER_SIZE):
        player_pos.y -= 300 * dt
    if keys[pg.K_s] and player_pos.y < screen.get_height()-(PLAYER_SIZE):
        player_pos.y += 300 * dt
    if keys[pg.K_a] and player_pos.x > (PLAYER_SIZE):
        player_pos.x -= 300 * dt
    if keys[pg.K_d] and player_pos.x < screen.get_width()-(PLAYER_SIZE):
        player_pos.x += 300 * dt

    #auto skjut

    current_time = pg.time.get_ticks()

    if current_time - last_shot_time >= shoot_delay:

        bullet=pg.Rect(player_pos.x - 3, player_pos.y - 40, 6, 12)

        bullets.append(bullet)

        last_shot_time = current_time

        #flytta bullets
    for bullet in bullets[:]:

        bullet.y -= bullet_speed

        if bullet.bottom < 0:

            bullets.remove(bullet)
    for bullet in bullets:

                pg.draw.rect(screen, bullet_color, bullet)


    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pg.quit()

#Hejsan
#hej
