import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices_cube1 = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (1, 1, -1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, 1, -1)
)

faces_cube1 = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)

vertices_cube2 = (
    (2, -2, -2),
    (2, -2, 2),
    (-2, -2, 2),
    (-2, -2, -2),
    (2, 2, -2),
    (2, 2, 2),
    (-2, 2, 2),
    (-2, 2, -2)
)

faces_cube2 = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)

tex_coords_cube = [
    (1, 0),
    (1, 1),
    (0, 1),
    (0, 0)
]

def load_texture_cube():
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    texture_surface = pygame.image.load("tex1.jpg")
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_width(), texture_surface.get_height()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    return texture

def load_texture_cube2():
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    texture_surface = pygame.image.load("creeper1.png")
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_width(), texture_surface.get_height()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    return texture
    

def draw_cube(vertices, faces, tex_coords):
    texture = load_texture_cube2()
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        for j, vertex in enumerate(face):
            glTexCoord2fv(tex_coords[j])
            glVertex3fv(vertices[vertex])
    glEnd()

    
def draw_cube2(vertices, faces, tex_coords):
    texture = load_texture_cube()
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        for j, vertex in enumerate(face):
            glTexCoord2fv(tex_coords[j])
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("06 Performance Task 1 - Juan Rafael F. Rivera")
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -15)

    clock = pygame.time.Clock()

    cube2_xpos = -10.0
    cube1_ypos = -2.0

    cube1_scale = 0.3

    angle_cube2accel = 0.0

    counter1 = 0

    angle_cube1 = 0.0
    angle_cube2 = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0,cube1_ypos,0)
        glScalef(cube1_scale,cube1_scale,cube1_scale)
        glRotatef(angle_cube1, 0, -1, 0)  # Rotate the first cube
        draw_cube(vertices_cube1, faces_cube1, tex_coords_cube)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(cube2_xpos,3,0)
        glRotatef(angle_cube2, 0, 3, 0)  # Rotate the second cube
        glScalef(1,0.3,1)
        draw_cube2(vertices_cube2, faces_cube2, tex_coords_cube)
        glPopMatrix()

        angle_cube1 += 1.0

        if cube2_xpos <= 0:
            cube2_xpos += 0.1;
        else:
            if angle_cube2accel < 1:
                angle_cube2accel += 0.01
            else:
                if counter1 < 100:
                    counter1 += 1
                elif counter1 >= 100:
                    if cube1_ypos < 3:
                        cube1_ypos += 0.02
                    else:
                        cube1_scale = 0
                        cube2_xpos += 0.05;
                    
            angle_cube2 += angle_cube2accel
            

        angle_cube1 %= 360.0
        angle_cube2 %= 360.0

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
