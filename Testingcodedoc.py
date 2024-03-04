
import pygame 

import time 

import random 

 

pygame.init() 

 

# Colors 

white = (255, 255, 255) 

yellow = (255, 255, 102) 

black = (0, 0, 0) 

red = (213, 50, 80) 

green = (0, 255, 0) 

blue = (50, 153, 213) 

 

# Set display size 

dis_width = 800 

dis_height = 600 

dis = pygame.display.set_mode((dis_width, dis_height)) 

pygame.display.set_caption('Snake Game') 

 

# Snake block size 

snake_block = 10 

 

# Clock to manage game speed 

clock = pygame.time.Clock() 

 

# Fonts 

font_style = pygame.font.SysFont(None, 50) 

 

class Snake: 

    def __init__(self): 

        self.position = [100, 50] 

        self.body = [[100, 50], [90, 50], [80, 50]] 

        self.direction = "RIGHT" 

        self.change_to = self.direction 

 

    def change_direction(self, keys): 

        if keys[pygame.K_UP] and self.direction != "DOWN": 

            self.change_to = "UP" 

        if keys[pygame.K_DOWN] and self.direction != "UP": 

            self.change_to = "DOWN" 

        if keys[pygame.K_LEFT] and self.direction != "RIGHT": 

            self.change_to = "LEFT" 

        if keys[pygame.K_RIGHT] and self.direction != "LEFT": 

            self.change_to = "RIGHT" 

 

    def move(self, food_position): 

        if self.change_to == "UP": 

            self.position[1] -= 10 

        if self.change_to == "DOWN": 

            self.position[1] += 10 

        if self.change_to == "LEFT": 

            self.position[0] -= 10 

        if self.change_to == "RIGHT": 

            self.position[0] += 10 

 

        if self.position == food_position: 

            # Grow the Snake 

 

            def grow(self, food_position): 

            # Increase the length of the Snake 

                pass 

 

class Food: 

    def __init__(self): 

        self.position = [random.randrange(1, (dis_width//10)) * 10, random.randrange(1, (dis_height//10)) * 10]  # Random food position 

 

def game_loop(): 

    game_over = False 

    snake = Snake() 

    food = Food() 

    score = 0 

 

    while not game_over: 

        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 

                game_over = True 

            if event.type == pygame.KEYDOWN: 

                if event.key == pygame.K_UP: 

                    snake.change_to = "UP" 

                elif event.key == pygame.K_DOWN: 

                    snake.change_to = "DOWN" 

                elif event.key == pygame.K_LEFT: 

                    snake.change_to = "LEFT" 

                elif event.key == pygame.K_RIGHT: 

                    snake.change_to = "RIGHT" 

 

        snake.move(food.position) 

 

        if snake.position == food.position: 

            food.position = [random.randrange(1, (dis_width//10)) * 10, random.randrange(1, (dis_height//10)) * 

10] 

            score += 1 

            snake.grow() 

 

        # Collision detection and game over handling 

 

        dis.fill(blue) 

        # Draw the snake and the food 

        pygame.display.update() 

 

        clock.tick(15)  # Game speed 

 

game_loop() 

pygame.quit() 

quit() 