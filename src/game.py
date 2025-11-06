# Example file showing a circle moving on screen
import pygame as pg
import pygame_gui as pgg  # pip3 install pygame_gui
from config import HEIGHT, WIDTH, FPS, MOVEMENT_SPEED, PLAYER_SIZE, GAME_SOUNDTRACK
from utils.Sound import GetSoundById
### ENTITIES ###
from entities.Player import Player
from entities.Enemy import Enemy
from entities.Boss import Boss
import sys


# pg setup
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))


### MUSIC SETUP ###
pg.mixer.music.load(GetSoundById(GAME_SOUNDTRACK))
pg.mixer.music.set_volume(.015)

# pg.mixer.music.play()
# pg.mixer.music.play()

##### GUI Setup######
ui_manager = pgg.UIManager((WIDTH, HEIGHT))


level1 = "src/scenes/background.png"

background = pg.image.load(level1)

clock = pg.time.Clock()
running = True


enemies_killed = 0  # Killed enemies tracker
boss_killed = 0  # Killed boss
score = 0  # Score

# Create sprite classes
all_sprites = pg.sprite.Group()
bullet_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
boss_group = pg.sprite.Group()

# Create player
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)


#### UI Elements ####
# Create a text-label for score
score_label = pgg.elements.UILabel(
    # Position and size, text that shows
    relative_rect=pg.Rect(10, 10, 150, 30), text=f"Score: {score}",
    manager=ui_manager  # Connect to manager
)

# Create a health bar
score_label.text_colour = "#FFFFFF"

#Create a health bar
health_bar = pgg.elements.UIProgressBar(
    relative_rect=pg.Rect(10, 50, 200, 25),  # Position and size
    manager=ui_manager
)

health_bar.set_current_progress(player.health)  # Startvalue of healthbar

font = pg.font.Font(None, 50)
health_bar.set_current_progress(player.health)   
health_bar.bar_filled_colour = "#50F527"
health_bar.bar_unfilled_colour = "#F54927"                              #Startvalue of healthbar
health_bar.text_colour = "#FFFFFF"

loading = True
loading_start = pg.time.get_ticks()  # när vi började ladda

while loading:
    # hantera events (så fönstret svarar)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loading = False

    # rita “Loading…”-text
    loading_image = pg.image.load("assets/images/Loading_Screen.png").convert_alpha()
    screen.blit(loading_image, (0, 0))
    pg.display.flip()

    # simulera laddning (t.ex. ladda resurser här)
    if pg.time.get_ticks() - loading_start > 2000:
        loading = False  # efter 2 sekunder, gå vidare

# fortsätt till spelet
print("Startar spelet...")

while running:
    dt = clock.tick(FPS) / 1000
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        ui_manager.process_events(event)

    screen.blit(background, (0, 0))

    # Player movement
    keys = pg.key.get_pressed()
    player.Move(keys)
    player.Sprint(keys)
    player.Shoot(bullet_group)

    #### Update healthbar ####
    health_bar.set_current_progress(player.health)

    #### Update scoreboard ####
    score_label.set_text(f"Score: {score}")

    #### Spwawns####
    # Spawn enemies
    if len(enemy_group) < 5 and enemies_killed < 5:
        enemy = Enemy()
        enemy.spawn(player.pos)
        enemy_group.add(enemy)
        all_sprites.add(enemy)

    # Spawn boss
    if enemies_killed >= 5 and len(boss_group) == 0 and boss_killed == 0:
        boss = Boss()
        boss.spawn(player.pos)
        boss_group.add(boss)
        all_sprites.add(boss)

    # Update bullets
    bullet_group.update()
    # Update enemies
    enemy_group.update(dt, player.pos)
    # Update boss
    boss_group.update(dt, player.pos)

    ###### Check for collisions ######
    # Collision between player and enemy
    hits_player = pg.sprite.spritecollide(player, enemy_group, False)
    if hits_player:
        player.health -= 1
    if player.health <= 0:
        running = False

    # Collision between bullet and enemy
    hits_enemy = pg.sprite.groupcollide(bullet_group, enemy_group, True, False)
    for bullets, enemies in hits_enemy.items():
        for enemy in enemies:
            enemy.hp -= 1
            if enemy.hp <= 0:
                enemy.kill()
                enemies_killed += 1
                score += 10

    # Collision between bullet and boss
    hits_boss = pg.sprite.groupcollide(bullet_group, boss_group, True, False)
    for bullets, boss in hits_boss.items():
        for boss in boss:
            boss.hp -= 1
            if boss.hp <= 0:
                boss.kill()
                boss_killed += 1
                score += 50

    #### Draw sprites #####
    all_sprites.draw(screen)
    bullet_group.draw(screen)

    #### Update healthbar and scoreboard ####
    health_bar.set_current_progress(player.health)
    score_label.set_text(f"Score: {score}")

    #### Draw healthbar and scoreboard #####
    ui_manager.update(dt)
    ui_manager.draw_ui(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pg.quit()
