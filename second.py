from pygame import *
import random
from json import *

points = 0
font.init()
font1 = font.SysFont('Arial', 20)
font2 = font.SysFont('TimesNewRoman', 100)
font3 = font.SysFont('TimesNewRoman', 50)
mixer.init()
teleport = mixer.Sound('zvuk-pri-teleportatsii.ogg')


class GameSprite(sprite.Sprite):
    def __init__(self, speed, pl_image, x, y, width, height):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.startpoint = y
        self.jumpCount = 10
        self.isJump = False

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    global af

    def update(self):
        pass


class Asteroid(GameSprite):
    pass


asteroid = Asteroid(10, 'астероид.png', 700, 0, 100, 100)
af = 2
player = Player(0, 'герой.png', 100, 150, 100, 150)
window = display.set_mode((700, 500))
display.set_caption('SpaceRunner')
display.set_icon(image.load('герой.png'))
clock = time.Clock()
bg = transform.scale(image.load('фон.png'), (700, 500))
proval = font2.render('You lose', True, (255, 0, 0))
gf = 1
gfold = 0
timer = 0
game = True
red, green, blue = 0, 0, 0
everytick = 0
increse = True
not_started = True
pause = False
once = False
once2 = False
pausef = font2.render('Pause', True, (255, 255, 255))
escape = False
next = False
nexte = font2.render('Continue', True, (255, 255, 255))
music = True
mixer_music.load('spacemusic.mp3')
once3 = False
once4 = False
settings = font2.render('Settings', True, (255, 255, 255))
how_to_play1 = False
how_to_play = font2.render('How to play?', True, (255, 255, 255))
text_for_howToplayw = font3.render('W - Up', True, (255, 255, 255))
text_for_howToplays = font3.render('S - Down', True, (255, 255, 255))
text_for_howToplayesc = font3.render('ESC - Settings', True, (255, 255, 255))
text_for_howToplayspace = font3.render('SPACE - Pause', True, (255, 255, 255))
text_for_howToplayr = font3.render('R - Restart, only if you lose', True, (255, 255, 255))
back = font3.render('Back', True, (255, 255, 255))
efect = True
once5 = False
canpress = True
canclick = True
canclick2 = True
while True:
    if not_started and not escape:
        canclick = False
    if not_started and escape:
        canclick = True
    if not not_started and not escape:
        canclick = False
    if not not_started and escape:
        canclick = True
    if not_started and not escape:
        canclick2 = False
    if not_started and escape:
        canclick2 = True
    if not not_started and not escape:
        canclick2 = False
    if not not_started and escape:
        canclick2 = True
    if music:
        if not once3:
            mixer_music.unpause()
            mixer_music.play(-1)
            once3 = True
    if not music:
        once3 = False
        mixer_music.pause()
    if pause and not_started != True:
        window.blit(pausef, (200, 200))
    if not_started:
        click_here = font2.render('Start', True, (255, 255, 255))
        window.blit(bg, (0, 0))
        window.blit(click_here, (250, 200))
        window.blit(settings, (175, 300))
    if escape and not pause:
        window.blit(bg, (0, 0))
        window.blit(nexte, (150, 0))
        window.blit(how_to_play, (150, 200))
        if music:
            musicb = font2.render('Music on', True, (0, 255, 0))
            window.blit(musicb, (150, 100))
        if not music:
            musicb = font2.render('Music off', True, (255, 0, 0))
            window.blit(musicb, (150, 100))
        if efect:
            efectb = font2.render('Efects on', True, (0, 255, 0))
            window.blit(efectb, (150, 300))
        if not efect:
            efectb = font2.render('Efects off', True, (255, 0, 0))
            window.blit(efectb, (150, 300))
        next = True
        if how_to_play1:
            window.blit(bg, (0, 0))
            window.blit(text_for_howToplayw, (100, 0))
            window.blit(text_for_howToplays, (100, 100))
            window.blit(text_for_howToplayesc, (100, 200))
            window.blit(text_for_howToplayspace, (100, 300))
            window.blit(text_for_howToplayr, (100, 400))
            window.blit(back, (500, 0))

    if not game:
        pause = False
        window.blit(bg, (0, 0))
        press_restart = font2.render('Press r to restart', True, (red, green, blue))
        window.blit(proval, (150, 175))
        window.blit(press_restart, (50, 275))
        everytick += 1
        if everytick >= 1:
            if red <= 0 or green <= 0 or blue <= 0:
                increse = True

            if red >= 255 or green >= 255 or blue >= 255:
                increse = False

            if increse:
                red += 1
                green += 1
                blue += 1
            if not increse:
                red -= 1
                green -= 1
                blue -= 1
        with open('best for second.json', 'r', encoding='utf-8') as file:
            ded = load(file)
            if int(ded['Points']) < points:
                ded = {'Points': points}
                with open('best for second.json', 'w', encoding='utf-8') as file2:
                    dump(ded, file2)
    if not escape:
        if not pause:

            if game and not_started == False:
                timer += 1
                if timer >= 120:
                    asteroid.speed += 1
                    timer = 0
                window.blit(bg, (0, 0))
                point = font1.render(str(points), True, (255, 255, 255))
                window.blit(point, (650, 50))
                asteroid.reset()
                player.reset()
                with open('best for second.json', 'r', encoding='utf-8') as file:
                    ded = load(file)
                    if int(ded['Points']) < points:
                        ded = {'Points': points}
                        with open('best for second.json', 'w', encoding='utf-8') as file2:
                            dump(ded, file2)
                with open('best for second.json', 'r', encoding='utf-8') as file:
                    ded = load(file)
                    bestpoint = font1.render(str(ded['Points']), True, (255, 255, 255))
                    window.blit(bestpoint, (650, 100))
                if gf == 1:
                    asteroid.rect.y = 0
                if gf == 2:
                    asteroid.rect.y = 150
                if gf == 3:
                    asteroid.rect.y = 350
                asteroid.rect.x -= asteroid.speed
                if asteroid.rect.x <= 0:
                    gfold = gf
                    if gfold == 1:
                        gf = random.randint(2, 3)
                    elif gfold == 2:
                        b = random.randint(1, 2)
                        if b == 1:
                            gf = 1
                        if b == 2:
                            gf = 3
                    elif gfold == 3:
                        gf = random.randint(1, 2)
                    asteroid.rect.x = 700
                    points += 1
                if player.rect.y == 150:
                    af = 2
                if player.rect.y == 350:
                    af = 3
                if player.rect.y == 0:
                    af = 1
    for e in event.get():
        if e.type == QUIT:
            with open('best for second.json', 'r', encoding='utf-8') as file:
                ded = load(file)
                if int(ded['Points']) < points:
                    ded = {'Points': points}
                    with open('best for second.json', 'w', encoding='utf-8') as file2:
                        dump(ded, file2)
            exit()
        if e.type == MOUSEBUTTONDOWN:
            if e.pos[0] >= 249 and e.pos[0] <= 446 and e.pos[1] >= 213 and e.pos[1] <= 296 and e.pos[0] >= 253 and \
                    e.pos[1] <= 292 and not_started and not how_to_play1 and not escape:
                not_started = False
            if e.pos[0] >= 153 and e.pos[0] <= 518 and e.pos[1] >= 16 and e.pos[1] <= 97 and e.pos[0] >= 144 and \
                    e.pos[1] <= 97 and escape and not how_to_play1:
                once2 = False
                escape = False
                canpress = True

            if e.pos[0] >= 138 and e.pos[0] <= 535 and e.pos[1] >= 106 and e.pos[1] <= 195 and e.pos[0] >= 139 and \
                    e.pos[1] <= 195 and escape and not how_to_play1:
                if music and once3:
                    music = False
                if not music and not once3:
                    music = True
            if e.pos[0] >= 175 and e.pos[0] <= 508 and e.pos[1] >= 313 and e.pos[1] <= 411 and e.pos[0] >= 173 and \
                    e.pos[1] <= 411 and canpress and not_started:
                if once2 == False:
                    escape = True
                    once2 = True
                    canpress = False
                elif once2:
                    escape = False
                    once2 = False
                    canpress = True
            if e.pos[0] >= 145 and e.pos[0] <= 686 and e.pos[1] >= 211 and e.pos[1] <= 296 and e.pos[0] >= 141 and \
                    e.pos[1] <= 296 and not how_to_play1 and canclick:
                if not once4:
                    how_to_play1 = True
                    once4 = True


                elif once4:
                    how_toPlay1 = False
                    once4 = False
            if e.pos[0] >= 496 and e.pos[0] <= 605 and e.pos[1] >= 4 and e.pos[1] <= 50:
                how_to_play1 = False
                once4 = False
            if e.pos[0] >= 139 and e.pos[0] <= 531 and e.pos[1] >= 307 \
                    and e.pos[1] <= 395 and escape and not how_to_play1 and canclick2:
                if not once5:

                    efect = True
                    once5 = True
                elif once5:

                    efect = False
                    once5 = False
        if e.type == KEYDOWN:
            if not pause and not escape and not canclick and not not_started:
                if e.key == K_w:
                    if efect:
                        teleport.play()
                    if af == 1:
                        player.rect.y = 0
                    if af == 2:
                        player.rect.y = 0
                    if af == 3:
                        player.rect.y = 150
                if e.key == K_s:
                    if efect:
                        teleport.play()
                    if af == 1 :
                        player.rect.y = 150
                    if af == 2:
                        player.rect.y = 350
                    if af == 3:
                        player.rect.y = 350
                if e.key == K_r and not game:
                    game = True
                    asteroid.kill()
                    player.kill()
                    player = Player(0, 'герой.png', 100, 150, 100, 150)
                    asteroid = Asteroid(10, 'астероид.png', 700, 0, 100, 100)
                    af = 2
                    gf = random.randint(1, 3)
                    red, green, blue = 0, 0, 0
                    not_started = True
                    points = 0
            if e.key == K_ESCAPE:
                if once2 == False:
                    escape = True
                    once2 = True
                    how_to_play1 = False
                    once4 = False
                    canpress = False
                elif once2:
                    escape = False
                    once2 = False
                    how_to_play1 = False
                    once4 = False
                    canpress = True
            if e.key == K_SPACE:
                if once == False and not_started != True:
                    pause = True
                    once = True
                elif once and not_started != True:
                    pause = False
                    once = False
        if e.type == KEYUP:
            pass
    if sprite.collide_rect(player, asteroid):
        game = False

    clock.tick(60)
    display.update()
