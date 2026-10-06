import pygame

pygame.init()
t = pygame.display.set_mode((500, 400))
c = pygame.time.Clock()
px, bx, by, dx, dy, pts = 200, 250, 150, 4, -4, 0

while True:
    if pygame.event.peek(pygame.QUIT): break
    
    k = pygame.key.get_pressed()
    px += (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * 6
    px = max(0, min(400, px))  # Limita raquete na tela
    
    bx += dx; by += dy
    if bx <= 0 or bx >= 485: dx *= -1
    if by <= 0: dy *= -1
    
    r_bola = pygame.Rect(bx, by, 15, 15)
    r_raquete = pygame.Rect(px, 370, 100, 10)
    
    if r_bola.colliderect(r_raquete) and dy > 0:
        dy *= -1
        pts += 1
        
    if by > 400:  # Game over / reseta
        bx, by, dy, pts = 250, 150, -4, 0

    t.fill((0, 0, 0))
    pygame.draw.rect(t, (255, 255, 255), r_raquete)
    pygame.draw.ellipse(t, (255, 50, 50), r_bola)
    pygame.display.flip()
    c.tick(60)

pygame.quit()