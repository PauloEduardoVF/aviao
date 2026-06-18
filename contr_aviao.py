import pygame

class ContrAviao:
    def __init__(self, jogo):
        self.tela = jogo.tela
        self.tela_rect =jogo.tela.get_rect()
        self.imagem = pygame.image.load('imagens/Starfighter.bmp')
        self.retangulo = self.imagem.get_rect()
        self.retangulo.midbottom = self.tela_rect.midbottom

    def blime(self):
        self.tela.blit(self.imagem, self.retangulo)