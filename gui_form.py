import pygame

class TextInput:
    def __init__(self, x, y, width, height, max_length):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font = pygame.font.Font("./assets/fonts/Redaction35-Bold.otf", 25)
        self.max_length = max_length

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < self.max_length:
                    self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        rendered_text = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(rendered_text, (self.rect.x + 5, self.rect.y + 5))