# RIVERA A702
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("04 TP 1 - Juan Rafael F. Rivera")
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslate(0,0,-30)

yangle = 180

vertices = (
    (0,3,0),
    (0,0,-2),
    (2,0,0),
    (0,0,2),
    (-2,0,0),
    (0,-3,0)
)

colours = (
    (1,0,0),
    (0,1,0),
    (1,1,0),
    (0,0,1),
    (1,0,1),
    (0,1,1),
    (1,1,1),
    (0.1,0.1,0.1)
)

edges = (
    (0,1,2),
    (0,1,4),
    (0,2,3),
    (0,3,4),
    (5,1,2),
    (5,1,4),
    (5,2,3),
    (5,3,4)
)


def draw_cube():
    glBegin(GL_TRIANGLES)
    colour_index = 0
    colour_change = False
    for edge in edges:
        glColor3f(colours[colour_index][0],colours[colour_index][1],colours[colour_index][2])
        for vertex in edge:
            glVertex3f(vertices[vertex][0],vertices[vertex][1],vertices[vertex][2])
        colour_index = colour_index + 1
    glEnd()

movex = 0
movey = 0
movez = 0
rotx = 0
roty = 0
rotz = 0
speed = 1
scaleup = False
scaledown = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movex = -0.5
            if event.key == pygame.K_d:
                movex = 0.5
            if event.key == pygame.K_w:
                movey = 0.5
            if event.key == pygame.K_s:
                movey = -0.5
            if event.key == pygame.K_q:
                movez = 0.5
            if event.key == pygame.K_e:
                movez = -0.5
            if event.key == pygame.K_l:
                rotx = 1
            if event.key == pygame.K_j:
                rotx = -1
            if event.key == pygame.K_i:
                roty = 1
            if event.key == pygame.K_k:
                roty = -1
            if event.key == pygame.K_u:
                rotz = 1
            if event.key == pygame.K_o:
                rotz = -1
            if event.key == pygame.K_x:
                speed = speed + 1
            if event.key == pygame.K_z:
                speed = speed - 1
            if event.key == pygame.K_n:
                scaleup = True
            if event.key == pygame.K_m:
                scaledown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movex = 0
            if event.key == pygame.K_d:
                movex = 0
            if event.key == pygame.K_w:
                movey = 0
            if event.key == pygame.K_s:
                movey = 0
            if event.key == pygame.K_q:
                movez = 0
            if event.key == pygame.K_e:
                movez = 0
            if event.key == pygame.K_j:
                rotx = 0
            if event.key == pygame.K_l:
                rotx = 0
            if event.key == pygame.K_i:
                roty = 0
            if event.key == pygame.K_k:
                roty = 0
            if event.key == pygame.K_u:
                rotz = 0
            if event.key == pygame.K_o:
                rotz = 0
            if event.key == pygame.K_n:
                scaleup = False
            if event.key == pygame.K_m:
                scaledown = False
    glTranslatef(movex,movey,movez)
    glRotatef(speed,roty,rotx,rotz)
    if scaleup == True:
        glScale(1.1,1.1,1.1)
    if scaledown == True:
        glScale(0.9,0.9,0.9)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(15)
