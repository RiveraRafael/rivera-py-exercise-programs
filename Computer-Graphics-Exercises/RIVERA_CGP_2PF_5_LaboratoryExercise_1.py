# RIVERA A702
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("05 Lab 1 - Juan Rafael F. Rivera")
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslate(0,0,-20)

vertices = (
    (1,1,1),
    (1,1,-1),
    (1,-1,-1),
    (1,-1,1),
    (-1,1,1),
    (-1,-1,-1),
    (-1,-1,1),
    (-1,1,-1)
)

colours = (
    (0,0.25,0),
    (0,0.50,0),
    (0,0.75,0),
    (0,1,0)
)

edges = (
    (0,1,2),
    (0,2,3),
    (0,1,7),
    (0,4,7),
    (2,3,5),
    (3,5,6),
    (5,6,7),
    (4,6,7),
    (0,3,6),
    (0,4,6),
    (1,2,5),
    (1,5,7),
)

def draw_cube():
    glBegin(GL_TRIANGLES)
    for edge in edges:
        for vertex in edge:
            glVertex3f(vertices[vertex][0],vertices[vertex][1],vertices[vertex][2])
    glEnd()

def draw_object():
    global colours
    for i, colour in enumerate(colours):
        glPushMatrix()
        glScalef(4 - i * 1, 4 - i * 1, 4 - i * 1)
        glColor3fv(colour)
        draw_cube()
        glPopMatrix()

direction = 0
speed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                glTranslatef(-1,0,0)
            if event.key == pygame.K_d:
                glTranslatef(1,0,0)
            if event.key == pygame.K_w:
                glTranslatef(0,1,0)
            if event.key == pygame.K_s:
                glTranslatef(0,-1,0)
            if event.key == pygame.K_q:
                glTranslatef(0,0,1)
            if event.key == pygame.K_e:
                glTranslatef(0,0,-1)
            if event.key == pygame.K_j:
                direction = 0
            if event.key == pygame.K_k:
                direction = 1
            if event.key == pygame.K_l:
                direction = 2
            if event.key == pygame.K_o:
                speed = speed + 1
            if event.key == pygame.K_p:
                speed = speed - 1
            if event.key == pygame.K_n:
                glScale(1.1,1.1,1.1)
            if event.key == pygame.K_m:
                glScale(0.9,0.9,0.9)
    if direction == 0:
        glRotatef(speed,1,0,0)
    elif direction == 1:
        glRotatef(speed,0,1,0)
    elif direction == 2:
        glRotatef(speed,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_object()
    pygame.display.flip()
    pygame.time.wait(15)
