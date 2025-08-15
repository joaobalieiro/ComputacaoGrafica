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
    # Inclinação da reta
    dx = x2 - x1
    dy = y2 - y1

    # Direções de incremento (sinal)
    sx = 1 if dx >= 0 else -1
    sy = 1 if dy >= 0 else -1

    # Caso linha vertical (x constante)
    if dx == 0:
        y = y1
        Write_pixel(x1, y, color)
        for _ in range(dy):
            y += sy
            Write_pixel(x1, y, color)
        return

    # Caso linha horizontal (y constante)
    if dy == 0:
        x = x1
        Write_pixel(x, y1, color)
        for _ in range(dx):
            x += sx
            Write_pixel(x, y1, color)
        return

    # Caso geral: decidir eixo de iteração
    if dx >= dy:
        # Iteração ao longo de X (|m| <= 1)
        d = 2 * dy - dx  # decisão inicial
        incE = 2 * dy  # escolher "E"
        incNE = 2 * (dy - dx)  # escolher "NE" (ou "SE" dependendo do sy)
        x, y = x1, y1
        Write_pixel(x, y, color)
        for i in range(dx):
            if d <= 0:
                # segue no eixo principal (E)
                d += incE
            else:
                # anda um em Y (NE/SE)
                y += sy
                d += incNE
            x += sx
            Write_pixel(x, y, color)
    else:
        # Iteração ao longo de Y (|m| > 1)
        d = 2 * dx - dy  # decisão inicial
        incE = 2 * dx  # escolher "E" no espaço transposto
        incNE = 2 * (dx - dy)  # escolher "NE/SE" no espaço transposto
        x, y = x1, y1
        Write_pixel(x, y, color)
        for i in range(dy):
            if d <= 0:
                # segue no eixo principal (E "transposto")
                d += incE
            else:
                # anda um em X
                x += sx
                d += incNE
            y += sy
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
    midPoint(-0, -0, 100, 100, (1.0, 0.0, 0.0))

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
