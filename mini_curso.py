from random import randint
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


player1 = Heroi('Jogador 1')
player2 = Heroi('Jogador 2')
player3 = Heroi('Jogador 3')

jogadores = player1,player2,player3


while((player1.estaVivo and player2.estaVivo) or (player1.estaVivo and player3.estaVivo) or (player2.estaVivo and player3.estaVivo)):
    atacante = randint(1,3)

    if atacante == 1 and player1.estaVivo:
        vitima = randint(0,1)
        if vitima == 0 and player2.estaVivo:          
            player1.ataca(player3)
        else:
            player1.ataca(player2)

    elif atacante == 2 and player2.estaVivo :
        vitima = randint(0,1)
        if vitima == 0 and player1.estaVivo:          
            player2.ataca(player1)
        else:
            player2.ataca(player3)

    elif atacante == 3 and player3.estaVivo:
        vitima = randint(0,1)
        if vitima == 0 and player1.estaVivo:          
            player3.ataca(player1)
        else:
            player3.ataca(player2)



for jogador in jogadores: #Exibe o jogador vencedor
    if jogador.estaVivo:
        print(Fore.GREEN + 'O %s venceu' % jogador.nome)
