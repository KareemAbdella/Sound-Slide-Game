import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *


def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_MODELVIEW)

    texture = glGenTextures(5)

    imgload = pygame.image.load("coin_01.png")

    img_raw = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()

    print(width)
    print(height)

    glBindTexture(GL_TEXTURE_2D, texture[0])

    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE,
                 img_raw)  # set the image to the texture object texture[0]

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texture[0])


def draw():
    glColor(1, 1, 1)

    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-0.75, -0.75, 0)

    glTexCoord(1, 0)
    glVertex(0.75, -0.75, 0)

    glTexCoord(1, 1)
    glVertex(0.75, 0.75, 0)

    glTexCoord(0, 1)
    glVertex(-0.75, 0.75, 0)

    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Texture")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()


main()
