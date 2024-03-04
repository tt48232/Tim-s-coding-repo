Sure, here's a simple Python program for a Snake game using the Pygame library:
```python
import pygame
import sys

pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500

# Set the initial position and size of the snake
SNAKE_SIZE = 10
SNAKE_INIT_X = 200
SNAKE_INIT_Y = 300

# Set the initial direction of the snake
SNAKE_DIR = 'RIGHT'

# Set the initial food position
FOOD_X = 250
FOOD_Y = 350

# Set the speed of the snake
SNAKE_SPEED = 5

# Define the colors for the snake and food
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the font for the game over message
font = pygame.font.SysFont(None, 36)

# Set up the snake
snake = [SNAKE_INIT_X, SNAKE_INIT_Y]

# Set up the food
food = [FOOD_X, FOOD_Y]

# Set up the score
score = 0

# Set up the direction of the snake
snake_dir = SNAKE_DIR

# Set up the snake speed
snake_speed = SNAKE_SPEED

# Set up the game over flag
game_over = False

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.keys[0] == pygame.K_LEFT:
                snake_dir = 'LEFT'
            elif event.keys[0] == pygame.K_RIGHT:
                snake_dir = 'RIGHT'
            elif event.keys[0] == pygame.K_UP:
                snake_dir = 'UP'
            elif event.keys[0] == pygame.K_DOWN:
                snake_dir = 'DOWN'

    # Move the snake
    if snake_dir == 'LEFT':
        snake = [max(snake[0] - SNAKE_SIZE, 0), snake[1]]
    elif snake_dir == 'RIGHT':
        snake = [min(snake[0] + SNAKE_SIZE, WINDOW_WIDTH), snake[1]]
    elif snake_dir == 'UP':
        snake = [snake[0], max(snake[1] - SNAKE_SIZE, 0)]
    elif snake_dir == 'DOWN':
        snake = [snake[0], min(snake[1] + SNAKE_SIZE, WINDOW_HEIGHT)]
    
    # Move the food
    if snake_dir == 'LEFT':
        food = [max(food[0] - SNAKE_SIZE, 0), food[1]]
    elif snake_dir == 'RIGHT':
        food = [min(food[0] + SNAKE_SIZE, WINDOW_WIDTH), food[1]]
    elif snake_dir == 'UP':
        food = [food[0], max(food[1] - SNAKE_SIZE, 0)]
    elif snake_dir == 'DOWN':
        food = [food[0], min(food[1] + SNAKE_SIZE, WINDOW_HEIGHT)]
    
    # Check if the snake has eaten the food
    if snake[0] == food[0] and snake[1] == food[1]:
        score += 1
        food = [max(0, random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)), max