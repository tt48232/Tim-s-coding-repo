import pygame 

import time 

import random 

 

# Initialize Pygame 

pygame.init() 

 

# Set display size 

dis_width = 800 

dis_height = 600 

dis = pygame.display.set_mode((dis_width, dis_height)) 

 

# Set Title 

pygame.display.set_caption('Snake Game') 

 

# Clock to manage game speed 

clock = pygame.time.Clock() 

 

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

 

        # Update the body segment positions 

 

class Food: 

    def __init__(self): 

        self.position = [random.randrange(1, (dis_width//10)) * 10, random.randrange(1, (dis_height//10)) * 10]  # Random 

food position 

 

class Game: 

    def __init__(self): 

        self.game_over = False 

        self.snake = Snake() 

        self.food = Food() 

 

def game_loop(): 

    game = Game() 

 

    while not game.game_over: 

        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 

                game.game_over = True 

            if event.type == pygame.KEYDOWN: 

                game.snake.change_direction(pygame.key.get_pressed()) 

 

        game.snake.move(game.food.position) 

 

        if game.snake.position == game.food.position: 

            game.food.position = [random.randrange(1, dis_width//10) * 10, random.randrange(1, dis_height//10) * 

10] 

            # Increase the length of the snake 

         

        # Handle collision events and game over conditions 

 

        # Update the display 

 

        clock.tick(15)  # Game speed 

 

game_loop() 

pygame.quit() 

quit() 