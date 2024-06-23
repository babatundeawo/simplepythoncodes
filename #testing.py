import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800  # Increased width
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_SPEED = 3

# Load images
BIRD_IMG = pygame.image.load('bird.png')
PIPE_IMG = pygame.image.load('pipe.png')
BG_IMG = pygame.image.load('background.png')

# Bird class
class Bird:
    def __init__(self):
        self.image = BIRD_IMG
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Pipe class
class Pipe:
    def __init__(self, x, y, inverted):
        self.image = PIPE_IMG
        self.rect = self.image.get_rect(topleft=(x, y) if not inverted else (x, y - PIPE_GAP - self.image.get_height()))
        self.inverted = inverted

    def update(self):
        self.rect.x -= PIPE_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Function to display Game Over message
def display_game_over(screen, score):
    font = pygame.font.SysFont(None, 55)
    text = font.render(f"Game Over! Your score: {int(score)}", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Main game function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bird = Bird()
    pipes = []
    score = 0

    # Pipe generation event
    pygame.time.set_timer(pygame.USEREVENT, 1500)

    running = True
    game_over = False
    while running:
        screen.blit(BG_IMG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.flap()
            elif event.type == pygame.USEREVENT and not game_over:
                pipe_y = random.randint(SCREEN_HEIGHT // 2 - 200, SCREEN_HEIGHT // 2 + 200)
                pipes.append(Pipe(SCREEN_WIDTH, pipe_y, False))
                pipes.append(Pipe(SCREEN_WIDTH, pipe_y + PIPE_GAP, True))

        if not game_over:
            bird.update()
            bird.draw(screen)

            for pipe in pipes:
                pipe.update()
                pipe.draw(screen)

            # Collision detection
            for pipe in pipes:
                if bird.rect.colliderect(pipe.rect):
                    game_over = True
                if pipe.rect.right < 0:
                    pipes.remove(pipe)
                    score += 0.5  # Increment score when pipes pass off-screen

            # Check if bird hits ground or flies too high
            if bird.rect.top < 0 or bird.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
                game_over = True

        if game_over:
            display_game_over(screen, score)
            running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    print(f"Game Over! Your score was: {int(score)}")

# Run the game
if __name__ == "__main__":
    main()
