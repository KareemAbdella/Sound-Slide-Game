from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import random

forward = 0
angle = 0
Flash = 0


def stars():
    global forward
    glLineWidth(2.5)
    glColor3f(1, 1, 1)
    for i in range(0, 10):
        px = random.randrange(-12, 12)
        py = random.randrange(0, 10)
        glBegin(GL_LINES)
        glVertex(px, py, -forward)
        glVertex(px, py, -0.75 - forward)
        glEnd()
        glLoadIdentity()
    if forward < 11:
        forward += 0.0005
    else:
        forward = 0


def moon():
    glColor3f(1, 1, 1)
    glTranslate(-20, 10, -50)
    glutSolidSphere(2.5, 200, 200)
    glLoadIdentity()


def mountain1(z):
    glColor3f(0.1, 0.1, 0.2)
    glTranslate(-18, 2, -30 - z)
    glutSolidSphere(4, 200, 200)
    glLoadIdentity()
    glTranslate(-18, -5, -30 - z)
    glScale(1, 3.25, 2)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(-13.5, -15, -35 - z)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 20, 200, 200)
    glLoadIdentity()
    glTranslate(-20, -15, -32.5 - z)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 17, 200, 200)
    glLoadIdentity()


def mountain2(z):
    glColor3f(0.1, 0.1, 0.2)
    glTranslate(18, 2, -30 - z)
    glutSolidSphere(4, 200, 200)
    glLoadIdentity()
    glTranslate(18, -5, -30 - z)
    glScale(1, 3.25, 2)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(19, -15, -35 - z)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 19, 200, 200)
    glLoadIdentity()
    glTranslate(25, -15, -32.5 - z)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 20, 200, 200)
    glLoadIdentity()


def tree1(z):
    glColor3f(0.2, 0.1, 0)
    glTranslate(17, -10, -30 - z)
    glScale(0.1, 5, 1)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glColor3f(0, 0.3, 0)
    glTranslate(18, 2, -30 - z)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(16, 1.5, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(19, 1, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(16, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(18, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glColor3f(0.2, 0.1, 0)
    glTranslate(22, -10, -30 - z)
    glScale(0.1, 5, 1)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glColor3f(0, 0.3, 0)
    glTranslate(23, 2, -30 - z)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(21, 1.5, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(24, 1, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(21, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(23, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()


def tree2(z):
    glColor3f(0.2, 0.1, 0)
    glTranslate(-17, -10, -30 - z)
    glScale(0.1, 5, 1)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glColor3f(0, 0.3, 0)
    glTranslate(-18, 2, -30 - z)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(-16, 1.5, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-19, 1, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-16, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-18, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glColor3f(0.2, 0.1, 0)
    glTranslate(-22, -10, -30 - z)
    glScale(0.1, 5, 1)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glColor3f(0, 0.3, 0)
    glTranslate(-23, 2, -30 - z)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(-21, 1.5, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-24, 1, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-21, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-23, 3, -30 - z)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()


def tree3(z):
    glColor3f(0, 0.1, 0)
    glTranslate(17, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(16, -9, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(19, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(16, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(18, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(21, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(20, -9, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(23, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(20, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(22, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(12, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(11, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(14, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(13, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(3, 200, 200)
    glLoadIdentity()
    glTranslate(15, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()


def tree4(z):
    glColor3f(0, 0.1, 0)
    glTranslate(-17, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(-16, -9, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-19, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-16, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-18, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-21, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(-20, -9, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-23, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-20, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-22, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-12, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(-11, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-14, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-13, -11, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(3, 200, 200)
    glLoadIdentity()
    glTranslate(-15, -10, -30 - z)
    glScale(1, 1, 0.01)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()


def tower1(z):
    global angle
    global Flash
    glColor3f(0.2, 0, 0)
    glTranslate(-18, -5, -30 - z)
    glScale(0.5, 2.5, 0.5)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0.7 + Flash, 0.3 + Flash, Flash)
    glTranslate(-18, 4, -30 - z)
    glRotate(angle, 0, 0, 1)
    glutWireSphere(1.5, 8, 8)
    glLoadIdentity()


def tower2(z):
    global angle
    global Flash
    glColor3f(0.2, 0, 0)
    glTranslate(18, -5, -30 - z)
    glScale(0.5, 2.5, 0.5)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0.7 + Flash, 0.3 + Flash, Flash)
    glTranslate(18, 4, -30 - z)
    glRotate(angle, 0, 0, 1)
    glutWireSphere(1.5, 8, 8)
    glLoadIdentity()
    angle -= 0.5
    if 0.3 >= Flash >= 0:
        Flash += 0.05
        if Flash >= 0.3:
            Flash = 0


def house1(z):
    glColor3f(0, 0, 0.2)
    glTranslate(-18, -5, -30 - z)
    glScale(3.5, 3.5, 8.5)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0.7, 0.9, 0)
    glTranslate(-2, 6.3, -0.25 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(2)
    glLoadIdentity()
    glLoadIdentity()
    glColor3f(0.7, 0.9, 0)
    glTranslate(-3, 5, 3 - 0.35 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(3)
    glLoadIdentity()


def house2(z):
    glColor3f(0, 0, 0.2)
    glTranslate(18, -5, -30 - z)
    glScale(3.5, 3.5, 8.5)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0.7, 0.9, 0)
    glTranslate(2, 6.3, - 0.25 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(2)
    glLoadIdentity()
    glLoadIdentity()
    glColor3f(0.7, 0.9, 0)
    glTranslate(3, 5, 3 - 0.35 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(3)
    glLoadIdentity()


def house3(z):
    glColor3f(0.2, 0.4, 0.3)
    glTranslate(-18, -5, -30 - z)
    glScale(4, 6, 9)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(-2, 4, -0.25 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(2)
    glLoadIdentity()
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(-3, 2, 3 - 0.35 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(3)
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(-2, 7.3, -0.25 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(2)
    glLoadIdentity()
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(-3, 6.5, 3 - 0.35 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(3)
    glLoadIdentity()


def house4(z):
    glColor3f(0.2, 0.4, 0.3)
    glTranslate(18, -5, -30 - z)
    glScale(4, 6, 9)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(2, 4, -0.25 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(2)
    glLoadIdentity()
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(3, 2, 3 - 0.35 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(3)
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(2, 7.3, -0.25 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(2)
    glLoadIdentity()
    glLoadIdentity()
    glColor3f(0.8, 0.8, 0)
    glTranslate(3, 6.5, 3 - 0.35 * z)
    glScale(0.01, 1, 1)
    glutSolidCube(3)
    glLoadIdentity()


def tower3(z):
    glColor3f(0.1, 0.1, 0.1)
    glTranslate(-18.8, 2, -30 - z)
    glutSolidSphere(3.5, 200, 200)
    glLoadIdentity()
    glTranslate(-18, -15, -35 - z)
    glRotate(90, -6, -1, 0)
    glutSolidCone(6, 20, 6, 200)
    glLoadIdentity()


def tower4(z):
    glColor3f(0.1, 0.1, 0.1)
    glTranslate(20, 2, -30 - z)
    glutSolidSphere(3.5, 200, 200)
    glLoadIdentity()
    glTranslate(24, -15, -35 - z)
    glRotate(90, -6, -1, 0)
    glutSolidCone(5, 20, 6, 200)
    glLoadIdentity()


def FULL():
    tower1(1600)
    tower2(1600)
    tower4(1550)
    tower3(1540)
    tower4(1530)
    tower3(1520)
    tower4(1510)
    tower3(1500)
    tower4(1490)
    tower3(1480)
    tower4(1470)
    tower3(1460)
    mountain2(1400)
    mountain1(1350)
    mountain2(1300)
    mountain1(1250)
    mountain2(1200)
    tree3(1145)
    tree4(1145)
    tree3(1130)
    tree4(1130)
    tree3(1115)
    tree4(1115)
    tree3(1100)
    tree4(1100)
    tree3(1085)
    tree4(1185)
    tree3(1160)
    tree4(1160)
    house3(1050)
    house4(1050)
    house3(970)
    house4(910)
    house3(850)
    house4(790)
    house3(730)
    house4(670)
    house3(810)
    house4(650)
    tower1(600)
    tower2(600)
    house2(500)
    house1(480)
    house2(440)
    house1(430)
    house2(390)
    house1(370)
    house2(330)
    house1(320)
    mountain1(250)
    mountain2(250)
    mountain1(180)
    mountain2(180)
    mountain1(110)
    mountain2(110)
    tree1(40)
    tree2(40)
    tree1(34)
    tree2(34)
    tree1(28)
    tree2(28)
    tower1(0)
    tower2(0)
