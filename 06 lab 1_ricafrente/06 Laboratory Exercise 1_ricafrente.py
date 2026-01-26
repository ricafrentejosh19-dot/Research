import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def add_texture():
    image = pygame.image.load('texture.png')
    data = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

def draw_square():
    glBegin(GL_TRIANGLES)
    
    # First triangle (lower-left, lower-right, upper-right)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 0)
    
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 0)
    
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 0)
    
    # Second triangle (lower-left, upper-right, upper-left)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 0)
    
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 0)
    
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 0)
    
    glEnd()

def draw_cube():
    # 1st pair - Front face
    glPushMatrix()
    glTranslatef(0, 0, 1)
    draw_square()
    glPopMatrix()
    
    # 2nd pair - Right face
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslatef(0, 0, 1)
    draw_square()
    glPopMatrix()
    
    # 3rd pair - Back face
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    glTranslatef(0, 0, 1)
    draw_square()
    glPopMatrix()
    
    # 4th pair - Left face
    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    glTranslatef(0, 0, 1)
    draw_square()
    glPopMatrix()
    
    # 5th pair - Top face
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslatef(0, 0, 1)
    draw_square()
    glPopMatrix()
    
    # 6th pair - Bottom face
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glTranslatef(0, 0, 1)
    draw_square()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("06 Lab 1")
    
    glEnable(GL_DEPTH_TEST)
    add_texture()
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    rotation_x = 0
    rotation_y = 0
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        draw_cube()
        glPopMatrix()
        
        pygame.display.flip()
        
        rotation_x += 0.5
        rotation_y += 0.5
        
        clock.tick(60)

if __name__ == "__main__":
    main()
