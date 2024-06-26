
import pygame
import os
import tkinter as tk
from tkinter import simpledialog
pygame.init()

tamanho_tela = (900, 600)
tela = pygame.display.set_mode((tamanho_tela))
nomeJogo = pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("img/fundo.png")
# pygame.image.load("img/icone.png")
# pygame.display.set_icon()
relogio = pygame.time.Clock()
#pygame.mixer.music.load("img/somJogo.mp3")
#pygame.mixer.music.play (-1)
branco = (255,255,255)
cinza = (190, 190, 190)
verde = (173, 255, 47)
fonte = pygame.font.SysFont("baskerville ", 20)



def jogo ():
    os.system("cls")
    nomeEstrelas = {}

    while True :
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = evento.pos
                caixaPergunta = simpledialog.askstring("Space", "Nome da Estrela")
                if caixaPergunta is None or caixaPergunta.strip() == "":
                    caixaPergunta = f"Desconhecido {posicao}"
                nomeEstrelas[caixaPergunta]= posicao

        tela.fill(branco)
        tela.blit (fundo,(0,0))

        #Dados
        salvarTxt = fonte.render("Pressione 1 para salvar os pontos",True,cinza)    
        tela.blit(salvarTxt,(4,0))
        carregarTxt = fonte.render("Pressione 2 para carregar os pontos",True,cinza)
        tela.blit(carregarTxt,(4,15))
        excluirTxt = fonte.render("Pressione 3 para exluir os pontos",True,cinza)
        tela.blit(excluirTxt,(4,32))   
    
        for nome, pos in nomeEstrelas.items():
            pygame.draw.circle(tela, verde, pos, 3)
            font = pygame.font.Font(None, 20)
            texto = fonte.render(nome, True, cinza)
            tela.blit(texto, (pos[0] + 10, pos[1] - 10))



        pygame.display.update()
        relogio.tick(60)

jogo()