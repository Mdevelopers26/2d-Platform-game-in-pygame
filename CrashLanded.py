import pygame as pg
import math
import random
import time

pg.init()

WIDTH = 1280 # screen dimensions
HEIGHT = 736

text = pg.font.SysFont("Corbel",25) # define and load all used fonts, sounds and images
font = pg.font.SysFont("Corbel",35)
title_font = pg.font.SysFont("Architectural",60)
bg = pg.transform.scale(pg.image.load("bg.png"),(WIDTH,HEIGHT))
bgmenu = pg.transform.scale(pg.image.load("bgmenu.jpg"),(WIDTH,HEIGHT))
enemy = pg.transform.scale(pg.image.load("spaceship.png"),(32,32))
ammo = pg.transform.scale(pg.image.load("ammo.png"),(12,12))
shield = pg.transform.scale(pg.image.load("shield.png"),(32,32))
player_width = 40
player_height = 50
player = pg.transform.scale(pg.image.load("player_char.png"),(player_width, player_height)) # lists of player character spritesheet images for animation
player_left = [pg.transform.scale(pg.image.load("L1.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L2.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L3.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L4.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L5.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L6.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L7.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L8.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L9.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L10.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L11.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("L12.png"),(player_width, player_height))]
player_right = [pg.transform.scale(pg.image.load("R1.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R2.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R3.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R4.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R5.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R6.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R7.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R8.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R9.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R10.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R11.png"),(player_width, player_height)),pg.transform.scale(pg.image.load("R12.png"),(player_width, player_height))]
bullet_sound = pg.mixer.Sound("Laser.wav")
bullet_sound.set_volume(0.1)
death_sound = pg.mixer.Sound("hurt.wav")
death_sound.set_volume(0.5)
shock_sound = pg.mixer.Sound("shock.wav")
shock_sound.set_volume(0.5)
pickup_sound = pg.mixer.Sound("pickup.wav")
pickup_sound.set_volume(0.5)
pg.mixer.music.load("BGmusic.mp3")
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)

def main_menu(): # Start menu for game
    Play = True
    while Play:
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        screen.blit(bgmenu,(0,0))
        pg.display.set_caption("Main Menu")
        text_title = title_font.render("CRASH LANDED", True, "White")
        text_rect = text_title.get_rect(center = (WIDTH/4-50,HEIGHT/8+50))
        screen.blit(text_title,text_rect)
        x,y = pg.mouse.get_pos() # gets postion of mouse cursor
        
        button_1 = Button("New Game","Black",WIDTH/5-100,HEIGHT/3+50,200,50,"White") #define and draw all buttons using button class
        button_2 = Button("How to Play","Black",WIDTH/5-100,HEIGHT/3+125,200,50,"White")
        button_3 = Button("Difficulty","Black",WIDTH/5-100,HEIGHT/3+200,200,50,"White")
        button_4 = Button("Quit","Black",WIDTH/5-100,HEIGHT/3+275,200,50,"White")
        
        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)
        button_4.draw(screen)
        
        for event in pg.event.get(): # cycle through all event types
            if event.type == pg.QUIT:
                Play = False # exit while loop
            if button_1.rect.collidepoint((x,y)): # If mouse cursor is colliding with buttons, change button text colour
                button_1 = Button("New Game","Black",WIDTH/5-100,HEIGHT/3+50,200,50,"Blue") # highlight button with different colour text
                button_1.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN: # If button is clicked...
                    pg.mixer.music.load("Background.mp3")
                    pg.mixer.music.set_volume(0.2)
                    pg.mixer.music.play(-1)
                    game_loop() # start game
            if button_2.rect.collidepoint((x,y)):
                button_2 = Button("How to Play","Black",WIDTH/5-100,HEIGHT/3+125,200,50,"Blue")
                button_2.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN:
                    how_to_play() # go to how to play menu
            if button_3.rect.collidepoint((x,y)):
                button_3 = Button("Difficulty","Black",WIDTH/5-100,HEIGHT/3+200,200,50,"Blue")
                button_3.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN:
                    difficulty_() # go to difficulty menu
            if button_4.rect.collidepoint((x,y)):
                button_4 = Button("Quit","Black",WIDTH/5-100,HEIGHT/3+275,200,50,"Blue")
                button_4.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN:
                    Play = False # exit while loop
                    
        pg.display.flip()    # update display      
    pg.quit() # If while loop ends, close game
    
class Button: # Class to define and buttons with text overlayed
    def __init__(self,text,colour,x,y,width,height,text_colour):
        self.text = text
        self.colour = colour
        self.x = x # coordinates where button will be placed
        self.y = y
        self.width = width # button dimensions
        self.height = height
        self.text_colour = text_colour
        self.rect = pg.Rect(x,y,width,height) 
        self.text_define = font.render(text,True,text_colour)
        
    def draw(self,screen):
        pg.draw.rect(screen,self.colour,self.rect)
        screen.blit(self.text_define,(self.x,self.y))
        
class Difficulty: # Class to define difficulty settings
    def __init__(self,maxVel,shotDelay,enemyScore,waveScore,enemyIncrement):
        self.maxVel = maxVel # max velocity of ememies
        self.shotDelay = shotDelay # delay between player shots
        self.enemyScore = enemyScore # score for enemy kill
        self.waveScore = waveScore # score for completing a wave
        self.enemyIncrement = enemyIncrement # number of additional enemies per round
        
class Drops(): # Class to describe and draw enemy drops
    def __init__(self, x, y, droptime):
        self.image = shield
        self.rect = self.image.get_rect() # Define rect over image
        self.rect.x = x #rect coordinates is the enemy postion when it was destroyed
        self.rect.y = y
        self.droptime = droptime # system time when drop was created
        
    def draw(self,screen):
        screen.blit(shield,self.rect) 
        
    
class Bullet(): # Class to define bullets and their motion. The mathematical formula required to allow the bullets to move in this way were sourced online, full references will be supplied in the DESCRIPTION file
    def __init__(self,x, y, speed, mx,my):
        angle = math.atan2(my-y, mx-x) # angle between player position and mouse cursor when clicked
        self.dx = math.cos(angle)*speed # change in x axis to reach target
        self.dy = math.sin(angle)*speed # change in y axis to reach target
        self.x = x # spawn coordinates of bullet
        self.y = y
        self.image = ammo
        self.rect = self.image.get_rect()
        self.speed = speed 
    
    def move(self): # updates position of bullet
        self.x += self.dx #update position of bullet with changes in x and y axes towards target
        self.y += self.dy
        self.rect.x = int(self.x) #redefine bullet rect coordindates based on new bullet position
        self.rect.y = int(self.y)
        
    def draw(self, screen):
        screen.blit(ammo,self.rect)
        

class Player(pg.sprite.Sprite): # Defines movement and attributes of player character
    def __init__(self, start_position, colour=(255, 0, 0), score=0, wave=1, numEnemies=10, deathwave=1,deathscore=0,shield=0):
        pg.sprite.Sprite.__init__(self) # gets all attributes and methods of the special sprite class to load images.
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.x = start_position[0]
        self.rect.y = start_position[1]
        self.jump = False
        self.left = False # Booleans to track when moving left or right, for animation, and when jumping
        self.right = False
        self.vel_index = 0
        self.score = score # Current score during game
        self.wave = wave # current wave during game
        self.numEnemies = numEnemies # number of enemies spawned in a given wave
        self.deathwave = deathwave # wave player was in at time of death
        self.deathscore = deathscore # final score after death
        self.shield = shield # amount of shield held by player
        self.count = 0 # count to track iterations through animation cycle (This count method was inspired by an online example, which is fully referenced in the DESCRIPTION file)


    def move(self):
        self.move_x = 0
        self.move_y = 10  # Set 10 for gravity

        keys = pg.key.get_pressed()  # get list of all keys that are down at a particular time

        if keys[pg.K_a]:
            self.left = True # moving left
            self.right = False
            self.count += 1 # iterate count
            if self.rect.left > 0:  # stops falling off left side of screen
                self.move_x = -3
            else:
                self.move_x = 0
        elif keys[pg.K_d]:
            self.left = False
            self.right = True # moving right
            self.count += 1
            if self.rect.right < WIDTH:  # stops falling off right side of screen
                self.move_x = 3
            else:
                self.move_x = 0 
        else:
            self.count = 0 # if stationary, reset count to reset animation cycle
            self.right = False
            self.left = False
                
        if self.count >= 36: # 3 times number of sprite images per list, so each image is displayed for 3 frames
            self.count = 0

        if keys[pg.K_w] and not self.jump:# if up key is pressed and we are not jumping AND ON PLATFORM
            for ledge in environment:
                if self.rect.midbottom[1] == ledge.rect.y and ledge.rect.x - 40 <= self.rect.x <= ledge.rect.x + ledge.width:
                    self.jump = True
                    self.vel_index = 0

        if self.jump:
            vel_list = list(i for i in range(-15, 16))
            if self.vel_index == len(vel_list):  # or collision with platform
                self.jump = False  # change false breaker here to platform
            if self.vel_index < len(vel_list):
                self.move_y = vel_list[self.vel_index]
                self.vel_index += 1

        self.rect.x += self.move_x  # finally update player rect position for both x and y
        self.rect.y += self.move_y

        collision = pg.sprite.spritecollide(self, environment, False)
        if collision and self.move_y > 0:  # if falling down, stop on top of platform
            self.rect.bottom = collision[0].rect.top
        elif collision and self.move_y < 0:  # if jumping up, stop at bottom of platform
            self.rect.top = collision[0].rect.bottom
            
    def draw(self,screen):
        if self.left:
            screen.blit(player_left[self.count//3],self.rect) # when moving left, iterate through and display animationm images, 3 frames per image
        elif self.right:
            screen.blit(player_right[self.count//3],self.rect) # same for right
        else:
            screen.blit(player,self.rect) # when not moving left or right, display default player image



class Enemy(pg.sprite.Sprite): # Defines enemies and their movement
    def __init__(self,x,y,velocity=1):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.x = x # enemy spawn location
        self.rect.y = y
        self.velocity = velocity # velocity at which enemies move toward player
    
    def move(self,playerX,playerY): # takes current coordinates of player as arguments
        dx = playerX - self.rect.x # length between enemy and player in x axis
        dy = playerY - self.rect.y # length between enemy and player in y axis
            #Enemy moves in horizontally or vertically
        if abs(dx) > abs(dy): # if enemy is further away from player in x axis than y axis...
             if dx > 0: # if player is on the right of enemy...
                 self.rect.x += self.velocity # move right 
             else: # if player is on left...
                 self.rect.x -= self.velocity # move left
        else: # enemy is further away in y axis
            if dy > 0: # if player is below enemy
                 self.rect.y += self.velocity # move down
            else: # If player is above enemy
                self.rect.y -= self.velocity # move up
                
    def draw(self, screen):
        screen.blit(enemy,self.rect)
                

class Ledge(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        IMAGE = pg.transform.scale(pg.image.load("ledge.jpg"), (width, height)) # change image file here
        pg.sprite.Sprite.__init__(self)
        self.image = IMAGE
        self.rect = IMAGE.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height


# GROUP CREATION
environment = pg.sprite.Group()

# PLAYERS
player1 = Player((WIDTH//2, HEIGHT - 40)) # create player character as object of Player class

# LEDGES
LEDGE_HEIGHT = 20   # Thickness of all ledges pre-defined 
l1 = Ledge(0, HEIGHT-LEDGE_HEIGHT, WIDTH, LEDGE_HEIGHT) #create ledge objects
l2 = Ledge(0, HEIGHT//1.2, WIDTH//4, LEDGE_HEIGHT)
l3 = Ledge(WIDTH//2, HEIGHT//1.2, WIDTH - WIDTH//2, LEDGE_HEIGHT)
l4 = Ledge(0, HEIGHT//1.7, WIDTH//3, LEDGE_HEIGHT)
l5 = Ledge(WIDTH//11, HEIGHT//3, WIDTH//2, LEDGE_HEIGHT)
l6 = Ledge(WIDTH//2, HEIGHT//1.7, WIDTH//4, LEDGE_HEIGHT)
l7 = Ledge(WIDTH//1.6, HEIGHT//2.2, WIDTH, LEDGE_HEIGHT)
l8 = Ledge(WIDTH//2.8, HEIGHT//1.4, WIDTH//11, LEDGE_HEIGHT)
# ADD TO GROUPS FOR .DRAW FUNCTION

environment.add(l1)
environment.add(l2)
environment.add(l3)
environment.add(l4)
environment.add(l5)
environment.add(l6)
environment.add(l7)
environment.add(l8)

difficulty = Difficulty(2.0,0.4,10,100,2) # default difficulty initialised


def how_to_play(): # menu to display instructions on how to play the game
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("How to Play")
    
    Play = True
    while Play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Play = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    main_menu()
                    
        text1 = title_font.render("CONTROLS", True, "White")
        rect1 = text1.get_rect(center = (WIDTH/4-50,HEIGHT/8+50))
        text2 = font.render("A: Move Left", True, "White")
        rect2 = text2.get_rect(center = (WIDTH/4-50,HEIGHT/8+200))
        text3 = font.render("D: Move Right", True, "White")
        rect3 = text3.get_rect(center = (WIDTH/4-50,HEIGHT/8+250))
        text4 = font.render("W: Jump", True, "White")
        rect4 = text4.get_rect(center = (WIDTH/4-50,HEIGHT/8+300))
        text5 = font.render("Left Mouse Button: Shoot", True, "White")
        rect5 = text5.get_rect(center = (WIDTH/4-50,HEIGHT/8+350))
        text6 = font.render("ESCAPE: Back (Menus)", True, "White")
        rect6 = text6.get_rect(center = (WIDTH/4-50,HEIGHT/8+400))
        text7 = text.render("Pick up batteries from enemies to power your shields,", True, "White")
        rect7 = text7.get_rect(center = (WIDTH/4-50,HEIGHT/8+500))
        text8 = text.render("which allow you to negate damage", True, "White")
        rect8 = text8.get_rect(center = (WIDTH/4-50,HEIGHT/8+550))
        text9 = text.render("Objective: Survive and get the highest score possible", True, "White")
        rect9 = text9.get_rect(center = (WIDTH/4-50,HEIGHT/8+600))
        
        
        screen.blit(bgmenu,(0,0))
        screen.blit(text1,rect1)
        screen.blit(text2,rect2)
        screen.blit(text3,rect3)
        screen.blit(text4,rect4)
        screen.blit(text5,rect5)
        screen.blit(text6,rect6)
        screen.blit(text7,rect7)
        screen.blit(text8,rect8)
        screen.blit(text9,rect9)
        pg.display.flip()
    pg.quit()
    
def difficulty_(): # function to modify difficulty my changing game settings
    global difficulty
    Play = True
    while Play:
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        screen.blit(bgmenu,(0,0))
        pg.display.set_caption("Difficulty")
        x,y = pg.mouse.get_pos()
        
        button_1 = Button("Easy","Black",WIDTH/5-100,HEIGHT/3+50,200,50,"White") # 3 difficulty buttons
        button_2 = Button("Default","Black",WIDTH/5-100,HEIGHT/3+125,200,50,"White")
        button_3 = Button("Impossible","Black",WIDTH/5-100,HEIGHT/3+200,200,50,"White")
        
        
        for event in pg.event.get():      # When buttons hovered over with mouse, text changes colour, when clicked
            if event.type == pg.QUIT:     # difficulty is changed for that instance of the game
                Play = False
            if button_1.rect.collidepoint((x,y)):
                button_1 = Button("Easy","Black",WIDTH/5-100,HEIGHT/3+50,200,50,"Blue")
                button_1.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN:
                     difficulty = Difficulty(1.0,0.2,5,50,1)
                     main_menu() # when difficulty is chosen, automatically return to main menu
            if button_2.rect.collidepoint((x,y)):
                button_2 = Button("Default","Black",WIDTH/5-100,HEIGHT/3+125,200,50,"Blue")
                button_2.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN:
                    difficulty = Difficulty(2.0,0.4,10,100,2)
                    main_menu()
            if button_3.rect.collidepoint((x,y)):
                button_3 = Button("Impossible","Black",WIDTH/5-100,HEIGHT/3+200,200,50,"Blue")
                button_3.draw(screen)
                if event.type == pg.MOUSEBUTTONDOWN:
                    difficulty = Difficulty(3.0,0.6,20,200,3)
                    main_menu()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    main_menu()            
        
        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)
                    
        pg.display.flip()         
    pg.quit()
    
def deathscreen(): # screen when player dies in the game
    pg.mixer.music.load("endmusic.mp3")
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("You Died")
    Play = True
    while Play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Play = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: # return to main menu, reset music
                    pg.mixer.music.load("BGmusic.mp3")
                    pg.mixer.music.set_volume(0.1)
                    pg.mixer.music.play(-1)
                    main_menu()
                    
        deathscore_text = title_font.render(f"Your Score: {player1.deathscore}", True, "White") # display final score and wave for the previous game
        deathscore_rect = deathscore_text.get_rect(center = (WIDTH/2, HEIGHT/2))
        deathwave_text = title_font.render(f"You Were Overrun On Wave {player1.deathwave}", True, "White")
        deathwave_rect = deathwave_text.get_rect(center = (WIDTH/2,HEIGHT/2 - 200))
        command_text = title_font.render("Press ESCAPE to Continue", True, "White")
        command_rect = command_text.get_rect(center = (WIDTH/2,HEIGHT/2 + 200))
    
    
        screen.fill("Black")            
        screen.blit(deathscore_text,deathscore_rect)
        screen.blit(deathwave_text,deathwave_rect)
        screen.blit(command_text,command_rect)
        pg.display.flip()
    pg.quit()
    

def game_loop(): # main game loop, calling function starts game
    bullets = [] # empty lists initialised for bullets,enemies and drops
    enemies = []
    drops = []
    bullet_time = time.time() # initialise system time when bullet is fired
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.blit(bg,(0,0))
    pg.display.set_caption("Crash Landed")
# GAME LOOP:
    clock = pg.time.Clock()
    
    
    for i in range(player1.numEnemies): # for each enemy that must be spawned in a given wave
        x = random.randint(-100,WIDTH+100) # enemies spawn above the map in a random location and descend onto the player
        y = random.randint(-500,100)
        ranVel = random.uniform(1.0,difficulty.maxVel) # for each enemy, randomise speed between 1 and either 1,2 or 3 depending on difficulty
        enemy = Enemy(x,y,ranVel) # create enemy objects
        enemies.append(enemy) # add enemies to list
    
    Play = True # while true, game is active
    while Play:
        clock.tick(200) # FPS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Play = False
            if event.type == pg.MOUSEBUTTONDOWN: # if mouse is clicked
                if time.time() - bullet_time > float(difficulty.shotDelay): # if minimum shot delay time has elapsed
                    bullet_time = time.time() # previous shot time = current time
                    x,y = pg.mouse.get_pos()
                    bullet = Bullet(player1.rect.centerx,player1.rect.centery,5,x,y) # create bullet and add to list, bullet target is where mouse was clicked (x,y)
                    bullet_sound.play()
                    bullets.append(bullet)
                
                
        score_text = title_font.render(f"Score:{player1.score}", True, "White") # HUD elements
        score_rect = score_text.get_rect()
        wave_text = title_font.render(f"Wave: {player1.wave}", True, "White")
        wave_rect = score_text.get_rect(topleft = (WIDTH/2-150,0))
        shield_text = title_font.render(f"Shield: {player1.shield}", True, "White")
        shield_rect = shield_text.get_rect(topright = (WIDTH-50,0))
                
                
                
        
        for enemy in enemies: # update movement for bullets and enemies
            enemy.move(player1.rect.x,player1.rect.y) # enemies move towards current player position
        for bullet in bullets:
            bullet.move() 
            
        for ledge in environment: # if a bullet collides with a ledge, the bullet is destroyed (removed from list)
            for bullet in bullets:
                if ledge.rect.colliderect((bullet.rect)):
                    bullets.remove(bullet)
                
                    
        for enemy in enemies:
            if enemy.rect.collidepoint((player1.rect.x,player1.rect.y)): # if player collides with enemy and they have no shield, player dies and all player attributes are reset
                if player1.shield == 0:
                    player1.deathscore = player1.score # final score and wave saved before reset
                    player1.deathwave = player1.wave
                    player1.numEnemies = 10 # default settings at start of game reapplied
                    player1.wave = 1
                    player1.score = 0
                    player1.shield = 0
                    player1.rect.x = WIDTH/2
                    player1.rect.y = HEIGHT - 40
                    death_sound.play()
                    pg.mixer.music.stop()
                    deathscreen() # go to deathscreen
                else:
                     player1.shield -= 100 # if player hit, but has a shield, shield is lost and enemy dies
                     shock_sound.play()
                     enemies.remove(enemy)
            
            for bullet in bullets:
                if enemy.rect.colliderect((bullet.rect)):
                    enemies.remove(enemy)
                    bullets.remove(bullet) # if bullet collides with enemy, delete bullet and enemy and increase player score
                    player1.score += difficulty.enemyScore
                    ifDrop = random.randint(0,99)
                    if ifDrop >= 0 and ifDrop <= 4: # 5% chance for dead enemy to spawn a shield drop, time when item is dropped is recorded
                        droptime = time.time()
                        drop = Drops(enemy.rect.x,enemy.rect.y,droptime)
                        drops.append(drop)
                        
        for drop in drops:
            if drop.rect.colliderect(player1.rect):
                pickup_sound.play()
                if player1.shield < 200: # if player collides with shield, shield is increased by 100 and drop is deleted              
                    drops.remove(drop)
                    player1.shield += 100
                else:
                    drops.remove(drop) # player can hold maximum of 200 shield, further pickups increase score
                    player1.score += 50
            if time.time() - drop.droptime > 10: # if a drop has not been picked up in 10 seconds, remove from map
                drops.remove(drop)
            
                        
                    
        if enemies == []: # When all enemies for the wave have been killed, increment additional enemies, wave number and score. Call game loop recursively to respawn enemies on a higher round
            player1.numEnemies += difficulty.enemyIncrement 
            player1.wave += 1
            player1.score += difficulty.waveScore
            game_loop()
                    
        screen.blit(bg,(0,0))  
        environment.draw(screen)
        for enemy in enemies: # draw all game elements
            enemy.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for drop in drops:
            drop.draw(screen)
        screen.blit(score_text,score_rect)
        screen.blit(wave_text,wave_rect)
        screen.blit(shield_text,shield_rect)
        player1.move() # activate player movement
        player1.draw(screen)
        pg.display.flip()
    pg.quit()

main_menu() # call the main menu
