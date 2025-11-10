import json
import pygame as pg
import pygame_gui as pgg
from config import HEIGHT, WIDTH, FPS, GAME_SOUNDTRACK
from utils.Sound import GetSoundById

### ENTITIES ###
from entities.Player import Player
from entities.Enemy import Enemy
from entities.Boss import Boss


### PYGAME SETUP ###
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))


### MUSIC SETUP ###
pg.mixer.music.load(GetSoundById(GAME_SOUNDTRACK))
pg.mixer.music.set_volume(.015)

pg.mixer.music.play()

##### GUI Setup######
with open("src/label.json", "r") as f:
    theme = json.load(f)

ui_manager = pgg.UIManager((WIDTH, HEIGHT), theme_path=theme)


level1 = "src/scenes/background.png"

background = pg.image.load(level1)

player_is_dead = False

clock = pg.time.Clock()
running = True


enemies_killed = 0
boss_killed = 0
score = 0

### SPRITE CLASSES ###
all_sprites = pg.sprite.Group()
bullet_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
boss_group = pg.sprite.Group()

### PLAYER ###
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)


def updateScore():
    return f"{"0"*(6-len(list(str(score))))}{score}" # Updates the score label

#### UI Elements ####

# Create a text-label for score
score_label = pgg.elements.UILabel(
    # Position and size, text that shows
    relative_rect=pg.Rect(850, 10, 700, 30), text=updateScore(),
    manager=ui_manager
)

# Create a health bar
score_label.text_colour = "#FFFFFF"

#Create a health bar
health_bar = pgg.elements.UIProgressBar(
    relative_rect=pg.Rect(10, 10, 200, 25),  # Position and size
    manager=ui_manager
)

health_bar.set_current_progress(player.health)  # Startvalue of healthbar

font = pg.font.Font(None, 50)
health_bar.set_current_progress(player.health)   
health_bar.bar_filled_colour = "#50F527"
health_bar.bar_unfilled_colour = "#F54927"                              #Startvalue of healthbar
health_bar.text_colour = "#FFFFFF"

### LOADING SCREEN ###
loading = True
loading_start = pg.time.get_ticks() # Start Time Of Loading

while loading:
    # Quits on user actions
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loading = False

    # Draw loading text to screen surface
    loading_image = pg.image.load("assets/images/Loading_Screen.png").convert_alpha()
    screen.blit(loading_image, (0, 0))
    pg.display.flip()

    # Simulating loading
    if pg.time.get_ticks() - loading_start > 3000:
        loading = False  # efter x sekunder, gå vidare


# Start game
print("Game is starting...")

while running:
    dt = clock.tick(FPS) / 1000 # Delta time for simulating physics

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

    health_bar.set_current_progress(player.health) # Updating healthbar

    score_label.set_text(updateScore()) # Updating score label

    ### SPAWNS ###

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

    bullet_group.update() # Updates bullets

    enemy_group.update(dt, player.pos) # Updates enemies

    boss_group.update(dt, player.pos) # Updates boss

    ### COLLISIONS ###

    # Collision between player and enemy
    hits_player = pg.sprite.spritecollide(player, enemy_group, False)
    if hits_player:
        player.health -= 1
    if player.health <= 0:
        player_is_dead = True

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

    ### DRAW SPRITES ###
    all_sprites.draw(screen)
    bullet_group.draw(screen)

    ### Update healthbar and scoreboard ###
    health_bar.set_current_progress(player.health)
    score_label.set_text(updateScore())

    ### Draw healthbar and scoreboard ###
    ui_manager.update(dt)
    ui_manager.draw_ui(screen)

    pg.display.flip() # Updates screen

    if player_is_dead:
        font = pg.font.Font(None, 50)
        
        ### GAME OVER SCREEN ###
        loading = True
        loading_start = pg.time.get_ticks() 
        loading_image = pg.image.load("assets/images/Game_over.jpeg").convert_alpha()

        while loading:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            # Draw "Game Over"-image to screen
            screen.blit(loading_image, (0, 0))
            pg.display.flip()

            if pg.time.get_ticks() - loading_start > 3000:
                loading = False

            
        pg.quit()
        exit()

pg.quit()
