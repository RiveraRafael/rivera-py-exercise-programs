# RIVERA A702
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def add_texture(texture):
    image = pygame.image.load(texture)
    data = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)
    return texID

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("06 LaboratoryExercise 1 - Juan Rafael F. Rivera")
glEnable(GL_DEPTH_TEST)
tex = (
    add_texture('creeper1.png'),
    add_texture('creeper3.png'),
    add_texture('creeper5.png'),
    add_texture('creeper4.png'),
    add_texture('creeper2.png'),
    add_texture('creeper6.png')
)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslate(0,0,-20)
glScale(3,3,3)

vertices = (
    (1,1,1),
    (-1,1,1),
    (1,-1,1),
    (-1,-1,1)
)

edges = (
    (0,1,2),
    (1,2,3)
)

rotation = (
    (0,0,0,0),
    (90,0,1,0),
    (-90,1,0,0),
    (180,0,1,0),
    (-90,0,1,0),
    (90,1,0,0)
)

texedges = (
    (0,0),
    (1,0),
    (0,1),
    (1,1)
)

def draw_square():
    glBegin(GL_TRIANGLES)
    for i, edge in enumerate(edges):
        for vertex in edge:
            glTexCoord2f(texedges[vertex][0], texedges[vertex][1])
            glVertex3f(vertices[vertex][0],vertices[vertex][1],vertices[vertex][2])
    glEnd()

def draw_object():
    global colours
    v = 0
    for i in rotation:
        glPushMatrix()
        glRotatef(i[0],i[1],i[2],i[3])
        glBindTexture(GL_TEXTURE_2D, tex[v])
        draw_square()
        glPopMatrix()
        v = v + 1

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
