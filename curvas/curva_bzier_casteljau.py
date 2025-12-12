import pygame
import math

def ponto_medio(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def casteljau(p, tolerancia, curva):
    p0, p1, p2, p3 = p

    distancia = math.dist(p0, p3)
    if distancia < tolerancia:
        curva.append(p3)
        return

    p01 = ponto_medio(p0, p1)
    p12 = ponto_medio(p1, p2)
    p23 = ponto_medio(p2, p3) 

    p012 = ponto_medio(p01, p12)
    p123 = ponto_medio(p12, p23)

    p0123 = ponto_medio(p012, p123)

    casteljau([p0, p01, p012, p0123], tolerancia, curva)
    casteljau([p0123, p123, p23, p3], tolerancia, curva)

def gerar_curva(p, tolerancia=2.0):
    curva = [p[0]]
    casteljau(p, tolerancia, curva)
    return curva

def desenha_curva(tela, pontos):
    curva = gerar_curva(pontos, tolerancia=2)

    pygame.draw.lines(tela, (200, 0, 0), False, pontos, 1)
    for pt in pontos:
        pygame.draw.circle(tela, (255, 0, 0), pt, 5)

    pygame.draw.lines(tela, (0, 0, 0), False, curva, 2)



if __name__ == "__main__":
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    p = [(100, 400), (200, 100), (400, 100), (500, 400)]
    #p = [(100, 300), (250, 50), (350, 550), (500, 300)]
    #p = [(50, 300), (200, 250), (350, 350), (500, 300)]
    #p = [(50, 300), (200, 100), (350, 500), (550, 300)]
    #p = [(100, 200), (200, 210), (300, 190), (400, 200)]
    #p = [(50, 300), (150, 50), (300, 500), (450, 100), (600, 300)]


    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill((255, 255, 255))
        desenha_curva(tela, p)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

