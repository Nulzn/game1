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
bullet_color = (255, 50, 50)
bullet_radius = 6.  # storlek på bullet
bullet_speed = 400  # pixels per second
bullets = []

# bullet  timing
shoot_delay = 400  # millisekunder mellan skott
last_shot_time = pg.time.get_ticks()
last_move_direction = pg.Vector2(0, -1)  


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

    #skjut beroende på rörelse
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


    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pg.quit()

#Hejsan
#hej
