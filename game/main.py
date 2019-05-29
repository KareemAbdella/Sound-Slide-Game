import pygame

import BG
import road2
from BG2 import *
from movement import *

time_interval = 1  # try  2,5,7 msec

gameover1 = False
# To get full screen
user32 = ctypes.windll.user32
res = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
pygame.init()

background = pygame.image.load("header3.png")
icon = pygame.image.load("icon.png")
# noinspection PyInterpreter
introintro = pygame.image.load("intro_intro.png")

pygame.init()
pygame.mixer.music.load("Sneaky Snitch (Kevin MacLeod) - Gaming Background Music (HD).mp3")
pygame.mixer.music.play(1, 0)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Sound Slider')

white = (255, 255, 255)
black = (0, 0, 0)
light_black = (20, 20, 20)
red = (200, 0, 0)
mod_color = (238, 64, 13)
yellow = (200, 200, 0)
green = (34, 177, 76)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("Script MT Bold", 30)
medfont = pygame.font.SysFont("Arial", 60)
med_large_font = pygame.font.SysFont("Arial", 70)
largefont = pygame.font.SysFont("Arial", 85)


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "medlarge":
        textSurface = med_large_font.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()  # get mouse pos
    click = pygame.mouse.get_pressed()  # get moude actoin
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                # sys._clear_type_cache()
                maina()
            if action == "main":
                game_intro()
            if action == "cridet":
                cridet()
            if action == "pause":
                pause()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, mod_color, x, y, width, height)


def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(black) #  black background
        gameDisplay.blit(background, (0, 0))  # background is an image

        message_to_screen("Controls", red, -100, size="large")
        message_to_screen("It's Too Easy ...Just Using Arrows", mod_color, -30)
        message_to_screen("Move Right => arrow Right", mod_color, 10)
        message_to_screen("Move Left => arrow Left", mod_color, 50)
        message_to_screen("Pause => P", mod_color, 90)

        button("play", 150, 500, 130, 50, black, light_black, action="play")
        button("Main", 350, 500, 130, 50, black, light_black, action="main")
        button("quit", 550, 500, 130, 50, black, light_black, action="quit")

        pygame.display.update()

        clock.tick(15)  # FPS


def cridet():
    gcridet = True

    while gcridet:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(black)
        gameDisplay.blit(background, (0, 0))

        message_to_screen("BROUGHT TO YOU BY ...", red, -100, size="medium")
        message_to_screen("TEAM A.A", mod_color, -30)
        message_to_screen("SUPERVISION :", mod_color, 10)
        message_to_screen("DR. Mohamed Eita", black, 50, size="medium")

        button("play", 150, 500, 130, 50, black, light_black, action="play")
        button("Main", 350, 500, 130, 50, black, light_black, action="main")
        button("quit", 550, 500, 130, 50, black, light_black, action="quit")

        pygame.display.update()

        clock.tick(15)


def pause():
    paused = True
    message_to_screen("Paused", red, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", mod_color, 25)  # we can do it using button
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)  # less FPS => less # of operation => less rendering time


def game_intro():  # base intro func

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background, (0, 0))

        button("Play", 610, 220, 130, 50, black, light_black, action="play")
        button("Controls", 625, 290, 130, 50, black, light_black, action="controls")
        button("Cridet", 640, 360, 130, 50, black, light_black, action="cridet")
        button("Quit", 655, 430, 130, 50, black, light_black, action="quit")

        pygame.display.update()

        clock.tick(15)


def game_over():
    global gameover1, win
    best_score = 0

    pygame.mixer.music.stop()
    if win:
        pygame.mixer.music.load("win.mp3")
    if gameover1:
        pygame.mixer.music.load("Lay lay Music (Oficial mp3).mp3")
    pygame.mixer.music.play(-1)

    while gameover1 == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    gameover1 = False
                    maina()
        if win:
            message_to_screen("WIN THE GAME", red, -100, size="large")

        else:
            message_to_screen("GAME OVER", red, -100, size="large")
        if not win:
            message_to_screen("Your Score :" + str(movement.GetScore()), mod_color, 25)
        if movement.GetScore() > best_score:
            best_score = movement.GetScore()
        if not win:
            message_to_screen("Your Best :" + str(best_score), mod_color, 100, size="large")

        button("play Again", 150, 500, 130, 50, black, light_black, action="play")
        button("Main", 350, 500, 130, 50, black, light_black, action="main")
        button("quit", 550, 500, 130, 50, black, light_black, action="quit")
        clock.tick(5)  # less FPS => less # of operation => less rendering time
        pygame.display.update()


def drawText(string, xShift=0, yShift=0, scale=1.0, lineWidth=3):
    global win
    glLineWidth(lineWidth)
    if string == "Winner Winner Chicken dinner ":
        glColor(1, 1, 0)
    elif string == "Game Over":
        glColor(1, 0, 0)
    else:
        glColor(1, 1, 1)

    Display.orthoProjection()
    glPushMatrix()
    glLoadIdentity()
    glTranslate(xShift, yShift, 0)
    glScale(scale, scale, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

    glPopMatrix()


# ============================================================================================================= #

win = False


def Timer(v):
    my_Game()

    glutTimerFunc(time_interval, Timer, 1)


def camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 200)
    x = movement.getpo()
    k = x - 1
    l = (-pi + k * pi) / 4
    if x == 0 or x == 8:
        l = (-pi) / 4
        gluLookAt(0, 9, movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  0, 1, 0
                  )
    elif x == 1:

        gluLookAt(-6 * cos(45) - 2, 3 + 6 * sin(45),
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  -1, 1, 0
                  )
    elif x == 2:

        gluLookAt(-6 * cos(0), 3 + 6 * sin(0),
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  -1, 0, 0
                  )
    elif x == 3:

        gluLookAt(-6 * cos(45), 3 - 6 * sin(45) + 2,
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  -1, -1, 0
                  )
    elif x == 4:

        gluLookAt(0, -3,
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  0, -1, 0
                  )
    elif x == 5:

        gluLookAt(6 * cos(45) + 2, 3 - 6 * sin(45),
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  1, -1, 0
                  )
    elif x == 6:

        gluLookAt(6, 3,
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  1, 0, 0
                  )
    elif x == 7:
        gluLookAt(6 * cos(45) + 2, 3 + 6 * sin(45),
                  movement.GetPosition() + 10,
                  cos(l) * 3, 3 + sin(l) * 3, -10 + movement.GetPosition(),
                  1, 1, 0
                  )
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


class Display:
    WIDTH = res[0]
    HEIGHT = res[1]
    TITLE = b"Game"

    @staticmethod
    def init():
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GL_DEPTH)
        glutInitWindowSize(Display.WIDTH, Display.HEIGHT)
        glutCreateWindow(Display.TITLE)
        glutDisplayFunc(my_Game)
        glutIdleFunc(my_Game)
        glutSpecialFunc(movement.keyboard)

    @staticmethod
    def orthoProjection():
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, Display.WIDTH, 0, Display.HEIGHT)
        glMatrixMode(GL_MODELVIEW)


x = 0


def get_x():
    global x
    return x


def Collesionn():
    global win, gameover1, x

    if x == 1:
        game_over()
        sys.exit()

    if gg():
        gameover1 = True
        x += 1
    else:
        for i in range(32):

            if get_cool() == i and GetPosition() < -50 - (30 * i) and get_cool() >= get_coool():
                gameover1 = True
                x += 1
            elif get_coool() == i + 1 and GetPosition() > -30 + (-30 * i):
                gameover1 = True
                x += 1
    if gameover and x == 0:
        set_c()
    if movement.GetPosition() == -1010:
        win = True
        game_over()
    movement.drawmodelnaa()

    # for i in range(17, 32):
    #     if get_cool() == i and GetPosition() < -50 - (30 * i) and get_cool() >= get_coool():
    #         print("col")
    #     elif get_coool() == i + 1 and GetPosition() > -30 + (-30 * i):
    #         print("col")


def draw():
    global win, gameover1
    camera()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    BG.all_BG()
    road2.all_road()
    # الحتة المسئولة عن حركة الاوبجيكت
    x = movement.getpo()
    if x > 1:
        k = x - 1
        l = (-pi + k * pi) / 4

        glTranslate(cos(l) * 3, 3 + sin(l) * 3, 0)
    if x == 1:
        glTranslate(cos(-pi / 4) * 3, 3 + sin(-pi / 4) * 3, 0)
    Collesionn()
    if gg() or gameover1:
        set_c()
        drawText("Game Over", 100, 400, 0.7)

    if movement.GetPosition() < -1000:  # pygame.mixer.music.load("win.mp3")
        drawText("Winner Winner Chicken dinner ", 100, 400, 0.7)
    drawText("Score: " + str(movement.GetScore()), 10, 800, 0.25)

    glutSwapBuffers()


def my_Game():
    global gameover1
    if gameover1:
        pygame.mixer.music.stop()

    draw()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 200)
    gluLookAt(0, 9, 10,
              0, 0, -10,
              0, 1, -0.5
              )
    glClearColor(0, 0, 0.2, 1)


def maina():
    global gameover1
    # pygame.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound Slide Music - Level Select.mp3")
    pygame.mixer.music.play(-1)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()

    ##    gameDisplay.fill(black)  # the hole to the heart of the game
    pygame.display.update()
    clock.tick(5)
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GL_DEPTH)
    glutInitWindowSize(res[0], res[1])
    # glutInitWindowPosition(300, 0)
    glutCreateWindow(b"Sound Slide Game")
    myInit()
    glutDisplayFunc(my_Game)
    glutTimerFunc(time_interval, Timer, 1)
    # glutIdleFunc(my_Game)
    glutSpecialFunc(movement.keyboard)
    glutMainLoop()


# here run this fun to start the game game_intro()
game_intro()
