# Example file showing a circle moving on screen
import pygame as pg
import pygame_gui as pgg # pip3 install pygame_gui
from config import HEIGHT, WIDTH, FPS, MOVEMENT_SPEED, PLAYER_SIZE, GAME_SOUNDTRACK
from utils.Sound import GetSoundById
### ENTITIES ###
from entities.Player import Player
from entities.Enemy import Enemy
from entities.Boss import Boss

from entities.Enemy import Enemy

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

clock = pg.time.Clock()
running = True

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#enemy_pos = pg.Vector2(PLAYER_SIZE*10, PLAYER_SIZE*10)
# enemy_pos = pg.Vector2(PLAYER_SIZE*10, PLAYER_SIZE*10)
enemies = []


# bullet inställningar
bullet_color = (255, 50, 50)
bullet_radius = 6   # storlek på bullet
bullet_speed = 400  # pixels per second
bullets = []

# bullet  timing
shoot_delay = 400  # millisekunder mellan skott
last_shot_time = pg.time.get_ticks()
last_move_direction = pg.Vector2(0, -1)  
last_move_direction = pg.Vector2(0, -1)

dt = 0 # Delta Time

score = 0
enemies_killed = 0
wave_size = 2
enemies_left_in_wave = wave_size
enemy_move_speed = 25 

def spawn_enemy(enemy_move_speed=25):

    enemy = Enemy()
    enemy.spawn(player_pos, enemy_move_speed)
    enemies.append(enemy)

def next_wave():
    
    pass

#def main():
    
# def main():
for _ in range(5):
    spawn_enemy()

while running:
    dt = clock.tick(FPS) / 1000
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        manager.process_events(event)
    
    manager.update(dt)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    
    #direction = player_pos - enemy_pos
    #if direction.length() > 0:
    # direction = player_pos - enemy_pos
    # if direction.length() > 0:
    #     direction = direction.normalize()
    #enemy_pos += direction * 200
    # enemy_pos += direction * 200

    if enemies_left_in_wave <= 0:
        # Spawn new Wave 
        wave_size += 2
        enemy_move_speed += 20
        enemies_left_in_wave = wave_size
        for _ in range(wave_size):
            spawn_enemy(enemy_move_speed)
    
    #enemy = pg.draw.circle(screen,"red",enemy_pos, 30)
    # enemy = pg.draw.circle(screen,"red",enemy_pos, 30)
    keys = pg.key.get_pressed()

    if keys[pg.K_w] and player_pos.y > (PLAYER_SIZE):
        player_pos.y -= MOVEMENT_SPEED * dt
    if keys[pg.K_s] and player_pos.y < screen.get_height()-(PLAYER_SIZE):
        player_pos.y += MOVEMENT_SPEED * dt
    if keys[pg.K_a] and player_pos.x > (PLAYER_SIZE):
        player_pos.x -= MOVEMENT_SPEED * dt
    if keys[pg.K_d] and player_pos.x < screen.get_width()-(PLAYER_SIZE):
        player_pos.x += MOVEMENT_SPEED * dt

    for enemy in enemies:
        enemy.update(dt,player_pos)
    
    #auto skjut
        enemy.update(dt, player_pos)

    # auto skjut

        # få rörelse riktning
    movement = pg.Vector2(0, 0)

    # uppdatera senaste rörelseriktning
    if movement.length() != 0:
        movement = movement.normalize()
        last_move_direction = movement

    current_time = pg.time.get_ticks()

    if current_time - last_shot_time >= shoot_delay:
        bullet_pos = player_pos.copy()
        bullets.append({"pos": bullet_pos, "dir": last_move_direction.copy()})
        last_shot_time = current_time

    # uppdatera bullet positioner
    for bullet in bullets[:]:
        bullet["pos"] += bullet["dir"] * bullet_speed * dt
        if (
            bullet["pos"].x < 0 or bullet["pos"].x > screen.get_width()
            or bullet["pos"].y < 0 or bullet["pos"].y > screen.get_height()
        ):
            bullets.remove(bullet)

    ## Collisions:

    # Has enemy collided with player ?
    #if player_not_immune: # to be one-tapped
    for enemy in enemies:
        if enemy.check_collision_with(player_pos, PLAYER_SIZE):
            print("big dmg to player", enemy.pos)
                # Maybe add knockback or immun frames

    # Has bullet collided with enemy ?
    for enemy in enemies:
        for bullet in bullets[:]:
            if enemy.check_collision_with(bullet["pos"], bullet_radius):
                if enemy.deal_dmg(2):
                    enemies.remove(enemy)
                    enemies_killed += 1
                    enemies_left_in_wave -= 1
                bullets.remove(bullet)


    pg.draw.circle(screen, "yellow", player_pos, PLAYER_SIZE)

    # rita bullets
    for bullet in bullets:

    ###
    # OMEGA DRAW STEP
    ###

    player = pg.draw.circle(screen, "yellow", player_pos, PLAYER_SIZE)

    for enemy in enemies:
        enemy.draw(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pg.quit()

#main()# main()
