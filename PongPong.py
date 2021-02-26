import pygame, sys
import MainPongGame
import time
import random


pygame.init()
pygame.display.set_caption('P O N G - AV games')
clock = pygame.time.Clock()
screenw = 1280
screenh = 960
screen = pygame.display.set_mode((screenw, screenh))



# Rectangles to make it easier to manipulate and measure objects
ball = pygame.Rect(screenw/2 - 15, screenh/2 - 15, 30, 30) 
player_paddle = pygame.Rect(screenw - 20, screenh/2 - 70, 10, 140)
enemy_paddle = pygame.Rect(10, screenh/2 - 70, 10, 140)

backgroundclr = pygame.Color('grey12')
light_gray = (200, 200, 200)

# Movement variables
ball_speedx = 8
ball_speedy = 8
paddle_speed = 0
enemy_speed = 8

# Score Variables
enemy_score = 0
player_score = 0
game_text = pygame.font.Font("freesansbold.ttf", 45)
result_text = pygame.font.Font("freesansbold.ttf", 120)
enemy_win = False
player_win = False

# Click click
click = False
hard_mode = False

def reset_ball():
        ball.center = (screenw/2, screenh/2)

def introscreen():
    checker = True
    while checker == True:
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Background and Title Text
        screen.fill(backgroundclr)
        title_text = game_text.render("P O N G", False, light_gray)
        screen.blit(title_text, (538, 300))

        # Buttons
        pbutton = pygame.Rect(548, 375, 150, 50)
        pygame.draw.rect(screen, light_gray, pbutton)
        pbuttontext = game_text.render("PLAY", False, backgroundclr)
        screen.blit(pbuttontext, (560, 380))
        
        hbutton = pygame.Rect(548, 450, 150, 50)
        pygame.draw.rect(screen, light_gray, hbutton)
        hbuttontext = game_text.render("HARD", False, backgroundclr)
        screen.blit(hbuttontext, (560, 455))

        # Button Collisions
        mouse = pygame.mouse.get_pos()
        
        if pbutton.collidepoint((mouse)):
            if click:
                maingame()
                checker = False
                

        if hbutton.collidepoint((mouse)):
            if click:
                global hard_mode
                hard_mode = True
                maingame()
                checker = False

        pygame.display.flip()
        clock.tick(60)


def maingame():
    global ball_speedx, ball_speedy, paddle_speed, enemy_speed, player_score, enemy_score 
    global game_text, backgroundclr, light_gray, ball, player_paddle, enemy_paddle
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    paddle_speed += 8
                if event.key == pygame.K_UP:
                    paddle_speed -= 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    paddle_speed -= 8
                if event.key == pygame.K_UP:
                    paddle_speed += 8

        # Score Checkers
        
        
        if enemy_score == 10:
            global enemy_win
            enemy_win = True
            results_screen()
            break
        if player_score == 10:
            global player_win
            player_win = True
            results_screen()
            break

        # Animations
        ball.x += ball_speedx
        ball.y += ball_speedy
        player_paddle.y += paddle_speed

        if enemy_paddle.top < ball.y:
            
            enemy_paddle.top += enemy_speed
        if enemy_paddle.bottom > ball.y:
            
            enemy_paddle.bottom -= enemy_speed

        # Collisions
        if ball.top <= 0 or ball.bottom >= screenh: 
            ball_speedy *= -1
                    
        if ball.left <= 0:
            player_score += 1
            reset_ball()

        if ball.right >= screenw:
            enemy_score += 1
            reset_ball()

        if ball.colliderect(player_paddle) or ball.colliderect(enemy_paddle):
            ball_speedx *= -1
                    
        if player_paddle.top <= 0:
            player_paddle.top = 0
        if player_paddle.bottom >= screenh:
            player_paddle.bottom = screenh

        if enemy_paddle.top <= 0:
            enemy_paddle.top = 0
        if enemy_paddle.bottom >= screenh:
            enemy_paddle.bottom = screenh

                    
        # Background fill
        screen.fill(backgroundclr)
                    
        # Score Text
        p_text = game_text.render(f"{player_score}", False, light_gray)
        screen.blit(p_text, (660, 470))
        e_text = game_text.render(f"{enemy_score}", False, light_gray)
        screen.blit(e_text, (600, 470))
                    
        # Main game objects
        pygame.draw.rect(screen, light_gray, player_paddle)
        pygame.draw.rect(screen, light_gray, enemy_paddle)
        pygame.draw.ellipse(screen, light_gray, ball)
        pygame.draw.aaline(screen, light_gray, (screenw/2,0), (screenw/2,screenh))

        pygame.display.flip()
            # Difficulty Checker
        if hard_mode == True:
            clock.tick(120)
        else:
            clock.tick(60)


def results_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(backgroundclr)
        if enemy_win == True:
            ewin_text = result_text.render("YOU LOSE", False, light_gray)
            screen.blit(ewin_text, (348, 300))
        else:
            pwin_text = result_text.render("YOU WIN", False, light_gray)
            screen.blit(pwin_text, (348, 300))
    
        pygame.display.flip()
        clock.tick(60)

introscreen()




# Remember to use >= for collision due to framerate bugs
# Remember pygame creates seperate surface for text
