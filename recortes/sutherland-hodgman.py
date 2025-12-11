import pygame

WIDTH, HEIGHT = 400, 400
PIXEL_SIZE = 1
JANELA_RECORTE = [(-100, -100), (100, -100), (100, 100), (-100, 100)]

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritmo de recorte Sutherland-Hodgman")

def calcular_reta_bresenham(x1, y1, x2, y2, cor=(0,0,0)):
    x1, y1, x2, y2 = int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2))

    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        
    swap_y = False
    if y2 < y1:
        y1, y2 = -y1, -y2
        swap_y = True
    
    swap_xy = False
    if abs(y2-y1) > abs(x2-x1):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        swap_xy = True
    
    dy = y2 - y1
    dx = x2 - x1
    y = y1
    p = 2 * dy - dx

    pontos = []
        
    for x in range(x1, x2+1):
        if swap_xy:
            draw_x = y
            draw_y = x
        else:
            draw_x = x
            draw_y = y
            
        if swap_y:
            draw_y = -draw_y
            
        draw_pixel(draw_x, draw_y, cor)

        if p >= 0:
            y += 1
            p = p + 2*(dy-dx)
        else:
            p = p + 2*dy

    for px, py in pontos:
        draw_pixel(px, py, cor)

def desenhar_poligono(pontos, cor=(0, 0, 0), delay=0):
    if len(pontos) < 2:
        return
    
    for i in range(len(pontos)):
        x1, y1 = pontos[i]
        x2, y2 = pontos[(i + 1) % len(pontos)]
        calcular_reta_bresenham(x1, y1, x2, y2, cor)
        
        if delay > 0:
            pygame.display.update()
            pygame.time.delay(delay)

def encontrar_intersecao(p1, p2, j1, j2):
    x1, y1 = p1
    x2, y2 = p2
    ax, ay = j1
    bx, by = j2

    if x1 == x2:
        if ax == bx:
            return None
        else:
            return (x1, ay)
    

    m = (y2 - y1) / (x2 - x1)
    
    if ax == bx:
        return (ax, m * (ax - x1) + y1)
    else:
        if m == 0:
            return (x1, ay)
        else:
            return (x1 + (1/m) * (ay - y1), ay)

def sutherland_recorte(poligono, janela):
    entrada = poligono[:]
    
    for i in range(len(janela)):
        j1 = janela[i]
        j2 = janela[(i+1) % len(janela)]
        saida = []
        for k in range(len(entrada)):
            p1 = entrada[k]
            p2 = entrada[(k+1) % len(entrada)]

            # P = (x-x1)*(y2-y1)-(y-y1)*(x2-x1)
            p1_pos = (p1[0]-j1[0])*(j2[1]-j1[1])-(p1[1]-j1[1])*(j2[0]-j1[0])
            p2_pos = (p2[0]-j1[0])*(j2[1]-j1[1])-(p2[1]-j1[1])*(j2[0]-j1[0])

            if p1_pos <= 0 and p2_pos <= 0: # CASO 1: P1 (dentro) -> P2 (dentro)
                saida.append(p2)
            elif p1_pos > 0 and p2_pos <= 0: # CASO 2: P1 (fora) -> P2 (dentro)
                p_int = encontrar_intersecao(p1, p2, j1, j2)
                if p_int:
                    saida.append(p_int)
                saida.append(p2)
            elif p1_pos <= 0 and p2_pos > 0: # CASO 3: P1 (dentro) -> P2 (fora)
                p_int = encontrar_intersecao(p1, p2, j1, j2)
                if p_int:
                    saida.append(p_int)
            else: # CASO 4: P1 (fora) -> P2 (fora)
                pass

        entrada = saida

    return entrada

def draw_pixel(x, y, cor=(0,0,0)):
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    
    pixel_x = center_x + int(round(x * PIXEL_SIZE))
    pixel_y = center_y - int(round(y * PIXEL_SIZE))
    
    if 0 <= pixel_x < WIDTH and 0 <= pixel_y < HEIGHT:
        tela.set_at((pixel_x, pixel_y), cor)

def limpar_tela():
    tela.fill((255, 255, 255))
    
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    pygame.draw.line(tela, (220, 220, 220), (center_x, 0), (center_x, HEIGHT), 1)
    pygame.draw.line(tela, (220, 220, 220), (0, center_y), (WIDTH, center_y), 1)

if __name__ == "__main__":
    poligono = [(-80, 50),(-80, 150),(80,150),(80, 50),(25, 50),(25, 110),(-25,110),(-25, 50)]
    #poligono = [(-50, -50), (-50, 150), (150, -50)]
    #poligono = [(-50, 0), (50, 0), (50, -40), (90, -40), (90, -120), (50, -120),(50, -160), (-50,-160), (-50, -120), (-90, -120), (-90, -40), (-50,-40)]
    #poligono = [(-30,-50),(20,40),(-70,120),(-160, 60),(-130, -50)]
    
    tela.fill((255, 255, 255))
    pygame.display.update()
    pygame.time.delay(500)
    
    desenhar_poligono(JANELA_RECORTE, (0, 0, 255))
    pygame.display.update()
    pygame.time.delay(1000)
    
    for i in range(len(poligono)):
        x1, y1 = poligono[i]
        x2, y2 = poligono[(i + 1) % len(poligono)]
        calcular_reta_bresenham(x1, y1, x2, y2, (255, 0, 0))
        pygame.display.update()
        pygame.time.delay(300)
    pygame.time.delay(500)

    resultado = sutherland_recorte(poligono, JANELA_RECORTE)
    
    if resultado:
        for i in range(len(resultado)):
            x1, y1 = resultado[i]
            x2, y2 = resultado[(i + 1) % len(resultado)]
            
            for offset in range(-1, 2):
                calcular_reta_bresenham(x1 + offset*0.4, y1, x2 + offset*0.4, y2, (0, 255, 0))
                calcular_reta_bresenham(x1, y1 + offset*0.4, x2, y2 + offset*0.4, (0, 255, 0))
            pygame.display.update()
 
    
    pygame.display.update()
    
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
    
    pygame.quit()
