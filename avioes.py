import pygame
import sys
from config import Config
from contr_aviao import ContrAviao

class Avioes:
    def __init__(self):
        pygame.init()
        self.frame = pygame.time.Clock() 
        self.config = Config()
        self.tela = pygame.display.set_mode((self.config.tela_largura, self.config.tela_altura))
        self.cor_fundo = (self.config.cor)
        pygame.display.set_caption("Aviões!")
        self.contr_aviao = ContrAviao(self)


    def rodar_jogo(self):
        while True:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.frame.tick(60)
            self.tela.fill(self.cor_fundo)
            self.contr_aviao.blime()

if __name__ == "__main__":
    jogo = Avioes()
    jogo.rodar_jogo()