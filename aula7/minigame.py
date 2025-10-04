import pygame, sys, random
# pip install pygame

# Inicialização do jogo
pygame.init()
# Criando a tela do jogo (x,y)
screen = pygame.display.set_mode((400,300))

# posiçao inicial da bolinha
x = 200
y = 150
raio = 20

# posicao aleatoria da comida
food_x = random.randint(20, 280) # meu limite é 400
food_y = random.randint(20, 280) # meu limite e 300

while True:
    # veriifacr todos os eventos
    for event in pygame.event.get():
        # o jogador clicou no X da guia e saiu do jogo
        if event.type == pygame.QUIT:
            sys.exit()

    # pegar teclas do jogador
    keys = pygame.key.get_pressed()
    # andar para  aesquerda
    if keys[pygame.K_LEFT]:
        x -=0.2
    # andadr para a direita
    if keys[pygame.K_RIGHT]:
        x +=0.2

    if keys[pygame.K_UP]:
        y -= 0.2

    if keys[pygame.K_DOWN]:
        y +=0.2

    # se x for menor que zero, a bolinha volta mais o tamanho da tela
    if x < raio:
        x = raio
        # se x for maior que 400, a bolinha volta menos o tamnjho da tela
    if x > 400 - raio:
        x = 400 - raio
    if y < raio:
        y = raio
    if y > 300 - raio:
        y = 300 - raio

    # diferença da poisicao vertical e horizontal
    diferenca_x = x - food_x
    diferenca_y = y - food_y

    # Quadrado das diferenças, ², para nao termos numeros negativos
    quadrado_x = diferenca_x ** 2
    quadrado_y = diferenca_y ** 2

    soma_quadrados = quadrado_x + quadrado_y

    # Raiz quadrada da soma (distancia final entre os centros), 0.5
    distancia = soma_quadrados ** 0.5

    if distancia < raio + 10: # se encostar (o raio 10 é o tamanho da bolinha amarela)
        raio += 3 # aumenta a bolinha vermelha

        # reposiciona a comida
        food_x = random.randint(20, 380)
        food_y - random.randint(20, 280)

    # pintar o fundo do jogo, RGB (0, 0, 0)
    screen.fill((0, 0, 0))

    # desenhar um circulo vermelho, RGB (255, 0, 0)
    # Cor RGB, Posiçao X e Y, com raio 20
    pygame.draw.circle(screen, (255, 0, 0), (x, y), raio)

    #bolinha amarela ( comida )
    pygame.draw.circle(screen, (255, 255, 0), (food_x, food_y), 10)

    # para trocar o frame
    pygame.display.flip()