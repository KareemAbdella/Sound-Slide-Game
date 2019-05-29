from model import *

z = 0
move = 0
score = 0
Lol = 0
L = 0
col = 0
gameover = False
n_RotateObg = 0
right = left = 0


def gg():
    # function to set the gameover situation
    global gameover
    if gameover:
        print ("col")
        return True
    else:
        return False


def GetScore():
    # function to get the score
    global score
    return score


def GetPosition():
    # function to get the position in z-axis
    global z
    return z


def getpo():
    # Function to handle the translate of object and camera position
    # الفانكشن اللي اسمها روتيشن بتدور انما الفانكشن دي اللي بتخليه يتنقل من مكان للتاني
    global L
    return L


def get_cool():
    # function to handle the coll
    global col
    return col


def getRotate():
    # function to handle the rotate angle of the object
    global n_RotateObg
    return n_RotateObg


def drawmodelnaa():
    global z
    draw_model()
    z -= 0.5


def get_coool():
    # دي قيمة استخدمتها في حالة واحده في الاول خالص عشان كان فيها ايرور ف احتجت اكتبها
    global Lol
    return Lol


def keyboard(key, x, y):
    global col, gameover, right, left
    global n_RotateObg, L
    global score, Lol
    var = col

    if key == GLUT_KEY_RIGHT:
        if ((right == 8 and left == 1) or (score != 0 and left % 8 != 0)):
            gameover = True
        right += 1
        Lol += 1
        col += 1
        L += 1
        n_RotateObg += 1
        score += 1
        if col < var or col == 9:
            gameover = True

    elif key == GLUT_KEY_LEFT:
        if right % 8 != 0:
            gameover = True
        left += 1
        Lol += 1
        col -= 1
        L -= 1
        n_RotateObg -= 1
        score += 1
        if col == -1 and Lol == 1:
            gameover = True
        if col > var:
            gameover = True
