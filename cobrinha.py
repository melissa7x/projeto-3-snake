import pygame
import random
import sys

pygame.init()
# --- CONSTANTES E CONFIGURAÇÕES ---
LARGURA, ALTURA = 600, 400
TAMANHO_BLOCO = 10
FPS = 10
FONTE_PLACAR = pygame.font.SysFont("Arial", 40)

ESTRELAS = []

for _ in range(80):
    x = random.randint(0, LARGURA)
    y = random.randint(0, ALTURA)
    ESTRELAS.append([x, y])

# Cores (Tuplas RGB)
PRETO = (0, 0, 0)
BRANCO = (255,255,255)
ROXO= (180,0,255)
ROXO_ESCURO = (90,0,140)
ROXO_NEON =(200,0,255)
VERDE = (0, 255, 0)
CIANO = (0,225,255)

def inicializar_jogo():
    """Configura o estado inicial do jogo."""
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Snake Refatorada")
    relogio = pygame.time.Clock()
    
    # Estado inicial da cobra e direção
    pos_x, pos_y = LARGURA // 2, ALTURA // 2
    cobra = [[pos_x, pos_y]]
    direcao = (0, 0) # (dx, dy)
    
    comida = gerar_comida(cobra)
    pontos = 0
    
    return tela, relogio, cobra, direcao, comida, pontos

def desenhar_fundo(tela):
    for x in range(0, LARGURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, (30, 30, 30), (x, 0), (x, ALTURA))

    for y in range(0, ALTURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, (30, 30, 30), (0, y), (LARGURA, y))

def desenhar_placar(tela,pontos):
    texto = FONTE_PLACAR.render(f"{pontos}", True, BRANCO)
    tela.blit(texto, (10,10))
    pygame.display.update()

def desenhar_fundo(tela):
    for estrela in ESTRELAS:
        pygame.draw.circle(tela, (40, 0, 60), estrela, 2)

def gerar_comida(cobra):
    """Gera uma posição aleatória para a comida que não esteja sobre a cobra."""
    while True:
        x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
        if [x, y] not in cobra:
            return [x, y]

def processar_eventos(direcao_atual):
    """Trata as entradas do teclado e fechamento da janela."""
    nova_direcao = direcao_atual
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            encerrar_jogo()
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao_atual != (0, TAMANHO_BLOCO):
                nova_direcao = (0, -TAMANHO_BLOCO)
            elif evento.key == pygame.K_DOWN and direcao_atual != (0, -TAMANHO_BLOCO):
                nova_direcao = (0, TAMANHO_BLOCO)
            elif evento.key == pygame.K_LEFT and direcao_atual != (TAMANHO_BLOCO, 0):
                nova_direcao = (-TAMANHO_BLOCO, 0)
            elif evento.key == pygame.K_RIGHT and direcao_atual != (-TAMANHO_BLOCO, 0):
                nova_direcao = (TAMANHO_BLOCO, 0)
                
    return nova_direcao

def atualizar_logica(cobra, direcao, comida, pontos):
    """Gerencia movimento, colisões e alimentação."""
    if direcao == (0, 0):
        return cobra, comida, False, pontos # Jogo parado no início

    # Calcula nova cabeça
    nova_cabeca = [cobra[0][0] + direcao[0], cobra[0][1] + direcao[1]]

    # Verificação de colisão com paredes ou corpo
    if (nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA or
        nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA or
        nova_cabeca in cobra):
        return cobra, comida, True,pontos # Fim de jogo

    cobra.insert(0, nova_cabeca)

    # Verificação de comida
    if nova_cabeca == comida:
        comida = gerar_comida(cobra)
        pontos += 1
    else:
        cobra.pop()

    return cobra, comida, False, pontos

def desenhar(tela, cobra, comida,pontos):
    """Renderiza todos os elementos na tela."""
    tela.fill(PRETO)
    desenhar_fundo(tela)
    
    desenhar_placar(tela, pontos)
    pygame.display.update()

    # Desenhar Comida
    pygame.draw.rect(tela, CIANO, (comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
    
    # Desenhar Cobra
    for segmento in cobra:
        pygame.draw.rect(tela, ROXO, (segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
    
    desenhar_placar(tela,pontos)
    
    pygame.display.update()

def encerrar_jogo():
    """Finaliza o Pygame e o sistema de forma limpa."""
    pygame.quit()
    sys.exit()

def main():
    """Loop principal do jogo."""
    tela, relogio, cobra, direcao, comida, pontos = inicializar_jogo()
    
    while True:
        direcao = processar_eventos(direcao)
        cobra,comida,game_over,pontos = atualizar_logica(cobra, direcao, comida,pontos)
        
        if game_over:
            print("Game Over!")
            encerrar_jogo()
            
        desenhar(tela, cobra, comida,pontos)
        

        relogio.tick(FPS)

if __name__ == "__main__":
    main()