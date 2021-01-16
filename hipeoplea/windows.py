import Button
import pygame
from background import Background
from slider import Slider

pygame.init()
pygame.mixer.music.load('soundtrack.ogg')
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Novel")
clock = pygame.time.Clock()
f1 = pygame.font.Font('12243.otf', 36)
f2 = pygame.font.Font('12243.otf', 18)
f3 = pygame.font.Font('12243.otf', 24)

startBackGround = Background('background_image.png', [0, 0])
settingsBackGround = Background('settings.png', [0, 0])
loadBackGround = Background('background_image.png', [0, 0])

locations = {'0': 'пустой слот',
             '1': 'пролог',
             '2': 'unt',
             '3': 'unt',
             '4': 'unt'}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def startWindow():
    start = True
    screen.fill([255, 255, 255])
    screen.blit(startBackGround.image, startBackGround.rect)

    startB = Button.Button()
    startB.create_button(screen, (245, 245, 220), 80, 200, 200, 50, 0, 'start', (68, 45, 37))

    loadB = Button.Button()
    loadB.create_button(screen, (245, 245, 220), 80, 300, 200, 50, 0, 'load', (68, 45, 37))

    settB = Button.Button()
    settB.create_button(screen, (245, 245, 220), 80, 400, 200, 50, 0, 'settings', (68, 45, 37))

    exB = Button.Button()
    exB.create_button(screen, (245, 245, 220), 80, 500, 200, 50, 0, 'exit', (68, 45, 37))

    saves = open('lvl.txt')
    c = saves.read().split()
    if c[4] == '0':
        hiden = f2.render('Загляни в настройки ведь это твой первый раз в игре', True, (240, 240, 240))
        screen.blit(hiden, (0, 680))

    while start:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c[4] = '1'
                copy = ' '.join(c)
                saves.close()
                f = open('lvl.txt', 'w')
                f.write(copy)
                f.close()
                start = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startB.pressed(pygame.mouse.get_pos()):
                    start = False
                    novel()
                elif settB.pressed(pygame.mouse.get_pos()):
                    start = False
                    settings()
                elif loadB.pressed(pygame.mouse.get_pos()):
                    start = False
                    loadWindow()
                elif exB.pressed(pygame.mouse.get_pos()):
                    start = False
                    pygame.quit()
    pygame.quit()


def loadWindow():
    screen.fill([255, 255, 255])

    screen.blit(loadBackGround.image, loadBackGround.rect)
    start = True
    count = 0
    saves = open('lvl.txt').read().split()
    loc = []
    for i in saves[0:4]:
        loc.append(locations[i])
        slotText = f1.render(locations[i], True, (90, 255, 100))
        screen.blit(slotText, (400, 200 + 100 * count))
        count += 1

    screen.blit(f1.render('to go back click esc ^^', False, (0, 0, 0)), (0, 664))

    slot1 = Button.Button()
    slot1.create_button(screen, (90, 255, 100), 80, 200, 200, 50, 0, '1 save', (68, 45, 37))

    slot2 = Button.Button()
    slot2.create_button(screen, (90, 255, 100), 80, 300, 200, 50, 0, '2 save', (68, 45, 37))

    slot3 = Button.Button()
    slot3.create_button(screen, (90, 255, 100), 80, 400, 200, 50, 0, '3 save', (68, 45, 37))

    slot4 = Button.Button()
    slot4.create_button(screen, (90, 255, 100), 80, 500, 200, 50, 0, '4 save', (68, 45, 37))

    while start:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start = False
                    startWindow()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if slot1.pressed(pygame.mouse.get_pos()):
                    start = False
                    load(loc[0])
                elif slot2.pressed(pygame.mouse.get_pos()):
                    start = False
                    load(loc[1])
                elif slot3.pressed(pygame.mouse.get_pos()):
                    start = False
                    load(loc[2])
                elif slot4.pressed(pygame.mouse.get_pos()):
                    start = False
                    load(loc[3])

    pygame.quit()


def load(location):
    print(get_key(locations, location))


def settings():
    screen.fill([245, 245, 220])
    screen.blit(settingsBackGround.image, loadBackGround.rect)
    start = True

    saves = open('lvl.txt')
    c = saves.read().split()
    if c[4] == '0':
        hiden = f3.render('Привет я рада что ты сюда заглянул) Как тебе музыка?^-^', True, (80, 150, 80))
        screen.blit(hiden, (0, 600))
    c[4] = '1'
    copy = ' '.join(c)
    saves.close()
    f = open('lvl.txt', 'w')
    f.write(copy)
    f.close()

    info1 = f1.render("to move forvard print space or enter :3", True, (138, 43, 226))
    screen.blit(info1, (0, 268))
    info2 = f1.render("to back to menu click esc ", True, (138, 43, 226))
    screen.blit(info2, (0, 320))
    info3 = f1.render("BUT don't forget save your progress", True, (138, 43, 226))
    screen.blit(info3, (0, 372))
    info4 = f1.render("thanks for playing ;)", True, (138, 43, 226))
    screen.blit(info4, (0, 428))

    ex = f3.render('you still need esc to exit to menu', True, (215, 24, 104))
    screen.blit(ex, (0, 676))

    music = Slider("Music Volume", 1, 300, 1, (20, 20), (400, 70))

    off = Button.Button()
    off.create_button(screen, (90, 255, 100), 30, 150, 200, 50, 0, 'off', (68, 45, 37))

    while start:
        music.draw(screen)
        pygame.display.flip()
        int(music.get_value())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start = False
                    startWindow()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if music.button_rect.collidepoint(pos):
                    music.hit = True
                if off.pressed(pos):
                    pygame.mixer.music.set_volume(0)
            elif event.type == pygame.MOUSEBUTTONUP:
                music.hit = False
        if music.hit:
            music.move()

    pygame.quit()


def novel():
    print('novel')
    pass


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Novel")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 700))
    startWindow()
    pygame.quit()