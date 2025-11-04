# Example file showing a circle moving on screen
import pygame as pg
from config import HEIGHT, WIDTH, FPS, MOVEMENT_SPEED
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

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")

    pg.draw.circle(screen, "yellow", player_pos, 40)

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= MOVEMENT_SPEED * dt
    if keys[pg.K_s]:
        player_pos.y += MOVEMENT_SPEED * dt
    if keys[pg.K_a]:
        player_pos.x -= MOVEMENT_SPEED * dt
    if keys[pg.K_d]:
        player_pos.x += MOVEMENT_SPEED * dt

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pg.quit()