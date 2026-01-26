import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cube():
    
    glBegin(GL_TRIANGLES)
    
    
     # kanan
    glColor3f(1, 0, 0)
     
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    glColor3f(1, 0, 0)
    
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)

    #taas
    glColor3f(1, 0.5, 0)
    
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    
    glColor3f(1, 0.5, 0)
    
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    #baba
    glColor3f(1, 1, 0)
    
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    
    glColor3f(1, 1, 0)
    
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)

    #kaliwa
    glColor3f(0, 1, 0)
    
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    
    glColor3f(0, 1, 0)
    
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)

    #likod
    glColor3f( 0, 0, 1)
    
    glVertex3f(-1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    
    glColor3f( 0, 0, 1)
    
    glVertex3f(-1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    #harap
    glColor3f( 0.5, 0, 1)
    
    glVertex3f(-1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    
    glColor3f( 0.5, 0, 1)
    
    glVertex3f(-1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    glEnd()

    

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("03 lab 1 Ricafrente")
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

while True:
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                glTranslatef(0, -1, 0)
            if event.key == pygame.K_UP:
                glTranslatef(0, 1, 0)
            if event.key == pygame.K_LEFT:
                glTranslatef(-1, 0, 0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(1, 0, 0)
            if event.key == pygame.K_s:
                glScalef(2, 2, 2)
            if event.key == pygame.K_d:
                glScalef(0.5, 0.5, 0.5)
            if event.key == pygame.K_r:
                glRotatef(60, 60, 60, 60)
            
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  
    draw_cube()
    

    pygame.display.flip()
    pygame.time.wait(15)
