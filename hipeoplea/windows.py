import os
import sqlite3
import time
import pygame
import sys
from pygame.locals import *
import Button
from background import Background
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

fon1 = Background(os.path.join('data', 'backgrounds', 'cafe.jpg'), [0, 0])
fon3 = Background(os.path.join('data', 'backgrounds', 'street.jpg'), [0, 0])
fon4 = Background(os.path.join('data', 'backgrounds', 'vorota.jpg'), [0, 0])
fon5 = Background(os.path.join('data', 'backgrounds', 'vorota_bez_vsex.jpg'), [0, 0])
fon6 = Background(os.path.join('data', 'backgrounds', 'cazino_inside.jpg'), [0, 0])
fon7 = Background(os.path.join('data', 'backgrounds', 'cazino_outside.jpg'), [0, 0])

tel_killua = Background(os.path.join('data', 'backgrounds', 'cafe_tel.jpg'), [0, 0])
tel_illumi = Background(os.path.join('data', 'backgrounds', 'cafe_tel_2.jpg'), [0, 0])
tel_illumi2 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_3.jpg'), [0, 0])
tel_illumi3 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_4.jpg'), [0, 0])

tel_kontakti = Background(os.path.join('data', 'backgrounds', 'kontakti.jpg'), [0, 0])

tel_leorio = Background(os.path.join('data', 'backgrounds', 'cafe_tel_5.jpg'), [0, 0])
tel_leorio1 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_6.jpg'), [0, 0])
tel_leorio2 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_7.jpg'), [0, 0])
tel_leorio3 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_8.jpg'), [0, 0])
tel_leorio4 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_9.jpg'), [0, 0])
tel_leorio5 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_10.jpg'), [0, 0])
tel_leorio6 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_11.jpg'), [0, 0])
tel_leorio7 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_12.jpg'), [0, 0])
tel_leorio8 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_13.jpg'), [0, 0])
tel_leorio9 = Background(os.path.join('data', 'backgrounds', 'cafe_tel_14.jpg'), [0, 0])

tel_hisoka = Background(os.path.join('data', 'backgrounds', 'vorota_tel.jpg'), [0, 0])
tel_hisoka1 = Background(os.path.join('data', 'backgrounds', 'vorota_tel1.jpg'), [0, 0])
tel_hisoka2 = Background(os.path.join('data', 'backgrounds', 'vorota_tel2.jpg'), [0, 0])
tel_hisoka3 = Background(os.path.join('data', 'backgrounds', 'vorota_tel3.jpg'), [0, 0])
tel_hisoka4 = Background(os.path.join('data', 'backgrounds', 'vorota_tel4.jpg'), [0, 0])
tel_hisoka5 = Background(os.path.join('data', 'backgrounds', 'vorota_tel5.jpg'), [0, 0])
tel_hisoka6 = Background(os.path.join('data', 'backgrounds', 'vorota_tel6.jpg'), [0, 0])

for_win = pygame.image.load(os.path.join('data', 'killua.gif')).convert()
for_win_pos = for_win.get_rect(center=(275, 540))
for_lose = Background(os.path.join('data', 'backgrounds', 'prison.jpg'), [0, 0])

rec = Background(os.path.join('data', 'rec', '1.jpg'), [0, 0])
rec2 = Background(os.path.join('data', 'rec', '2.jpg'), [0, 0])
rec3 = Background(os.path.join('data', 'rec', '3.jpg'), [0, 0])
rec4 = Background(os.path.join('data', 'rec', '4.jpg'), [0, 0])
rec5 = Background(os.path.join('data', 'rec', '5.jpg'), [0, 0])
rec6 = Background(os.path.join('data', 'rec', '6.jpg'), [0, 0])
rec7 = Background(os.path.join('data', 'rec', '7.jpg'), [0, 0])
rec8 = Background(os.path.join('data', 'rec', '8.jpg'), [0, 0])

bl = Background(os.path.join('data', 'backgrounds', 'black1.png'), [0, 0])
bl1 = Background(os.path.join('data', 'backgrounds', 'bl.png'), [0, 0])
bl2 = Background(os.path.join('data', 'backgrounds', 'black3.png'), [0, 0])
bl3 = Background(os.path.join('data', 'backgrounds', 'black4.png'), [0, 0])

# Вывод спрайтов персонажей
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(os.path.join("data\pers", filename))

    def pers(self):
        screen.blit(self.bitmap, (self.x, self.y))


killua = Sprite(0, 300, "killua.png")
illumi = Sprite(0, 300, "illumi.png")
gon = Sprite(550, 300, "gon.png")
leorio = Sprite(0, 291, "leorio_2.png")
oxrana = Sprite(50, 290, "oxrana.png")
hisoka = Sprite(50, 290, "hisoka.png")

con = sqlite3.connect(os.path.join('data', 'replics.db'))
cur = con.cursor()

global balance
balance = 500

global videl_camera
videl_camera = False

locations = {'0': 'пустой слот',
             '1': 'пролог',
             '2': 'флешбек',
             '3': 'начало расследования',
             '4': 'звонок',
             '5': 'на пути к хисоке',
             '6': 'в ожидании иллуми',
             '7': 'казино',
             '8': 'ответ хисоки',
             '9': 'ответ хисоки',
             '10': 'казино2',
             '11': 'просьба о помощи',
             '12': 'запись с камер',
             '13': 'сами справимся',
             '14': 'заплатим',
             '15': 'не хватает денег',
             '16': 'камера',
             '17': 'встреча с иллуми',
             '18': 'встретили иллуми'}


class Dialog(pygame.sprite.Sprite):
    def __init__(self, screen, loc, photo=None):
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
        self.loc = loc
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # монетки
                    pos = pygame.mouse.get_pos()
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
                    elif event.key == pygame.K_F5:
                        loadWindow(self.loc)
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


def get_key(d, value):
    loc = 0
    for k, v in d.items():
        if v == value:
            loc = k
    if loc == '0':
        loadWindow()
    elif loc == '1':
        prolog()
    elif loc == '2':
        fleshback()
    elif loc == '3':
        nachalo()
    elif loc == '4':
        call()
    elif loc == '5':
        do()
    elif loc == '6':
        wait()
    elif loc == '7':
        kazino()
    elif loc == '8':
        yes()
    elif loc == '9':
        no()
    elif loc == '10':
        kazino_2()
    elif loc == '11':
        askHelp()
    elif loc == '12':
        askKameras()
    elif loc == '13':
        nothing()
    elif loc == '14':
        give_money()
    elif loc == '15':
        dont_give_money()
    elif loc == '16':
        see_camera()
    elif loc == '17':
        dont_see_camera()


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
                    click.play()
                    nach()
                elif settB.pressed(pygame.mouse.get_pos()):
                    start = False
                    click.play()
                    settings()
                elif loadB.pressed(pygame.mouse.get_pos()):
                    start = False
                    click.play()
                    loadWindow()
                elif exB.pressed(pygame.mouse.get_pos()):
                    start = False
                    click.play()
                    pygame.quit()
    pygame.quit()


def loadWindow(locat=None):
    screen.fill([245, 245, 220])
    screen.blit(menu2.image, menu2.rect)
    start = True

    count = 0
    save = open(os.path.join('data', 'lvl.txt'))
    saves = save.read().split()
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
            if locat is None:
                if event.type == pygame.QUIT:
                    start = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                        click.play()
                        startWindow()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if slot1.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        load(loc[0])
                    elif slot2.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        load(loc[1])
                    elif slot3.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        load(loc[2])
                    elif slot4.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        load(loc[3])
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                        load(locat)
                elif event.type == pygame.QUIT:
                    start = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if slot1.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        save.close()
                        copy = saves
                        f = open('data\lvl.txt', 'w')
                        copy[0] = locat
                        f.write(' '.join(copy))
                        f.close()

                        startWindow()
                    elif slot2.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        save.close()
                        copy = saves
                        f = open('data\lvl.txt', 'w')
                        copy[1] = locat
                        f.write(' '.join(copy))
                        f.close()
                        startWindow()
                    elif slot3.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        save.close()
                        copy = saves
                        f = open('data\lvl.txt', 'w')
                        copy[2] = locat
                        f.write(' '.join(copy))
                        f.close()
                        startWindow()
                    elif slot4.pressed(pygame.mouse.get_pos()):
                        start = False
                        click.play()
                        save.close()
                        copy = saves
                        f = open('data\lvl.txt', 'w')
                        copy[3] = locat
                        f.write(' '.join(copy))
                        f.close()
                        startWindow()

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


def nach():
    screen.fill([0, 0, 0])
    pygame.display.flip()
    pygame.mixer.music.pause()
    lucky.play()
    time.sleep(12)
    pygame.mixer.music.unpause()
    prolog()


def prolog():
    result = cur.execute("""SELECT replik FROM text WHERE location = 1""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon1.image, fon1.rect)
    unNoDialog = Dialog(screen, '1')

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[0][0]:
            gon.pers()
        elif phrase == result[1][0]:
            screen.blit(tel_killua.image, tel_killua.rect)
        elif phrase == result[2][0]:
            screen.blit(tel_killua.image, tel_killua.rect)
        elif phrase == result[3][0]:
            screen.blit(tel_illumi2.image, tel_illumi2.rect)
        elif phrase == result[5][0]:
            screen.blit(tel_illumi3.image, tel_illumi3.rect)
        elif phrase == result[6][0]:
            screen.blit(tel_kontakti.image, tel_kontakti.rect)
        elif phrase == result[7][0]:
            screen.blit(tel_leorio.image, tel_leorio.rect)
        elif phrase == result[8][0]:
            screen.blit(tel_leorio1.image, tel_leorio1.rect)
        elif phrase == result[9][0]:
            screen.blit(tel_leorio2.image, tel_leorio2.rect)
        elif phrase == result[10][0]:
            screen.blit(tel_leorio3.image, tel_leorio3.rect)
        elif phrase == result[11][0]:
            screen.blit(tel_leorio4.image, tel_leorio4.rect)

        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}"))""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    fleshback()


def fleshback():
    result = cur.execute("""SELECT replik FROM text WHERE location = 2""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon3.image, fon3.rect)
    unNoDialog = Dialog(screen, '2')
    pers = 1

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 2)""").fetchall()
        name = name[0]
        if pers == 1:
            screen.blit(fon3.image, fon3.rect)
            gon.pers()
            pers += 1
        elif pers == 2:
            screen.blit(fon3.image, fon3.rect)
            killua.pers()
            pers -= 1
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    nachalo()


def nachalo():
    start = True
    screen.fill([255, 255, 255])
    screen.blit(tel_leorio5.image, tel_leorio5.rect)
    result = cur.execute("""SELECT replik FROM text WHERE location = 3""").fetchall()
    lct = '3'
    unNoDialog = Dialog(screen, lct)

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[2][0]:
            screen.blit(tel_leorio6.image, tel_leorio6.rect)
        elif phrase == result[3][0]:
            screen.blit(tel_leorio7.image, tel_leorio7.rect)
        elif phrase == result[4][0]:
            screen.blit(tel_leorio8.image, tel_leorio8.rect)
        elif phrase == result[5][0]:
            screen.blit(tel_leorio9.image, tel_leorio9.rect)
        elif phrase == result[6][0]:  # золдики
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[7][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[8][0]:
            screen.blit(fon5.image, fon5.rect)
            oxrana.pers()
        elif phrase == result[9][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[10][0]:
            screen.blit(fon5.image, fon5.rect)
            oxrana.pers()
        elif phrase == result[11][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[12][0]:
            screen.blit(fon5.image, fon5.rect)
            oxrana.pers()
        elif phrase == result[14][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[16][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[17][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[18][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[19][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
            screen.blit(bl.image, bl.rect)
            time.sleep(0.1)
            pygame.display.flip()
            screen.fill((255,255,255))
            screen.blit(bl1.image, bl.rect)
            time.sleep(0.1)
            pygame.display.flip()
            screen.fill((255,255,255))
            screen.blit(bl2.image, bl.rect)
            time.sleep(0.1)
            pygame.display.flip()
            screen.fill((255,255,255))
            screen.blit(bl3.image, bl.rect)
            time.sleep(1)
            pygame.display.flip()
            screen.fill((255,255,255))
            screen.blit(bl2.image, bl.rect)
            time.sleep(0.1)
            pygame.display.flip()
            screen.fill((255,255,255))
            screen.blit(bl1.image, bl.rect)
            time.sleep(0.1)
            pygame.display.flip()
            screen.fill((255,255,255))
            screen.blit(bl.image, bl.rect)
            time.sleep(0.1)
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[21][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[22][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[23][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[24][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[25][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[26][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[27][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                            (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 3)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    screen.blit(fon5.image, fon5.rect)
    call1 = Button.Button()
    call1.create_button(screen, (124, 124, 124), 0, 500, 900 // 3, 200, 0, 'позвонить Хисоке', (255, 255, 255), 1)
    do1 = Button.Button()
    do1.create_button(screen, (124, 124, 124), 900 // 3, 500, 900 // 3, 200, 0, 'пойти к Хисоке', (255, 255, 255), 1)
    wait1 = Button.Button()
    wait1.create_button(screen, (124, 124, 124), 900 // 3 * 2, 500, 900 // 3, 200, 0, 'подождать Иллуми',
                        (255, 255, 255), 1)
    while start:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    loadWindow(lct)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if call1.pressed(pos):
                    start = False
                    click.play()
                    call()
                if do1.pressed(pos):
                    start = False
                    click.play()
                    do()
                if wait1.pressed(pos):
                    start = False
                    click.play()
                    wait()


def call():
    result = cur.execute("""SELECT replik FROM text WHERE location = 4""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(tel_hisoka.image, tel_hisoka.rect)
    unNoDialog = Dialog(screen, '4')

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[1][0]:
            screen.blit(tel_hisoka1.image, tel_hisoka1.rect)
        elif phrase == result[1][0]:
            screen.blit(tel_hisoka2.image, tel_hisoka2.rect)
        elif phrase == result[2][0]:
            screen.blit(tel_hisoka3.image, tel_hisoka3.rect)
        elif phrase == result[3][0]:
            screen.blit(tel_hisoka4.image, tel_hisoka4.rect)
        elif phrase == result[4][0]:
            screen.blit(tel_hisoka5.image, tel_hisoka5.rect)
        elif phrase == result[7][0]:
            screen.blit(tel_hisoka6.image, tel_hisoka6.rect)
        elif phrase == result[10][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[11][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[12][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[13][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[-1][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                    (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 4)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    kazino()


def do():
    result = cur.execute("""SELECT replik FROM text WHERE location = 5""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon5.image, fon5.rect)
    unNoDialog = Dialog(screen, '5')

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[0][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()

        elif phrase == result[1][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[2][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[3][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[4][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[5][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[6][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[7][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 5)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    kazino()


def wait():
    result = cur.execute("""SELECT replik FROM text WHERE location = 6""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon5.image, fon5.rect)
    unNoDialog = Dialog(screen, '6')

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[0][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[2][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[3][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[4][0]:
            screen.blit(fon5.image, fon5.rect)
            illumi.pers()
        elif phrase == result[5][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[6][0]:
            screen.blit(fon5.image, fon5.rect)
            gon.pers()
        elif phrase == result[7][0]:
            screen.blit(fon5.image, fon5.rect)
            leorio.pers()
        elif phrase == result[-1][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 6)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    kazino()


def kazino():
    start = True
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    lct = '7'
    gon.pers()
    unNoDialog = Dialog(screen, lct)
    unNoDialog.message = ("Гон: Вполне возможно что Киллуа пропал. Ты не знаешь что-то об этом?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    hisoka.pers()
    unNoDialog.message = ("Хисока: Вы из-за этого пришли? Не то что бы мне есть дело, но вы рассказали Иллуми?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    yes1 = Button.Button()
    yes1.create_button(screen, (124, 124, 124), 0, 500, 900 // 2, 200, 0, 'да', (255, 255, 255), 1)
    no1 = Button.Button()
    no1.create_button(screen, (124, 124, 124), 900 // 2, 500, 900 // 2, 200, 0, 'нет', (255, 255, 255), 1)
    while start:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    loadWindow(lct)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if yes1.pressed(pos):
                    start = False
                    click.play()
                    yes()
                if no1.pressed(pos):
                    start = False
                    click.play()
                    no()


def yes():
    result = cur.execute("""SELECT replik FROM text WHERE location = 8""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    unNoDialog = Dialog(screen, '8')
    pers = 1

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 8)""").fetchall()
        name = name[0]
        if pers == 1:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
            pers += 1
        elif pers == 2:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
            pers -= 1
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    kazino_2()


def no():
    result = cur.execute("""SELECT replik FROM text WHERE location = 9""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    unNoDialog = Dialog(screen, '9')
    pers = 1

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                    (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 9)""").fetchall()
        name = name[0]
        if pers == 1:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
            pers += 1
        elif pers == 2:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
            pers -= 1
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    kazino_2()


def kazino_2():
    result = cur.execute("""SELECT replik FROM text WHERE location = 10""").fetchall()
    start = True
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    lct = '10'
    unNoDialog = Dialog(screen, lct)

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[0][0]:
            gon.pers()
        elif phrase == result[1][0]:
            screen.blit(fon6.image, fon6.rect)
            leorio.pers()
        elif phrase == result[2][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[3][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[4][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 10)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    askHelp1 = Button.Button()
    askHelp1.create_button(screen, (124, 124, 124), 0, 500, 900 // 3, 200, 0, 'попросить помощь', (255, 255, 255), 1)
    askKameras1 = Button.Button()
    askKameras1.create_button(screen, (124, 124, 124), 900 // 3, 500, 900 // 3, 200, 0, 'запись с камер',
                              (255, 255, 255), 1)
    nothing1 = Button.Button()
    nothing1.create_button(screen, (124, 124, 124), 900 // 3 * 2, 500, 900 // 3, 200, 0, 'ничего не просить',
                           (255, 255, 255), 1)
    while start:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    loadWindow(lct)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if askHelp1.pressed(pos):
                    start = False
                    click.play()
                    askHelp()
                if askKameras1.pressed(pos):
                    start = False
                    click.play()
                    askKameras()
                if nothing1.pressed(pos):
                    start = False
                    click.play()
                    nothing()


def askHelp():
    result = cur.execute("""SELECT replik FROM text WHERE location = 11""").fetchall()
    start = True
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    unNoDialog = Dialog(screen, '11')

    for elem in result:
        phrase = elem[0]
        c = 85
        if phrase == result[0][0]:
            gon.pers()
        elif phrase == result[1][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[2][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[3][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[4][0]:
            screen.blit(fon6.image, fon6.rect)
            leorio.pers()
        elif phrase == result[5][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[6][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[7][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[8][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[9][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[10][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[11][0]:
            screen.blit(fon6.image, fon6.rect)
            leorio.pers()
        elif phrase == result[12][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[13][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[14][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[15][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()

        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 11)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
        screen.blit(fon6.image, fon6.rect)
    camera(11)


def after_camera():
    start = True
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    videl_camera = True
    lct = '7'
    unNoDialog = Dialog(screen, lct)
    leorio.pers()
    unNoDialog.message = ("Леорио: И каким образом мы узнаем кто это?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    hisoka.pers()
    unNoDialog.message = ("Хисока: Ну, я вам помог, а так у меня есть и свои дела... Пока!.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    leorio.pers()
    unNoDialog.message = ("Леорио: ....",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    gon.pers()
    unNoDialog.message = ("Гон: Эх, спасибо!.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    withIllumi()


def askKameras():
    result = cur.execute("""SELECT replik FROM text WHERE location = 12""").fetchall()
    start = True
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    lct = '12'
    unNoDialog = Dialog(screen, lct)
    pers = 1

    for elem in result:
        phrase = elem[0]
        c = 85
        if pers == 1:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
            pers += 1
        elif pers == 2:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
            pers -= 1
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 12)""").fetchall()
        name = name[0]
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    screen.blit(fon6.image, fon6.rect)
    give_money1 = Button.Button()
    give_money1.create_button(screen, (124, 124, 124), 0, 500, 900 // 2, 200, 0, f'заплатить'
                                                                                 f'(ваш баланс: {balance})',
                              (255, 255, 255), 1)
    dont_give_money1 = Button.Button()
    dont_give_money1.create_button(screen, (124, 124, 124), 900 // 2, 500, 900 // 2, 200, 0, 'не платить',
                                   (255, 255, 255), 1)
    while start:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    loadWindow(lct)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if dont_give_money1.pressed(pos):
                    start = False
                    click.play()
                    dont_give_money()
                if give_money1.pressed(pos) and balance >= 500:
                    start = False
                    click.play()
                    give_money()


def nothing():
    result = cur.execute("""SELECT replik FROM text WHERE location = 13""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    unNoDialog = Dialog(screen, '13')

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 13)""").fetchall()
        name = name[0]
        if phrase == result[0][0]:
            gon.pers()
        elif phrase == result[1][0]:
            screen.blit(fon6.image, fon6.rect)
            leorio.pers()
        elif phrase == result[2][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[4][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    withIllumi()


def give_money():
    result = cur.execute("""SELECT replik FROM text WHERE location = 14""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    unNoDialog = Dialog(screen, '14')

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 14)""").fetchall()
        name = name[0]
        if phrase == result[0][0]:
            gon.pers()
        elif phrase == result[1][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[2][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[3][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[4][0]:
            screen.blit(fon6.image, fon6.rect)
            leorio.pers()
        elif phrase == result[5][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[6][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        elif phrase == result[7][0]:
            screen.blit(fon6.image, fon6.rect)
            gon.pers()
        elif phrase == result[8][0]:
            screen.blit(fon6.image, fon6.rect)
            hisoka.pers()
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    camera(11)


def dont_give_money():
    result = cur.execute("""SELECT replik FROM text WHERE location = 15""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon6.image, fon6.rect)
    unNoDialog = Dialog(screen, '15')

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 15)""").fetchall()
        name = name[0]
        gon.pers()
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    withIllumi()


def withIllumi():
    start = True
    screen.fill([255, 255, 255])
    screen.blit(fon7.image, fon7.rect)
    lct = '7'
    unNoDialog = Dialog(screen, lct)
    gon.pers()
    unNoDialog.message = ("Гон: Это Иллуми?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon7.image, fon7.rect)
    leorio.pers()
    unNoDialog.message = ("Леорио: Походу....",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon7.image, fon7.rect)
    illumi.pers()
    unNoDialog.message = ("Иллуми:Так и знал что вы у него! Не думал о такой подставе.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    unNoDialog.message = ("Иллуми: Я ему говорил что будет если он тронет Киллуа..",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon7.image, fon7.rect)
    gon.pers()
    unNoDialog.message = ("Гон: Ты о чём?.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    screen.blit(fon7.image, fon7.rect)
    illumi.pers()
    unNoDialog.message = ("Иллуми: Смотрите.",)
    unNoDialog.show = True
    unNoDialog.sndNext()
    camera(12)


def see_camera():
    start = True
    result = cur.execute("""SELECT replik FROM text WHERE location = 16""").fetchall()
    lct = '16'
    unNoDialog = Dialog(screen, lct)
    screen.fill([255, 255, 255])
    screen.blit(fon7.image, fon7.rect)
    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 16)""").fetchall()
        name = name[0]
        if phrase == result[0][0]:
            leorio.pers()
        elif phrase == result[1][0]:
            screen.blit(fon7.image, fon7.rect)
            illumi.pers()
        elif phrase == result[2][0]:
            screen.blit(fon7.image, fon7.rect)
            gon.pers()
        elif phrase == result[3][0]:
            screen.blit(fon7.image, fon7.rect)
            leorio.pers()
        elif phrase == result[4][0]:
            screen.blit(fon7.image, fon7.rect)
            gon.pers()
        elif phrase == result[5][0]:
            screen.blit(fon7.image, fon7.rect)
            leorio.pers()
        elif phrase == result[6][0]:
            screen.blit(fon7.image, fon7.rect)
            gon.pers()
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    win1 = Button.Button()
    win1.create_button(screen, (124, 124, 124), 0, 500, 900 // 3, 200, 0, 'виноват Хисока', (255, 255, 255), 1)

    lose_1 = Button.Button()
    lose_1.create_button(screen, (124, 124, 124), 900 // 3, 500, 900 // 3, 200, 0, 'никто не виноват',
                         (255, 255, 255), 1)
    lose_2 = Button.Button()
    lose_2.create_button(screen, (124, 124, 124), 900 // 3 * 2, 500, 900 // 3, 200, 0, 'виноват Иллуми'
                                                                                       '(подставил Хисоку)',
                         (255, 255, 255), 1)
    while start:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    loadWindow(lct)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if win1.pressed(pos):
                    start = False
                    click.play()
                    win()
                if lose_1.pressed(pos):
                    start = False
                    click.play()
                    lose()
                if lose_2.pressed(pos):
                    start = False
                    click.play()
                    lose()


def dont_see_camera():
    start = True
    result = cur.execute("""SELECT replik FROM text WHERE location = 18""").fetchall()
    screen.fill([255, 255, 255])
    screen.blit(fon7.image, fon7.rect)
    lct = '17'
    unNoDialog = Dialog(screen, lct)

    for elem in result:
        phrase = elem[0]
        c = 85
        name = cur.execute(f"""SELECT hero_name FROM heroes WHERE hero_id =
                                (SELECT pers FROM text WHERE replik = ("{phrase}") AND location = 18)""").fetchall()
        name = name[0]
        if phrase == result[0][0]:
            leorio.pers()
        elif phrase == result[1][0]:
            screen.blit(fon7.image, fon7.rect)
            illumi.pers()
        elif phrase == result[2][0]:
            screen.blit(fon7.image, fon7.rect)
            leorio.pers()
        elif phrase == result[3][0]:
            screen.blit(fon7.image, fon7.rect)
            gon.pers()
        if len(phrase) > c:
            while phrase[:c][-1] != ' ':
                c -= 1
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,
                                  phrase[c:],)
            unNoDialog.show = True
            unNoDialog.sndNext()
        else:
            first = str(name[0]) + ': ' + phrase[:c]
            unNoDialog.message = (first,)
            unNoDialog.show = True
            unNoDialog.sndNext()
    win1 = Button.Button()
    win1.create_button(screen, (124, 124, 124), 0, 500, 900 // 3, 200, 0, 'виноват Хисока', (255, 255, 255), 1)

    lose_1 = Button.Button()
    lose_1.create_button(screen, (124, 124, 124), 900 // 3, 500, 900 // 3, 200, 0, 'никто не виноват',
                         (255, 255, 255), 1)
    lose_2 = Button.Button()
    lose_2.create_button(screen, (124, 124, 124), 900 // 3 * 2, 500, 900 // 3, 200, 0, 'виноват Иллуми'
                                                                                       '(подставил Хисоку)',
                         (255, 255, 255), 1)
    while start:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    loadWindow(lct)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if win1.pressed(pos):
                    start = False
                    click.play()
                    win()
                if lose_1.pressed(pos):
                    start = False
                    click.play()
                    lose()
                if lose_2.pressed(pos):
                    start = False
                    click.play()
                    lose()


def win():
    screen.fill([255, 255, 255])
    screen.blit(for_win, for_win_pos)
    unNoDialog = Dialog(screen, '17')
    unNoDialog.message = ("Киллуа: Спасибо что спасили меня.",)
    unNoDialog.show = True
    unNoDialog.sndNext()


def lose():
    screen.fill([255, 255, 255])
    screen.blit(for_lose.image, for_lose.rect)
    unNoDialog = Dialog(screen, '17')
    unNoDialog.message = ("Киллуа: :(.",)
    unNoDialog.show = True
    unNoDialog.sndNext()


def camera(number):
    screen.fill([255, 255, 255])
    screen.blit(rec.image, rec.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec2.image, rec2.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec3.image, rec3.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec4.image, rec4.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec5.image, rec5.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec6.image, rec6.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec7.image, rec7.rect)
    time.sleep(0.18)
    pygame.display.flip()
    screen.fill([255, 255, 255])
    screen.blit(rec8.image, rec8.rect)
    time.sleep(0.18)
    if int(number) == 11:
        after_camera()
    elif int(number) == 12 and videl_camera is False:
        dont_see_camera()
    elif int(number) == 12 and videl_camera is True:
        see_camera()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Novel")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 700))
    startWindow()
    pygame.quit()
