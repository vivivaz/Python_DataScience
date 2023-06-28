from imagens import boneco
from lista import palavras
import random
import os

clear = lambda: os.system('cls')
letras = []
def jogo_forca():
    palavra = random.choice(palavras)
    palavra = list(palavra)
    print(palavra)
    tam = 7
    for t in range(len(palavra)):
        letras.append('_')
    print('Bem vindo ao jogo da forca!')
    print(boneco[6])
    print(letras)
    print(f'voce tem {tam} tentativas.')
    x = 1
    index = 5
    while tam != 0:
        if '_' not in letras:
            break
        letra = input('\ndigite uma letra: ').lower()
        if letra in palavra:
            for p in range(len(palavra)):
                if letra == palavra[p]:
                    letras[p] = letra
            print(letras)
            print('voce acertou!')
        else:
            print(boneco[index])
            print('voce errou!')
            if index > 0:
                index -= 1
        tam -= 1
            
clear()
jogo_forca()

if '_' in letras:
    print('voce perdeu!')
else:
    print('voce ganhou, parabens!')
print('Fim de jogo!')
# criar uma inteligencia artificial (chat gpt) que recebe uma base de dados e responde perguntas sobre os dados, automatiza análise exploratória