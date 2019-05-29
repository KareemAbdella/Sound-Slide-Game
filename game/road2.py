from OpenGL.GL import *
from math import *


def draw_road():  # draw single road
    glBegin(GL_POLYGON)
    glColor3f(0.941, 0.972, 1)
    # glColor3f(0,0.1,1)
    glVertex(0.5, 0, 0)
    glVertex(0.5, 0, -50)
    glVertex(-0.5, 0, -50)
    glVertex(-0.5, 0, 0)
    glEnd()


class Road:
    def __init__(self, x, y, z):  # x y z are the road axis
        self.x = x
        self.y = y
        self.z = z
        self.ID = 0

    def move_the_road(self):  # this function to translate the road along x y z

        glTranslate(self.x, self.y, self.z)

    def rotate_the_road(self, angle, around_x, around_y, around_z):
        glRotate(angle, around_x, around_y, around_z)

    def create(self, a):
        draw_road()

    def reset(self):
        glLoadIdentity()


# round one group
def anti_clock_wise_group(x=1):
    draw_road()
    road = []
    for i in range(0, 7):
        road.append(Road(cos((-pi + i * pi) / 4) * 3, 3 + sin((-pi + i * pi) / 4) * 3, -30 * (i + 1)))
        road[i].move_the_road()
        road[i].rotate_the_road(45 * (i + 1), 0, 0, 1)
        road[i].create(i + 1)
        road[i].reset()
    # draw_road()
    #
    # road_1 = Road(0 + cos(-pi / 4) * 3, 3 + sin(-pi / 4) * 3, -30)
    # road_1.move_the_road()
    # road_1.rotate_the_road(45, 0, 0, 1)
    # road_1.create(1)
    # road_1.reset()
    #
    # road_2 = Road(0 + cos(0) * 3, 3 + sin(0) * 3, -60)
    # road_2.move_the_road()
    # road_2.rotate_the_road(90, 0, 0, 1)
    # road_2.create(2)
    # road_2.reset()
    #
    # road_3 = Road(0 + cos(pi / 4) * 3, 3 + sin(pi / 4) * 3, -90)
    # road_3.move_the_road()
    # road_3.rotate_the_road(135, 0, 0, 1)
    # road_3.create(3)
    # road_3.reset()
    #
    # road_4 = Road(0 + cos(pi / 2) * 3, 3 + sin(pi / 2) * 3, -120)
    # road_4.move_the_road()
    # road_4.rotate_the_road(180, 0, 0, 1)
    # road_4.create(4)
    # road_4.reset()
    #
    # road_5 = Road(0 + cos(3 * pi / 4) * 3, 3 + sin(3 * pi / 4) * 3, -150)
    # road_5.move_the_road()
    # road_5.rotate_the_road(225, 0, 0, 1)
    # road_5.create(5)
    # road_5.reset()
    #
    # road_6 = Road(0 + cos(pi) * 3, 3 + sin(pi) * 3, -180)
    # road_6.move_the_road()
    # road_6.rotate_the_road(270, 0, 0, 1)
    # road_6.create(6)
    # road_6.reset()
    #
    # road_7 = Road(0 + cos(5 * pi / 4) * 3, 3 + sin(5 * pi / 4) * 3, -210)
    # road_7.move_the_road()
    # road_7.rotate_the_road(315, 0, 0, 1)
    # road_7.create(7)
    # road_7.reset()

    # road_8 = Road(0 + cos(3* pi / 2) * 3, 3 + sin(3 * pi / 2) * 3, go_z)
    # road_8.move_the_road()
    # road_8.rotate_the_road(360, 0, 0, 1)
    # road_8.create()
    # road_8.reset()


def clock_wise_group(x=0):
    road_1 = Road(0 + cos(6 * pi / 4) * 3, 3 + sin(3 * pi / 2) * 3, -240)
    road_1.move_the_road()
    road_1.rotate_the_road(360, 0, 0, 1)
    road_1.create(8)
    road_1.reset()

    road_2 = Road(0 - cos(-pi / 4) * 3, 3 + sin(-pi / 4) * 3, -270)
    road_2.move_the_road()
    road_2.rotate_the_road(-45, 0, 0, 1)
    road_2.create(9)
    road_2.reset()

    road_3 = Road(0 - cos(0) * 3, 3 + sin(0) * 3, -300)
    road_3.move_the_road()
    road_3.rotate_the_road(-90, 0, 0, 1)
    road_3.create(10)
    road_3.reset()

    road_4 = Road(0 - cos(pi / 4) * 3, 3 + sin(pi / 4) * 3, -330)
    road_4.move_the_road()
    road_4.rotate_the_road(-135, 0, 0, 1)
    road_4.create(11)
    road_4.reset()

    road_5 = Road(0 - cos(pi / 2) * 3, 3 + sin(pi / 2) * 3, -360)
    road_5.move_the_road()
    road_5.rotate_the_road(-180, 0, 0, 1)
    road_5.create(12)
    road_5.reset()

    road_6 = Road(0 - cos(3 * pi / 4) * 3, 3 + sin(3 * pi / 4) * 3, -390)
    road_6.move_the_road()
    road_6.rotate_the_road(-225, 0, 0, 1)
    road_6.create(13)
    road_6.reset()

    road_7 = Road(0 - cos(pi) * 3, 3 + sin(pi) * 3, -420)
    road_7.move_the_road()
    road_7.rotate_the_road(-270, 0, 0, 1)
    road_7.create(14)
    road_7.reset()

    road_8 = Road(0 - cos(5 * pi / 4) * 3, 3 + sin(5 * pi / 4) * 3, -450)
    road_8.move_the_road()
    road_8.rotate_the_road(-315, 0, 0, 1)
    road_8.create(15)
    road_8.reset()


# round two group
def distant_anti_clock_wise_group(x=0):
    road_1 = Road(0 + cos(3 * pi / 2) * 3, 3 + sin(3 * pi / 2) * 3, -480)
    road_1.move_the_road()
    road_1.rotate_the_road(360, 0, 0, 1)
    road_1.create(16)
    road_1.reset()

    road_2 = Road(0 + cos(-pi / 4) * 3, 3 + sin(-pi / 4) * 3, -510)
    road_2.move_the_road()
    road_2.rotate_the_road(45, 0, 0, 1)
    road_2.create(17)
    road_2.reset()

    road_3 = Road(0 + cos(0) * 3, 3 + sin(0) * 3, -540)
    road_3.move_the_road()
    road_3.rotate_the_road(90, 0, 0, 1)
    road_3.create(18)
    road_3.reset()

    road_4 = Road(0 + cos(pi / 4) * 3, 3 + sin(pi / 4) * 3, -570)
    road_4.move_the_road()
    road_4.rotate_the_road(135, 0, 0, 1)
    road_4.create(19)
    road_4.reset()

    road_5 = Road(0 + cos(pi / 2) * 3, 3 + sin(pi / 2) * 3, -600)
    road_5.move_the_road()
    road_5.rotate_the_road(180, 0, 0, 1)
    road_5.create(21)
    road_5.reset()

    road_6 = Road(0 + cos(3 * pi / 4) * 3, 3 + sin(3 * pi / 4) * 3, -630)
    road_6.move_the_road()
    road_6.rotate_the_road(225, 0, 0, 1)
    road_6.create(21)
    road_6.reset()

    road_7 = Road(0 + cos(pi) * 3, 3 + sin(pi) * 3, -660)
    road_7.move_the_road()
    road_7.rotate_the_road(270, 0, 0, 1)
    road_7.create(22)
    road_7.reset()

    road_8 = Road(0 + cos(5 * pi / 4) * 3, 3 + sin(5 * pi / 4) * 3, -690)
    road_8.move_the_road()
    road_8.rotate_the_road(315, 0, 0, 1)
    road_8.create(23)
    road_8.reset()

    # road_8 = Road(0 + cos(3* pi / 2) * 3, 3 + sin(3 * pi / 2) * 3, go_z)
    # road_8.move_the_road()
    # road_8.rotate_the_road(360, 0, 0, 1)
    # road_8.create()
    # road_8.reset()


def distant_clock_wise_group():
    road_1 = Road(0 + cos(3 * pi / 2) * 3, 3 + sin(3 * pi / 2) * 3, -720)
    road_1.move_the_road()
    road_1.rotate_the_road(360, 0, 0, 1)
    road_1.create(24)
    road_1.reset()

    road_2 = Road(0 - cos(-pi / 4) * 3, 3 + sin(-pi / 4) * 3, -750)
    road_2.move_the_road()
    road_2.rotate_the_road(-45, 0, 0, 1)
    road_2.create(25)
    road_2.reset()

    road_3 = Road(0 - cos(0) * 3, 3 + sin(0) * 3, -780)
    road_3.move_the_road()
    road_3.rotate_the_road(-90, 0, 0, 1)
    road_3.create(26)
    road_3.reset()

    road_4 = Road(0 - cos(pi / 4) * 3, 3 + sin(pi / 4) * 3, -810)
    road_4.move_the_road()
    road_4.rotate_the_road(-135, 0, 0, 1)
    road_4.create(27)
    road_4.reset()

    road_5 = Road(0 - cos(pi / 2) * 3, 3 + sin(pi / 2) * 3, -840)
    road_5.move_the_road()
    road_5.rotate_the_road(-180, 0, 0, 1)
    road_5.create(28)
    road_5.reset()

    road_6 = Road(0 - cos(3 * pi / 4) * 3, 3 + sin(3 * pi / 4) * 3, -870)
    road_6.move_the_road()
    road_6.rotate_the_road(-225, 0, 0, 1)
    road_6.create(29)
    road_6.reset()

    road_7 = Road(0 - cos(pi) * 3, 3 + sin(pi) * 3, -900)
    road_7.move_the_road()
    road_7.rotate_the_road(-270, 0, 0, 1)
    road_7.create(30)
    road_7.reset()

    road_8 = Road(0 - cos(5 * pi / 4) * 3, 3 + sin(5 * pi / 4) * 3, -930)
    road_8.move_the_road()
    road_8.rotate_the_road(-315, 0, 0, 1)
    road_8.create(31)
    road_8.reset()


# end level
def final_road():
    final = Road(0 + cos(3 * pi / 2) * 3, 3 + sin(3 * pi / 2) * 3, -960)
    final.move_the_road()
    final.rotate_the_road(360, 0, 0, 1)
    final.create(32)
    final.reset()


def all_road():
    # the three groups(CW, anti CW) are for round one
    anti_clock_wise_group()  # starts at z =0     && ends at z = -240
    clock_wise_group()  # starts at z = -240 && ends at z = -450

    # the next three groups((same roads but with distant spaces between tiles)) are for round two
    # the speed will increase in round two
    distant_anti_clock_wise_group()  # starts at z = -480 && ends at z= -720
    distant_clock_wise_group()  # starts at z = -760 && ends at z = -1040
    # final
    final_road()