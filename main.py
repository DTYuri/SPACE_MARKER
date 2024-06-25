### Yuri Duarte Theisen     RA: 1125371         Vinicius Radaelli da Silva  RA: 1135940

import pygame
import os
from tkinter import simpledialog
pygame.init()

tamanho_tela = (800, 600)
tela = pygame.display.set_mode((tamanho_tela))
nomeJogo = pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("img/fundo.jpg")
icone = pygame.image.load("img/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
branco = (255,255,255)
cinza = (190, 190, 190)
fonte = pygame.font.SysFont("baskerville ", 20)
nomeEstrelas = {}


while True :
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.MOUSEBUTTONUP:
            posicao = pygame.mouse.get_pos()
            caixaPergunta = simpledialog.askstring("Space", "Nome da Estrela")
            if caixaPergunta is None:
                caixaPergunta = "Não encontrado" +str(posicao)
            nomeEstrelas[caixaPergunta]= posicao

    tela.fill(branco)
    tela.blit (fundo,(0,0))
    
    
    for nome, pos in nomeEstrelas.items():
        texto = fonte.render(nome + str(pos), True, cinza)
        tela.blit(texto, pos)


    pygame.display.update()
    relogio.tick(60)

