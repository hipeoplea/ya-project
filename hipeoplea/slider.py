import pygame

pygame.init()


class Slider:
    def __init__(self, name, val, maxi, mini, position, size):
        self.val = val
        self.maxi = maxi
        self.mini = mini
        self.xpos = position[0]
        self.ypos = position[1]
        self.length = size[0] - 20
        self.surf = pygame.surface.Surface(size)
        self.hit = False

        self.txt_surf = font.render(name, True, (0, 0, 0))
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))
        print(self.txt_rect)

        # background слайдера #
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, (200, 200, 200), [0, 0, size[0], size[1]], 3)
        pygame.draw.rect(self.surf, (71, 159, 66),
                         [self.txt_rect[0] - 5, self.txt_rect[1], self.txt_rect[2] + 5, self.txt_rect[3]], 0)
        pygame.draw.rect(self.surf, (255, 255, 255), [10, 30, size[0] - 20, 5], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)

        # кружок который будет перемещаться #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill((1, 1, 1))
        self.button_surf.set_colorkey((1, 1, 1))
        pygame.draw.circle(self.button_surf, (0, 0, 0), (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, (0, 255, 50), (10, 10), 4, 0)

    def draw(self):
        surf = self.surf.copy()

        pos = (10 + int((self.val - self.mini) / (self.maxi - self.mini) * self.length), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)
        screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        # перемещение слайдера #
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / self.length * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi


# это код для проверки работоспособности класса в будующем его не будет#
X = 900
Y = 600
font = pygame.font.Font("12243.otf", 12)
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()

music = Slider("Music Volume", 1, 300, 1, (442, 326), (400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if music.button_rect.collidepoint(pos):
                music.hit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            music.hit = False
    if music.hit:
        music.move()
    screen.fill((0, 0, 0))
    music.draw()
    pygame.display.flip()
