import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("05 Performance Task 1 Ricafrente")

glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -15)

def draw_cube():
    vertices = [
        [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],  # back
        [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]       # Front
    ]
    
    faces = [
        [0, 1, 2, 3],  # Back
        [4, 5, 6, 7],  # Front
        [0, 1, 5, 4],  # Right
        [2, 3, 7, 6],  # Left
        [0, 3, 7, 4],  # Top
        [1, 2, 6, 5]   # Bottom
    ]
    
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_object():
    cube_size = 1.0
    spacing = 2.0  
    
    # Cube 1 -  mink
    glPushMatrix()
    glTranslatef(-2 * spacing, 0, 0)
    glColor3f(1.0, 0.7, 0.7)
    glScalef(cube_size, cube_size, cube_size)
    draw_cube()
    glPopMatrix()
    
    # Cube 2 - Red
    glPushMatrix()
    glTranslatef(-spacing, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    glScalef(cube_size, cube_size, cube_size)
    draw_cube()
    glPopMatrix()
    
    # Cube 3 - Blue 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor3f(0.0, 0.0, 1.0)
    glScalef(cube_size, cube_size, cube_size)
    draw_cube()
    glPopMatrix()
    
    # Cube 4 - Orange
    glPushMatrix()
    glTranslatef(spacing, 0, 0)
    glColor3f(1.0, 0.5, 0.0)
    glScalef(cube_size, cube_size, cube_size)
    draw_cube()
    glPopMatrix()
    
    # Cube 5 - Green
    glPushMatrix()
    glTranslatef(2 * spacing, 0, 0)
    glColor3f(0.0, 1.0, 0.0)
    glScalef(cube_size, cube_size, cube_size)
    draw_cube()
    glPopMatrix()


position_x = 0
rotation_front = 0
rotation_position = 0
rotating_front = False
rotating_back = False
rotating_left = False
rotating_right = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                position_x += 1
            elif event.key == pygame.K_LEFT:
                position_x -= 1
            elif event.key == pygame.K_f:
                rotating_front = True
                rotating_back = False
            elif event.key == pygame.K_b:
                rotating_back = True
                rotating_front = False
            elif event.key == pygame.K_l:
                rotating_left = True
                rotating_right = False
            elif event.key == pygame.K_r:
                rotating_right = True
                rotating_left = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                rotating_front = False
            elif event.key == pygame.K_b:
                rotating_back = False
            elif event.key == pygame.K_l:
                rotating_left = False
            elif event.key == pygame.K_r:
                rotating_right = False
    

    if rotating_front:
        rotation_front += 2
    if rotating_back:
        rotation_front -= 2
    if rotating_left:
        rotation_position += 2
    if rotating_right:
        rotation_position -= 2
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    
    # Apply left/right position movement
    glTranslatef(position_x, 0, 0)
    
    # Move to left end cube (pink cube) as pivot point
    glTranslatef(-4, 0, 0)
    
    # Apply L/R rotation around left end cube (pink cube)
    glRotatef(rotation_position, 0, 0, 1)
    
    # Apply F/B front rotation (around X-axis for horizontal rotation)
    glRotatef(rotation_front, 1, 0, 0)
    
    # Move back
    glTranslatef(4, 0, 0)
    
    draw_object()
    glPopMatrix()
    
    pygame.display.flip()
    pygame.time.wait(15)
