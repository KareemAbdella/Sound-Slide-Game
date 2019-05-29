import random
from OpenGL.GL import *
from OpenGL.GLUT import *

forward = 0


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
        forward += 0.05


def moon():
    global foward
    glColor3f(1, 1, 1)
    glTranslate(-20, 10, -50 - forward)
    glutSolidSphere(2.5,100,100)
    glLoadIdentity()


def mountain1(z):
    global forward
    glColor3f(0, 0, 0.1)
    glTranslate(-18, 2, -30 - z - forward)
    glutSolidSphere(4.25, 200, 200)
    glLoadIdentity()
    glTranslate(-18, -5, -30 - z - forward)
    glScale(1, 3.25, 2)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(-13.5, -15, -35 - z - forward)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 20, 200, 200)
    glLoadIdentity()
    glTranslate(-20, -15, -32.5 - z - forward)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 17, 200, 200)
    glLoadIdentity()


def mountain2(z):
    global forward
    glColor3f(0, 0, 0.1)
    glTranslate(18, 2, -30 - z - forward)
    glutSolidSphere(4.25, 200, 200)
    glLoadIdentity()
    glTranslate(18, -5, -30 - z - forward)
    glScale(1, 3.25, 2)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(19, -15, -35 - z - forward)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 19, 200, 200)
    glLoadIdentity()
    glTranslate(25, -15, -32.5 - z - forward)
    glRotate(90, -6, -1, 0)
    glutSolidCone(10, 20, 200, 200)
    glLoadIdentity()


def tree1(z):
    global forward
    glColor3f(0, 0, 0)
    glTranslate(17, -10, -30 - z - forward)
    glScale(0.1, 5, 1)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glColor3f(0, 0.1, 0)
    glTranslate(18, 2, -30 - z - forward)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(16, 1.5, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(19, 1, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(16, 3, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(18, 3, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()


rod = 0


def tree2(z):
    global forward
    glColor3f(0, 0, 0)
    glTranslate(-17, -10, -30 - z - forward)
    glScale(0.1, 5, 1)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glColor3f(0, 0.1, 0)
    glTranslate(-18, 2, -30 - z - forward)
    glutSolidSphere(2.3, 200, 200)
    glLoadIdentity()
    glTranslate(-16, 1.5, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-19, 1, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-16, 3, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()
    glTranslate(-18, 3, -30 - z - forward)
    glutSolidSphere(2, 200, 200)
    glLoadIdentity()


def all_BG():
    moon()
    mountain1(30)
    mountain2(30)
    tree1(0)
    tree2(0)
    stars()
