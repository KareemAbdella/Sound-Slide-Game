from OpenGL.GL import *
from OpenGL.GLUT import *
import movement

angleMINE = 0

CHANGE_COLOR = 0
xx = 0


def set_c():
    global xx
    xx = 1


def x():
    global angleMINE, z, xx
    global CHANGE_COLOR
    z = movement.GetPosition()
    # ناقص جلوبال الحاجات اللي بتلففه لو هتحطها هنا
    # + اقرى كومنت الفانكشن اللي بعد دي
    glColor3f(1, CHANGE_COLOR, CHANGE_COLOR)
    glTranslate(-z, 0.5, 0)  # TRANSLATE IN RESPONSE TO
    glRotate(angleMINE, 0, 1, 0)  # TO ROTATE
    glRotate(90, 1, 0, 0)  # TO DRAW OUR TOURUS IN WANTED VIEW " قبل كدة كان بيترسم عمودي مش نايم على الارضية "

    glutSolidTorus(0.2, 1.2, 5, 5)

    glColor3f(1, 0, 0)
    if xx:
        glColor3f(0, 0, 0)
    glutSolidSphere(0.5, 10, 10)
    if 1 >= CHANGE_COLOR >= 0:
        CHANGE_COLOR += 0.05
        if CHANGE_COLOR >= 1:
            CHANGE_COLOR = 0
    angleMINE += 3  # HERE THE ANGLE TO ROTATE THE TORUS


def draw_model():
    # مستخدم الروتيت هنا عشان انا فوق كنت برسم الموديل بيتحرك في x والحركة بتاعتنا كلها في z بس
    # ف أي تعديل فوق في دوران الموديل على الطريق ولا حاجة هتبقى x بدل z وهي هنا هتتغير تلقائي
    n = movement.getRotate()
    glRotate(n * 45, 0, 0, 1)
    glRotate(90, 0, 1, 0)
    x()
