from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFNC ():
    glClearColor ( 1.0,1.0,1.0,1.0 )
    
    glPointSize (10.0)
    gluOrtho2D (0, 25, 0,25)

def BMOcode(): 
    glClear (GL_COLOR_BUFFER_BIT)
    glPointSize (12)
#code to draw BMO using points
# black
    glBegin (GL_POINTS)
    glColor3f (0.0, 0.0, 0.0)

    glVertex2f (7.0,5.0)
    glVertex2f (8.0,5.0)
    glVertex2f (9.0,5.0)
    glVertex2f (10.0,5.0)
    glVertex2f (11.0,5.0)
    glVertex2f (12.0,5.0)
    glVertex2f (13.0,5.0)
    glVertex2f (14.0,5.0)
    glVertex2f (15.0,5.0)
    glVertex2f (16.0,5.0)
    glVertex2f (17.0,5.0)

    glVertex2f (7.0,20.0)
    glVertex2f (8.0,20.0)
    glVertex2f (9.0,20.0)
    glVertex2f (10.0,20.0)
    glVertex2f (11.0,20.0)
    glVertex2f (12.0,20.0)
    glVertex2f (13.0,20.0)
    glVertex2f (14.0,20.0)
    glVertex2f (15.0,20.0)
    glVertex2f (16.0,20.0)
    glVertex2f (17.0,20.0)

    glVertex2f(6.0, 6.0)
    glVertex2f(6.0, 7.0)
    glVertex2f(6.0, 8.0)
    glVertex2f(6.0, 9.0)
    glVertex2f(6.0, 10.0)
    glVertex2f(6.0, 11.0)
    glVertex2f(6.0, 12.0)
    glVertex2f(6.0, 13.0)
    glVertex2f(6.0, 14.0)
    glVertex2f(6.0, 15.0)
    glVertex2f(6.0, 16.0)
    glVertex2f(6.0, 17.0)
    glVertex2f(6.0, 18.0)
    glVertex2f(6.0, 19.0)

    glVertex2f(18.0, 6.0)
    glVertex2f(18.0, 7.0)
    glVertex2f(18.0, 8.0)
    glVertex2f(18.0, 9.0)
    glVertex2f(18.0, 10.0)
    glVertex2f(18.0, 11.0)
    glVertex2f(18.0, 12.0)
    glVertex2f(18.0, 13.0)
    glVertex2f(18.0, 14.0)
    glVertex2f(18.0, 15.0)
    glVertex2f(18.0, 16.0)
    glVertex2f(18.0, 17.0)
    glVertex2f(18.0, 18.0)
    glVertex2f(18.0, 19.0)
    glEnd ()


#face 
    glBegin (GL_POINTS)
    glColor3f (0.0, 0.0, 0.0)
    # eyes
    glVertex2f(9.0, 16.0)
    glVertex2f(15.0, 16.0)
    #mouth
    glVertex2f(11.0, 15.0)
    glVertex2f(12.0, 15.0)
    glVertex2f(13.0, 15.0)
    glEnd ()

# body
    glBegin (GL_POINTS)
    glColor3f (0.16078, 0.63922, 0.63922 )
    glVertex2f (7.0,19.0)
    glVertex2f (8.0,19.0)
    glVertex2f (9.0,19.0)
    glVertex2f (10.0,19.0)
    glVertex2f (11.0,19.0)
    glVertex2f (12.0,19.0)
    glVertex2f (13.0,19.0)
    glVertex2f (14.0,19.0)
    glVertex2f (15.0,19.0)
    glVertex2f (16.0,19.0)
    glVertex2f (17.0,19.0)

    glVertex2f(17.0, 6.0)
    glVertex2f(17.0, 7.0)
    glVertex2f(17.0, 8.0)
    glVertex2f(17.0, 9.0)
    glVertex2f(17.0, 10.0)
    glVertex2f(17.0, 11.0)
    glVertex2f(17.0, 12.0)
    glVertex2f(17.0, 13.0)
    glVertex2f(17.0, 14.0)
    glVertex2f(17.0, 15.0)
    glVertex2f(17.0, 16.0)
    glVertex2f(17.0, 17.0)
    glVertex2f(17.0, 18.0)
   
    glVertex2f(7.0, 6.0)
    glVertex2f(7.0, 7.0)
    glVertex2f(7.0, 8.0)
    glVertex2f(7.0, 9.0)
    glVertex2f(7.0, 10.0)
    glVertex2f(7.0, 11.0)
    glVertex2f(7.0, 12.0)
    glVertex2f(7.0, 13.0)
    glVertex2f(7.0, 14.0)
    glVertex2f(7.0, 15.0)
    glVertex2f(7.0, 16.0)
    glVertex2f(7.0, 17.0)
    glVertex2f(7.0, 18.0)

    glVertex2f (8.0,12.0)
    glVertex2f (9.0,12.0)
    glVertex2f (10.0,12.0)
    glVertex2f (11.0,12.0)
    glVertex2f (12.0,12.0)
    glVertex2f (13.0,12.0)
    glVertex2f (14.0,12.0)
    glVertex2f (15.0,12.0)
    glVertex2f (16.0,12.0)

    glVertex2f (8.0,10.0)
    glVertex2f (9.0,10.0)
    glVertex2f (10.0,10.0)
    glVertex2f (11.0,10.0)
    glVertex2f (12.0,10.0)
    glVertex2f (13.0,10.0)
    glVertex2f (14.0,10.0)
    glVertex2f (15.0,10.0)
    glVertex2f (16.0,10.0)
   
    glVertex2f (8.0,6.0)
    glVertex2f (9.0,6.0)
    glVertex2f (10.0,6.0)
    glVertex2f (11.0,6.0)
    glVertex2f (12.0,6.0)
    glVertex2f (13.0,6.0)
    glVertex2f (14.0,6.0)
    glVertex2f (15.0,6.0)
    glVertex2f (16.0,6.0)

    glVertex2f (16.0,11.0)
    glVertex2f (16.0,9.0)
    glVertex2f (16.0,8.0)
    glVertex2f (16.0,7.0)

    glVertex2f (15.0,9.0)
    glVertex2f (15.0,7.0)

    glVertex2f(13.0,7.0)
    glVertex2f(12.0,7.0)
    glVertex2f(11.0,7.0)
    glVertex2f(10.0,7.0)
    glVertex2f(8.0,7.0)

    glVertex2f(14.0,8.0)
    glVertex2f(12.0,8.0)
    glVertex2f(11.0,8.0)

    glVertex2f(14.0,9.0)
    glVertex2f(13.0,9.0)
    glVertex2f(12.0,9.0)
    glVertex2f(11.0,9.0)
    glVertex2f(10.0,9.0)
    glVertex2f(8.0,9.0)

    glVertex2f(14.0,11.0)
    glVertex2f(13.0,11.0)

    glEnd ()


    glBegin (GL_POINTS)
    glColor3f (0.0, 0.0, 1.0 )
    glVertex2f(15.0,11.0)
    glEnd ()

    glBegin (GL_POINTS)
    glColor3f (0.0, 0.2, 0.0 )
    glVertex2f(12.0,11.0)
    glVertex2f(11.0,11.0)
    glVertex2f(10.0,11.0)
    glVertex2f(9.0,11.0)
    glVertex2f(8.0,11.0)
    
    glEnd ()


    glBegin (GL_POINTS)
    glColor3f (0.4, 1.0, 0.4 )
    glVertex2f(15.0,8.0)
    glEnd ()


    glBegin (GL_POINTS)
    glColor3f (1.0, 0.0, 0.4 )
    glVertex2f(14.0,7.0)
    glEnd ()


    glBegin (GL_POINTS)
    glColor3f (0.4, 1.0, 1.0 )
    glVertex2f(13.0,8.0)
    glEnd ()


    glBegin (GL_POINTS)
    glColor3f (1.0, 0.85, 0.30 )
    glVertex2f(10.0,8.0)
    glVertex2f(9.0,8.0)
    glVertex2f(8.0,8.0)
    glVertex2f(9.0,7.0)
    glVertex2f(9.0,9.0)

    glEnd ()

   
    glBegin (GL_POINTS)
    glColor3f (0.6, 0.9, 0.9 )
    
    glVertex2f (8.0,18.0)
    glVertex2f (9.0,18.0)
    glVertex2f (10.0,18.0)
    glVertex2f (11.0,18.0)
    glVertex2f (12.0,18.0)
    glVertex2f (13.0,18.0)
    glVertex2f (14.0,18.0)
    glVertex2f (15.0,18.0)
    glVertex2f (16.0,18.0)

    glVertex2f (8.0,17.0)
    glVertex2f (9.0,17.0)
    glVertex2f (10.0,17.0)
    glVertex2f (11.0,17.0)
    glVertex2f (12.0,17.0)
    glVertex2f (13.0,17.0)
    glVertex2f (14.0,17.0)
    glVertex2f (15.0,17.0)
    glVertex2f (16.0,17.0)

    glVertex2f (8.0,13.0)
    glVertex2f (9.0,13.0)
    glVertex2f (10.0,13.0)
    glVertex2f (11.0,13.0)
    glVertex2f (12.0,13.0)
    glVertex2f (13.0,13.0)
    glVertex2f (14.0,13.0)
    glVertex2f (15.0,13.0)
    glVertex2f (16.0,13.0)
    
    glVertex2f (8.0,14.0)
    glVertex2f (9.0,14.0)
    glVertex2f (10.0,14.0)
    glVertex2f (11.0,14.0)
    glVertex2f (12.0,14.0)
    glVertex2f (13.0,14.0)
    glVertex2f (14.0,14.0)
    glVertex2f (15.0,14.0)
    glVertex2f (16.0,14.0)


    glVertex2f (14.0,15.0)
    glVertex2f (15.0,15.0)
    glVertex2f (16.0,15.0)

    glVertex2f (8.0,15.0)
    glVertex2f (9.0,15.0)
    glVertex2f (10.0,15.0)

    glVertex2f (8.0,16.0)
    glVertex2f (16.0,16.0)


    glVertex2f (10.0,16.0)
    glVertex2f (11.0,16.0)
    glVertex2f (12.0,16.0)
    glVertex2f (13.0,16.0)
    glVertex2f (14.0,16.0)
    glEnd ()
    glFlush()
   

def main() :
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(100,100) 
    glutCreateWindow("BMO")
    drawFNC()
    glutDisplayFunc(BMOcode)
    glutMainLoop()

if __name__ == "__main__":
        main()

