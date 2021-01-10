import pygame
import os

pygame.init()
defF = os.path.join("font", "DejaVuSans.ttf")


class Dialog(pygame.sprite.Sprite):
    def __init__(self, screen, photo=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/49.png").convert()  # Фон диалога
        self.rect = self.image.get_rect()
        self.rect.center = (400, 530)
        self.image.set_alpha(220)  # Прозрачность
        if photo:
            self.photo = pygame.image.load(photo).convert_alpha()  # Боковое изображение
        else:
            self.photo = None
        self.dFont = pygame.font.Font("12243.otf", 16)  # Шрифт
        self.message = (
            "This is a sample of using dialog box.",
            "The message that shown in the dialog box ",
            "has to be a tuple or list.",
        )
        self.screen = screen
        self.nextImage = pygame.image.load('next.png').convert_alpha()  # Стрелка перехода
        self.nextImageRect = self.nextImage.get_rect()
        self.nextImageRect.right = 410
        self.nextImageRect.bottom = 120
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
                    textImage.blit(textSurf, (34, lineCount * 20 + 4))
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
                if outOfText or nextPage:
                    textImage.blit(self.nextImage, self.nextImageRect)
                textSurf = self.dFont.render(text, False, (255, 255, 255, 0))
            self.screen.blit(lastScreen, (0, 0))
            self.screen.blit(self.image, self.rect)
            self.screen.blit(textSurf, (self.rect.left + 34, lineCount * 20 + 4 + self.rect.top))
            self.screen.blit(textImage, self.rect)
            pygame.draw.rect(self.screen, (255, 255, 255), (self.rect), 2)
            if self.photo:
                self.screen.blit(self.photo, (150, 170))
            pygame.display.flip()
        self.screen.blit(lastScreen, (0, 0))
