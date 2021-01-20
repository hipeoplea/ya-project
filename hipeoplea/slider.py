import pygame

pygame.init()


class Slider:
    def __init__(self, name, val, maxi, mini, position, size, font):
        self.val = val
        self.maxi = maxi
        self.mini = mini
        self.xpos = position[0]
        self.ypos = position[1]
        self.length = size[0] - 20
        self.surf = pygame.surface.Surface(size)
        self.hit = False
        font = font

        self.txt_surf = font.render(name, True, (138, 43, 226))
        self.txt_rect = self.txt_surf.get_rect(center=(80, 15))

        # background слайдера #
        self.surf.fill((245, 245, 220))
        pygame.draw.rect(self.surf, (255, 255, 255), [0, 0, size[0], size[1]], 3)
        #pygame.draw.rect(self.surf, (138, 43, 226),
        #                 [self.txt_rect[0] - 5, self.txt_rect[1], self.txt_rect[2] + 5, self.txt_rect[3]], 0)
        pygame.draw.rect(self.surf, (138, 43, 226), [10, 40, size[0] - 20, 8], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)

        # кружок который будет перемещаться #
        self.button_surf = pygame.surface.Surface((40, 40))
        self.button_surf.fill((1, 1, 1))
        self.button_surf.set_colorkey((1, 1, 1))
        pygame.draw.circle(self.button_surf, (0, 0, 0), (30, 30), 8, 0)
        pygame.draw.circle(self.button_surf, (138, 43, 226), (30, 30), 6, 0)

    def draw(self, surface):
        surf = self.surf.copy()

        pos = (int((self.val - self.mini) / (self.maxi - self.mini) * self.length), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)
        surface.blit(surf, (self.xpos, self.ypos))

    def move(self):
        # перемещение слайдера #
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / self.length * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
        self.get_value()

    def get_value(self):
        return self.val


