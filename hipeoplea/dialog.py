import pygame
import os

pygame.init()
defF = os.path.join("data", "font.otf")


class Dialog(pygame.sprite.Sprite):
    def __init__(self, screen, photo=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/backgrounds/49.png")  # Фон диалога
        self.rect = self.image.get_rect()
        self.rect.center = (450, 650)
        self.image.set_alpha(200)  # Прозрачность
        if photo:
            self.photo = pygame.image.load(photo).convert_alpha()  # Боковое изображение
        else:
            self.photo = None
        self.dFont = pygame.font.Font("data/font.otf", 16)  # Шрифт
        self.message = (
            "This is a sample of using dialog box.",
            "The message that shown in the dialog box ",
            "has to be a tuple or list.",
        )
        self.screen = screen
        self.show = True

    def sndNext(self):
        outOfText = False
        line = 0
        lineCount = 0
        nextPage = False
        text_pos = 0
        text = ""
        delayTimer = 30
        textSurf = None
        textImage = pygame.Surface(self.image.get_size())
        textImage.fill((0, 0, 0))
        textImage.set_colorkey((0, 0, 0))
        lastScreen = pygame.Surface(self.screen.get_size())
        lastScreen.blit(self.screen, (0, 0))
        while self.show:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        if not outOfText and not nextPage:
                            delayTimer = 0
                            continue
                        elif nextPage:
                            nextPage = False
                            textImage = pygame.Surface(self.image.get_size())
                            textImage.fill((0, 0, 0))
                            textImage.set_colorkey((0, 0, 0))
                            delayTimer = 30
                            continue
                        self.show = False
            if not outOfText and not nextPage:
                pygame.time.delay(delayTimer)
                text += self.message[line][text_pos]
                text_pos += 1
                if text_pos > len(self.message[line]) - 1:
                    textImage.blit(textSurf, (34, lineCount * 20 + 20))
                    textImage.set_colorkey((0, 0, 0))
                    text_pos = 0
                    line += 1
                    lineCount += 1
                    text = ""
                    if lineCount > 6:
                        nextPage = True
                        lineCount = 0
                        text = ""
                        text_pos = 0
                if line > len(self.message) - 1:
                    outOfText = True
                textSurf = self.dFont.render(text, False, (255, 255, 255, 0))
            self.screen.blit(lastScreen, (0, 0))
            self.screen.blit(self.image, self.rect)
            self.screen.blit(textSurf, (self.rect.left + 50, lineCount * 20 + 20 + self.rect.top))
            self.screen.blit(textImage, self.rect)
            if self.photo:
                self.screen.blit(self.photo, (150, 170))
            pygame.display.flip()
        self.screen.blit(lastScreen, (0, 0))
