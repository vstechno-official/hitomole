import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH = 400
HEIGHT = 400
FPS = 30
MOLE_SIZE = 50
SNAKE_SIZE = 35
TIME_LIMIT = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hitomole")
clock = pygame.time.Clock()

# Game variables
score = 0
time_remaining = TIME_LIMIT * FPS
snake_position = [WIDTH // 2, HEIGHT // 2]
mole_position = [random.randint(0, WIDTH - MOLE_SIZE), random.randint(0, HEIGHT - MOLE_SIZE)]
mole_speed = 5

# Load game assets
mole_image = pygame.image.load('mole.png').convert_alpha()
mole_image = pygame.transform.scale(mole_image, (MOLE_SIZE, MOLE_SIZE))
snake_image = pygame.image.load('snake.png').convert_alpha()
snake_image = pygame.transform.scale(snake_image, (SNAKE_SIZE, SNAKE_SIZE))
font = pygame.font.SysFont(None, 24)

running = True
game_over = False

while running:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_position[0] -= SNAKE_SIZE
            elif event.key == pygame.K_RIGHT:
                snake_position[0] += SNAKE_SIZE
            elif event.key == pygame.K_UP:
                snake_position[1] -= SNAKE_SIZE
            elif event.key == pygame.K_DOWN:
                snake_position[1] += SNAKE_SIZE

    # Game logic
    if not game_over:
        time_remaining -= 1
        if time_remaining <= 0:
            game_over = True
        mole_position[0] += random.randint(-mole_speed, mole_speed)
        mole_position[1] += random.randint(-mole_speed, mole_speed)
        mole_position[0] = max(0, min(mole_position[0], WIDTH - MOLE_SIZE))
        mole_position[1] = max(0, min(mole_position[1], HEIGHT - MOLE_SIZE))
        snake_rect = pygame.Rect(snake_position[0], snake_position[1], SNAKE_SIZE, SNAKE_SIZE)
        mole_rect = pygame.Rect(mole_position[0], mole_position[1], MOLE_SIZE, MOLE_SIZE)
        if snake_rect.colliderect(mole_rect):
            score += 1
            mole_position = [random.randint(0, WIDTH - MOLE_SIZE), random.randint(0, HEIGHT - MOLE_SIZE)]

    # Draw
    screen.fill(BLACK)
    screen.blit(mole_image, (mole_position[0], mole_position[1]))
    screen.blit(snake_image, (snake_position[0], snake_position[1]))

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display time remaining
    time_text = font.render("Time: " + str(time_remaining // FPS), True, WHITE)
    screen.blit(time_text, (WIDTH - 100, 10))

    # Display level
    level_text = None
    if score >= 6:
        level_text = font.render("Level: Pro", True, WHITE)
    elif score >= 3:
        level_text = font.render("Level: Intermediate", True, WHITE)
    else:
        level_text = font.render("Level: Noob", True, WHITE)
    screen.blit(level_text, (WIDTH // 2 - 60, HEIGHT - 30))

    # Display game information
    game_info_text = font.render("This game belongs to vstechno", True, WHITE)
    screen.blit(game_info_text, (WIDTH // 2 - 130, HEIGHT - 60))

    pygame.display.flip()

pygame.quit()


