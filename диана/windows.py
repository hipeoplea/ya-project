import os
import sqlite3

import Button
import pygame
from background import Background
from dialog import Dialog
from slider import Slider

pygame.init()
pygame.mixer.music.load(os.path.join('data\sounds', 'soundtrack.ogg'))
click = pygame.mixer.Sound(os.path.join('data\sounds', 'click.wav'))
lucky = pygame.mixer.Sound(os.path.join('data\sounds', 'luck.ogg'))
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Novel")
clock = pygame.time.Clock()

f1 = pygame.font.Font(os.path.join('data', 'font.otf'), 36)
f2 = pygame.font.Font(os.path.join('data', 'font.otf'), 18)
f3 = pygame.font.Font(os.path.join('data', 'font.otf'), 24)

startBackGround = Background(os.path.join('data', 'backgrounds', 'menuBack.png'), [0, 0])
menu2 = Background(os.path.join('data', 'backgrounds', 'menuBack2.png'), [0, 0])

con = sqlite3.connect(os.path.join('data', 'replics.db'))
cur = con.cursor()

locations = {'0': 'пустой слот',
             '1': 'пролог',
             '2': 'флешбек',
             '3': 'начало расследования',
             '4': 'звонок',
             '5': 'на пути к хисоке',
             '6': 'в ожидании иллуми',
             '7': 'казино',
             '11': 'просьба о помощи',
             '12': 'запись с камер',
             '13': 'сами справимся',
             '14': 'заплатим',
             '15': 'не хватает денег',
             '16': 'камера',
             '17': 'встреча с иллуми',
             '18': 'встретили иллуми'}


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

    saves = open(os.path.join('data', 'lvl.txt'))
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
                f = open(os.path.join('data', 'lvl.txt'), 'w')
                f.write(copy)
                f.close()
                start = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startB.pressed(pygame.mouse.get_pos()):
                    start = False
                    prolog()
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
    screen.fill([245, 245, 220])
    screen.blit(menu2.image, menu2.rect)
    start = True

    count = 0
    saves = open(os.path.join('data', 'lvl.txt')).read().split()
    loc = []
    for i in saves[0:4]:
        loc.append(locations[i])
        slotText = f1.render(locations[i], True, (0, 0, 0))
        screen.blit(slotText, (300, 100 + 100 * count))
        count += 1

    screen.blit(f1.render('to go back click esc ^^', False, (0, 0, 0)), (0, 664))

    slot1 = Button.Button()
    slot1.create_button(screen, (90, 255, 100), 40, 100, 200, 50, 0, '1 save', (68, 45, 37))

    slot2 = Button.Button()
    slot2.create_button(screen, (90, 255, 100), 40, 200, 200, 50, 0, '2 save', (68, 45, 37))

    slot3 = Button.Button()
    slot3.create_button(screen, (90, 255, 100), 40, 300, 200, 50, 0, '3 save', (68, 45, 37))

    slot4 = Button.Button()
    slot4.create_button(screen, (90, 255, 100), 40, 400, 200, 50, 0, '4 save', (68, 45, 37))

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
    screen.blit(menu2.image, menu2.rect)
    start = True

    saves = open(os.path.join('data', 'lvl.txt'))
    c = saves.read().split()
    if c[4] == '0':
        hiden = f3.render('Привет я рада что ты сюда заглянул) Как тебе музыка?^-^', True, (80, 150, 80))
        screen.blit(hiden, (0, 600))
    c[4] = '1'
    copy = ' '.join(c)
    saves.close()
    f = open('data\lvl.txt', 'w')
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

    music = Slider("Music Volume", 300, 300, 1, (20, 20), (400, 70), f2)

    off = Button.Button()
    off.create_button(screen, (90, 255, 100), 30, 150, 200, 50, 0, 'off', (68, 45, 37))

    while start:
        music.draw(screen)
        pygame.display.flip()

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
                    pygame.mixer.music.set_volume(int(music.get_value()) / 300)
                if off.pressed(pos):
                    pygame.mixer.music.set_volume(0)
            elif event.type == pygame.MOUSEBUTTONUP:
                music.hit = False
        if music.hit:
            music.move()

    pygame.quit()


def prolog():
    result = cur.execute("""SELECT * FROM text WHERE location = 1""").fetchall()
    screen.fill([245, 245, 220])
    screen.blit(menu2.image, menu2.rect)
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Это был самый обычный день из моей жизни, как....",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("???:Приветствую,житель Земли..",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = (
        "ЭТО ПОХОДУ РЕАЛЬНО ЧТО-ТО СЕРЬЁЗНОЕ! НАДО КОМУ-НИБУДЬ ПОЗВОНИТЬ.... эээ... Иллуми? Ты звонил Иллуми?Я думаю, что Леорио прав. Я вам ещё чем-то могу помочь или вы дадите мне насладиться моим прекрасным напитком?",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Элис:Сейчас я готова пообщаться, а ты?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Элис:Ой, и совсем забыла спросить твоё имя..",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Тебе интересно мое имя? Меня зовут Николас.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Элис:Привет Николас, рада познакомиться, а ты?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    slot3 = Button.Button()
    slot3.create_button(screen, (90, 255, 100), 40, 300, 200, 50, 0, '3 save', (68, 45, 37))

    slot4 = Button.Button()
    slot4.create_button(screen, (90, 255, 100), 40, 400, 200, 50, 0, '4 save', (68, 45, 37))
    while True:
        pygame.event.pump()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if slot3.pressed(pygame.mouse.get_pos()):
                    print("Концовка-1")
                    click.play()
                    whot()
                elif slot4.pressed(pygame.mouse.get_pos()):
                    print("Продолжение...")
                    click.play()
                    go()


def whot():
    pass


def go():
    pass


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Novel")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 700))
    startWindow()
    pygame.quit()
