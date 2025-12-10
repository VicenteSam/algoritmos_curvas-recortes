import pygame

def casteljau(p, t):
    if len(p) == 1:
        return p[0]
    q = []
    for i in range(len(p)-1):
        q.append(((1-t)*p[i][0] + t*p[i+1][0], (1-t)*p[i][1] + t*p[i+1][1]))

    return casteljau(q, t)


def desenha_curva(tela, pontos, passos=100):
    curva = [casteljau(pontos, k/passos) for k in range(passos + 1)]

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

