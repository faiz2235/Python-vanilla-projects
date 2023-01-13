"""
    Snake game is an Arcade Maze Game which has been developed by Gremlin
    Industries. The players objective in the game is to achieve maximum points
    as possible by collecting food or fruits. The player loses once the snake hits
    the wall or hits itself.
    ## Setup instructions
    In order to run this script, You just need the following 3 modules -
    - **Pygame:** It is a set of Python modules designed for writing video
    games.
    - **Time:** This function is used to count the number of seconds elapsed
    since the epoch.
    - **Random:** This function is used to generate random numbers in Python
    by using random module. **Pygame, Time and Random**
"""


import pygame
import time
import random


pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


display_width = 600
display_height = 400


display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game In Python')


clock = pygame.time.Clock()


snake_block = 10
snake_speed = 15


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render(f"Your score : {score}", True, yellow)
    display.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [
                         x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/6, display_height/3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(
        0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(
        0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            display.fill(blue)
            message("You Lost! Press 'C' to Play Again or 'Q' To Quit The Game", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

                if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change

                display.fill(blue)

                pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])

                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_list.append(snake_Head)

                if len(snake_list) > Length_of_snake :
                    del snake_list[0]

                
                for x in snake_list[:-1]:
                    if x == snake_Head :
                        game_close = True


                our_snake(snake_block, snake_list)
                your_score(Length_of_snake - 1)

                pygame.display.update()

                if x1 == foodx and y1 == foody :
                    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) *10.0
                    foody = round(random.randrange(0, display_height - snake_block) / 10.0) *10.0
                    Length_of_snake += 1
                
                clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()
