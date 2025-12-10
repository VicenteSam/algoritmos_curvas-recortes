import pygame
from math import comb

def parametrico(p, t):
    bx, by = 0, 0
    n = len(p)-1
    for i in range(n+1):
        bx += comb(n, i) * (1-t)**(n-i)*t**i * p[i][0]
        by += comb(n, i) * (1-t)**(n-i)*t**i * p[i][1]

    return (bx, by)

def desenha_curva(tela, pontos, passos=100):
    curva = [parametrico(pontos, k/passos) for k in range(passos + 1)]

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
    
