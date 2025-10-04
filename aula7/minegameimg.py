import pygame, sys, random
# pip install pygame

# Inicialização do jogo
pygame.init()
# Criando a tela do jogo (x,y)
screen = pygame.display.set_mode((400,300))

# carregar img
player_img = pygame.image.load("veiga.png")

food_img = pygame.image.load("lixo.png")
food_img = pygame.transform.scale(food_img, (50, 50))



# posiçao inicial da bolinha
x = 200
y = 150
tamanho = 40
velocidade = 5

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
    if x < 0:
        x = 0
        # se x for maior que 400, a bolinha volta menos o tamnjho da tela
    if x > 400 - tamanho:
        x = 400 - tamanho
    if y < 0:
        y = 0
    if y > 300 - tamanho:
        y = 300 - tamanho

    centro_player_x = x + tamanho / 2
    centro_player_y = y + tamanho / 2

    centro_food_x = food_x + 10
    centro_food_y = food_y + 10
   
    diferenca_x = centro_player_x - centro_food_x
    diferenca_y = centro_player_y - centro_food_y

    quadrado_x = diferenca_x ** 2
    quadrado_y = diferenca_y ** 2

    # soma dos quadrados
    soma_quadrados = quadrado_x + quadrado_y
    #raiz dos quadrados
    distancia = soma_quadrados ** 0.5

    if distancia < (tamanho / 2 + 10): # se encostar (o raio 10 é o tamanho da bolinha amarela)
        tamanho += 5 # aumenta a bolinha vermelha

        # reposiciona a comida
        food_x = random.randint(20, 380)
        food_y - random.randint(20, 280)

    # redimendionar a img do jogador
    player_scaled = pygame.transform.scale(player_img, (tamanho, tamanho))

    # pintar o fundo do jogo, RGB (0, 0, 0)
    screen.fill((0, 0, 0))

    screen.blit(food_img, (food_x, food_y))
    screen.blit(player_scaled, (x, y))

    # para trocar o frame
    pygame.display.flip()