# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
from lista import lista_palavras
import os
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

#função clear
clear = lambda: os.system('cls')

# Classe
class Hangman:

	# Método Construtor
     def __init__(self):
          palavra = random.choice(lista_palavras)
          palavra = list(palavra)
          self.palavra = palavra
          self.tam = 6
          self.letras = []
          for l in range(len(palavra)):
               self.letras += '_' 
          print(board[0])
          print('Bem vindo ao jogo da forca!')
          print(f'voce tem {self.tam} tentativas.')
          print(self.letras)

	# Método para adivinhar a letra
     def adivinha_letra(self):
          n = 0
          while self.tam != 0:
               if '_' not in self.letras:
                    print('Fim de jogo!')
                    break
               letra = input('\ndigite uma letra: ').lower()
               if letra in self.palavra:
                    for p in range(len(self.palavra)):
                         if letra == self.palavra[p]:
                              self.letras[p] = letra
                    print('você acertou.')
                    print(self.letras)

               else: 
                    n += 1
                    print(board[n])
                    print('você errou.')
                    self.tam -= 1
               
	
		
	# Método para verificar se o jogador venceu
     def resultado(self):
          if '_' not in self.letras:
               print('A palavra era %s parabéns, você venceu!' %(''.join(self.palavra)))
          else:
               print('Fim de jogo\nVocê perdeu!')
		


clear()
jogo1 = Hangman()
jogo1.adivinha_letra()
jogo1.resultado()

