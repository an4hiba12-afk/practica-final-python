import pygame
import random

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la moneda")

reloj = pygame.time.Clock()

jugador = pygame.Rect(375, 275, 50, 50)

moneda = pygame.Rect(
    random.randint(0, ANCHO - 30),
    random.randint(0, ALTO - 30),
    30,
    30
)

puntos = 0

fuente = pygame.font.Font(None, 36)

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador.x -= 5

    if teclas[pygame.K_RIGHT]:
        jugador.x += 5

    if teclas[pygame.K_UP]:
        jugador.y -= 5

    if teclas[pygame.K_DOWN]:
        jugador.y += 5

    if jugador.left < 0:
        jugador.left = 0

    if jugador.right > ANCHO:
        jugador.right = ANCHO

    if jugador.top < 0:
        jugador.top = 0

    if jugador.bottom > ALTO:
        jugador.bottom = ALTO

    if jugador.colliderect(moneda):
        puntos += 1

        moneda.x = random.randint(0, ANCHO - 30)
        moneda.y = random.randint(0, ALTO - 30)

    pantalla.fill((30, 30, 50))

    pygame.draw.rect(pantalla, (50, 150, 255), jugador)

    pygame.draw.ellipse(pantalla, (255, 220, 50), moneda)

    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pantalla.blit(texto, (20, 20))

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()