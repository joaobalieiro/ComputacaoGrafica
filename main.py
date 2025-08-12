from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 500, 500

# Função para desenhar pixel
def Write_pixel(x, y, color=(1.0, 0.0, 0.0)):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

# Algoritmo do ponto médio
def midPoint(x1, y1, x2, y2, color=(1.0, 0.0, 0.0)):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx  # valor inicial de d
    incE = 2 * dy  # incremento para E
    incNE = 2 * (dy - dx)  # incremento para NE

    x = x1
    y = y1
    Write_pixel(x, y, color)

    while x < x2:
        if d <= 0:
            # Escolhe E
            d += incE
            x += 1
        else:
            # Escolhe NE
            d += incNE
            x += 1
            y += 1
        Write_pixel(x, y, color)

# Desenha eixos X e Y com marcações
def draw_axes():
    glColor3f(0.0, 0.0, 0.0)  # preto
    glBegin(GL_LINES)
    # Eixo X
    glVertex2i(-width//2, 0)
    glVertex2i(width//2, 0)
    # Eixo Y
    glVertex2i(0, -height//2)
    glVertex2i(0, height//2)
    glEnd()

    # Marcações nos eixos
    glBegin(GL_LINES)
    for x in range(-width//2, width//2 + 1, 50):
        glVertex2i(x, -5)
        glVertex2i(x, 5)
    for y in range(-height//2, height//2 + 1, 50):
        glVertex2i(-5, y)
        glVertex2i(5, y)
    glEnd()

# Função de display
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_axes()

    # Exemplo: linha de (-100, -50) até (150, 120)
    midPoint(-100, -50, 100, 0, (1.0, 0.0, 0.0))

    glFlush()

# Inicializa OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # fundo branco
    glColor3f(1.0, 0.0, 0.0)          # cor inicial
    gluOrtho2D(-width//2, width//2, -height//2, height//2)  # origem no centro

# Programa principal
if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"MidPoint Line com Origem no Centro - OpenGL")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
