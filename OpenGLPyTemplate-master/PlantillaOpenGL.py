from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarFondo():
    glColor(0.2,0.7,0.7)
    glBegin(GL_QUADS)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,1,0)
    
  
    glEnd()


def dibujarpasto():
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.7,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()


def dibujaperilla():
    glColor3f(0,0,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.03 - -0.3 , sin(angulo) * 0.03 + -0.6, 0.0)
    glEnd()

def dibujarMarcoventana():
    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex3f(0.3,-0.3,0.0)
    glVertex3f(0.6,-0.3,0.0)
    glVertex3f(0.6,-0.1,0.0)
    glVertex3f(0.3,-0.1,0.0)
    
    glEnd()

def ventana1():
    glColor3f(0.1,1,1)
    glBegin(GL_QUADS)
    glVertex3f(0.31,-0.19,0.0)
    glVertex3f(0.44,-0.19,0.0)
    glVertex3f(0.44,-0.11,0.0)
    glVertex3f(0.31,-0.11,0.0)
    
    glEnd()

def ventana2():
    glColor3f(0.1,1,1)
    glBegin(GL_QUADS)
    glVertex3f(0.46,-0.19,0.0)
    glVertex3f(0.59,-0.19,0.0)
    glVertex3f(0.59,-0.11,0.0)
    glVertex3f(0.46,-0.11,0.0)
    
    glEnd()

def ventana3():
    glColor3f(0.1,1,1)
    glBegin(GL_QUADS)
    glVertex3f(0.46,-0.29,0.0)
    glVertex3f(0.59,-0.29,0.0)
    glVertex3f(0.59,-0.21,0.0)
    glVertex3f(0.46,-0.21,0.0)
    
    glEnd()

def ventana4():
    glColor3f(0.1,1,1)
    glBegin(GL_QUADS)
    glVertex3f(0.31,-0.29,0.0)
    glVertex3f(0.44,-0.29,0.0)
    glVertex3f(0.44,-0.21,0.0)
    glVertex3f(0.31,-0.21,0.0)
    
    glEnd()    

def rayosol1():
    glColor3f(0.9,0.4,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.23 - 0.6 , sin(angulo) * 0.23 + 0.6, 0.0)
    glEnd()

def dibujarCirculo():
    glColor3f(0.949,0.874,0.047)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6 , sin(angulo) * 0.2 + 0.6, 0.0)
    glEnd()


def dibujarCasaContorno():
    glColor3f(0.9,0.5,0.3)
    glBegin(GL_QUADS)
    glVertex3f(-0.1,-0.8,0.0)
    glVertex3f(0.7,-0.8,0.0)
    glVertex3f(0.7,0,0.0)
    glVertex3f(-0.1,0,0.0)
    glEnd()

def DibujarPuerta():
    glColor(0.9,0.9,0.9)
    glBegin(GL_QUADS)
    glVertex3f(0.1,-0.8,0.0)
    glVertex3f(0.4,-0.8,0.0)
    glVertex3f(0.4,-0.4,0.0)
    glVertex3f(0.1,-0.4,0.0)
    glEnd()

def DibujarTecho():
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.2,0,0)
    glVertex3f(0.3,0.4,0.0)
    glVertex3f(0.8,0,0)
    glEnd()

def DibujarArbol():
    glColor(0.4,0.2,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-0.8,-0.8,0.0)
    glVertex3f(-0.6,-0.8,0.0)
    glVertex3f(-0.6,-0.3,0.0)
    glVertex3f(-0.8,-0.3,0.0)
    glEnd()

def dibujarhojas1():
    glColor3f(0.1,0.3,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.3 - 0.7 , sin(angulo) * 0.2 + -0.2, 0.0)
    glEnd()

def dibujarhojas2():
    glColor3f(0.1,0.3,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.3 - 0.6 , sin(angulo) * 0.2 + -0.1, 0.0)
    glEnd()

def nube1():
    glColor3f(0.9,0.9,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 - 0.11 , sin(angulo) * 0.08 + 0.4, 0.0)
    glEnd()

def nube2():
    glColor3f(0.9,0.9,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 - 0.08 , sin(angulo) * 0.08 + 0.32, 0.0)
    glEnd()

def nube3():
    glColor3f(0.9,0.9,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 - -0.5 , sin(angulo) * 0.08 + 0.8, 0.0)
    glEnd()

def nube4():
    glColor3f(0.9,0.9,0.7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 - -0.58 , sin(angulo) * 0.08 + 0.72, 0.0)
    glEnd()



def dibujar():
    #rutinas de dibujo
    dibujarFondo()
    dibujarpasto()
    rayosol1()
    dibujarCirculo()
    dibujarCasaContorno()
    DibujarTecho()
    DibujarPuerta()
    DibujarArbol()
    dibujarhojas1()
    dibujarhojas2()
    dibujarMarcoventana()
    ventana1()
    ventana2()
    ventana3()
    ventana4()
    nube1()
    nube2()
    nube3()
    nube4()
    dibujaperilla()
    

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0,0,0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()