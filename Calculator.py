import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 475, 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# Button data
button_data = [
    ("7", 50, 200), ("8", 150, 200), ("9", 250, 200), ("/", 350, 200),
    ("4", 50, 300), ("5", 150, 300), ("6", 250, 300), ("*", 350, 300),
    ("1", 50, 400), ("2", 150, 400), ("3", 250, 400), ("+", 350, 400),
    ("0", 50, 500), (".", 150, 500), ("=", 250, 500), ("-", 350, 500),
]

# Initialize calculator state
expression = ""
result = ""

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for label, btn_x, btn_y in button_data:
                if btn_x <= x <= btn_x + 80 and btn_y <= y <= btn_y + 80:
                    if label == "=":
                        try:
                            result = str(eval(expression))
                        except:
                            result = "Error"
                        expression = ""
                    else:
                        expression += label

    screen.fill(WHITE)

    # Draw buttons
    for label, x, y in button_data:
        pygame.draw.rect(screen, GRAY, (x, y, 80, 80))
        font = pygame.font.Font(None, 36)
        text = font.render(label, True, BLACK)
        text_rect = text.get_rect(center=(x + 40, y + 40))
        screen.blit(text, text_rect)

    # Display expression and result
    font = pygame.font.Font(None, 48)
    expression_text = font.render(expression, True, BLACK)
    expression_rect = expression_text.get_rect(center=(WIDTH // 2, 100))
    screen.blit(expression_text, expression_rect)

    result_text = font.render(result, True, BLACK)
    result_rect = result_text.get_rect(center=(WIDTH // 2, 150))
    screen.blit(result_text, result_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()