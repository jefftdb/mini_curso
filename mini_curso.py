import random
import time
import colorama
from colorama import Fore

colorama.init()


class Item():
    def __init__(self,ataque = 10,vida = 100) -> None:        
        self.ataque = ataque
        self.vida = vida

    def equipa(self,item):
        self.ataque+=item.ataque
        self.vida+= item.vida



class Heroi(Item):
    def __init__(self,nome, estaVivo = True) -> None:
        Item.__init__(self)
        self.nome = nome
        self.estaVivo = estaVivo

    def ataca(self,inimigo):
        print(Fore.BLUE +'%s atacou %s' % (self.nome,inimigo.nome))

        time.sleep(1) #da um tempo de 1 segundo para aparecer a proxima mensagem

        inimigo.dano(self.ataque) # inimigo recebe o dano.
        time.sleep(1)
        inimigo.tem_Vida() # Verifica se o inimigo sobrevivei após o ataque.

    def dano(self,dano):
        self.vida-= dano
        print(Fore.RED +'%s recebeu %i de dano' % (self.nome, dano))
    
    def tem_Vida(self):
        if self.vida <= 0:
            print(Fore.RED +'%s foi eliminado' % (self.nome))
            self.estaVivo = False




jogadores = []

while True:
    player = input(Fore.GREEN + 'Digite o nome do Herói ou 0 para sair: ')
    if player != '0':

        jogadores.append(Heroi(player))
    else:
        break
    




while(len(jogadores) >=2):
    atacante = random.choice(jogadores)
    inimigo = random.choice(jogadores)

    if atacante != inimigo:
        atacante.ataca(inimigo)
    else:
        while atacante == inimigo:
            inimigo = random.choice(jogadores)

    
    for jogador in jogadores: # remove da lista o Jogador Eliminado
        if not jogador.estaVivo:
            jogadores.remove(jogador)


for jogador in jogadores: #Exibe o jogador vencedor
    if jogador.estaVivo:
        print(Fore.GREEN + 'O %s venceu' % jogador.nome)
