import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Global texture IDs
cube_texture = None
diamond_texture = None

def add_texture():
    
    global cube_texture, diamond_texture
    
    # Load cube texture
    image1 = pygame.image.load('texture.png')
    data1 = pygame.image.tostring(image1, 'RGBA')
    cube_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, cube_texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image1.get_width(), image1.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    
    # Load diamond texture
    image2 = pygame.image.load('diamond_texture.png')  
    data2 = pygame.image.tostring(image2, 'RGBA')
    diamond_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, diamond_texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image2.get_width(), image2.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data2)
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

def draw_triangle():
    
    glBegin(GL_TRIANGLES)
    
    glTexCoord2f(0.5, 1)
    glVertex3f(0, 1, 0)
    
    glTexCoord2f(0, 0)
    glVertex3f(-0.7, 0, 0.7)
    
    glTexCoord2f(1, 0)
    glVertex3f(0.7, 0, 0.7)
    
    glEnd()

def draw_cube():
  
    global cube_texture
    glBindTexture(GL_TEXTURE_2D, cube_texture)
    
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

def draw_diamond():
   
    global diamond_texture
    glBindTexture(GL_TEXTURE_2D, diamond_texture)
    
    # Top pyramid (4 faces)
    # Front face
    glPushMatrix()
    draw_triangle()
    glPopMatrix()
    
    # Right face
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    draw_triangle()
    glPopMatrix()
    
    # Back face
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    draw_triangle()
    glPopMatrix()
    
    # Left face
    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    draw_triangle()
    glPopMatrix()
    
    # Bottom pyramid (4 faces) - flip upside down
    # Front face
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    draw_triangle()
    glPopMatrix()
    
    # Right face
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(90, 0, 1, 0)
    draw_triangle()
    glPopMatrix()
    
    # Back face
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(180, 0, 1, 0)
    draw_triangle()
    glPopMatrix()
    
    # Left face
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(-90, 0, 1, 0)
    draw_triangle()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("06 Performance Task 1 Ricafrente")
    
    glEnable(GL_DEPTH_TEST)
    add_texture()
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -8)
    
    rotation_x = 0
    rotation_y = 0
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw cube on the left
        glPushMatrix()
        glTranslatef(-1.5, 0, 0)
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        draw_cube()
        glPopMatrix()
        
        # Draw diamond on the right
        glPushMatrix()
        glTranslatef(1.5, 0, 0)
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        glScalef(1.5, 1.5, 1.5)  # Make diamond slightly bigger
        draw_diamond()
        glPopMatrix()
        
        pygame.display.flip()
        
        rotation_x += 0.5
        rotation_y += 0.5
        
        clock.tick(60)

if __name__ == "__main__":
    main()
