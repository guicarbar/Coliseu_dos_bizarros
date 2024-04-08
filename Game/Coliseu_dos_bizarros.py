# area dos imports

import sys
import os
from time import sleep

# Area reservada para as funções

def write(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.05)
        

def imprimir(frases):
    for f in frases:
        write('\n' + f + '\n')


def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    

def linha():
    print('-'*40)
        

# introdução do game

'''

Abertura = [
    'Narrador: você acorda em uma cela suja e enferrujada com o barulho de uma multidão muito entusiasmada ...',
    'Narrador: não se lembra como foi parar nesse lugar.',
    'Narrador: então você se levanta e da uma olhada ao redor ...',
    'Narrador: observa que não tem nada além de uma grade que você pode ver dois soldados gladiando ao fundo e um velho sentado assistindo.',
    'Narrado: antes que você possa falar qualquer coisa o velho fala ...',
    'Velho: Você bebeu demais noite passada, posso ver que nem sabe como foi parar nesse lugar, não tenho tempo para explicar você será o próximo a lutar, se prepare ...',
    'Narrador: o velho aponta pra umas armas em cima do banco.'
    '...'
]

imprimir(Abertura)

# Tutorial do game

tutorial_yes = [
    'Narrador: é bem simples vou te explicar ...',
    'Narrador: na próxima área ao dar start você será redirecionado para uma área onde irei sortear a sua sorte do dia.',
    'Narrador: ela pode ser 1,2 ou 3 – sendo 1 azarado e 3 sortudos.',
    'Narrador: sua sorte influencia na forma como o jogo funciona.',
    'Narrador: após escolher sua sorte você terá que escolher sua arma.',
    'Narrador: que também tem 3 opções.',
    'Narrador: espada de cavaleiro, machado de bárbaro e adaga de ladrão.',
    'Narrador: e cada uma dessas armas terão atributos diferentes q iram influenciar em suas batalhas no coliseu.',
    'Narrador: escolha com sabedoria, boa sorte!!!'
]

tutorial_no = [
    'Narrador: vejo que você é o espertalhão.',
    'Narrador: boa sorte então!',
    'Narrador: que os jogos comecem',
    '...'
]

tutorial = str(input('Deseja saber como funciona o game ? S ou N    ')).upper()

if tutorial == 'S':
    imprimir(tutorial_yes)
elif tutorial == 'N':
    imprimir(tutorial_no)
elif tutorial != 'S' and tutorial != 'N':
    print('Narrador: erro, não reconhecido a escolha do jogador, apenas respostas como s ou n.')
    print('Narrador: o jogo irá dar reset em 5 segundos')
    for c in range(1,6):
        print('.')
        c += 1
        sleep(1)
    reset()
    
'''    
# abertura do game

linha()
print('         COLISEU DOS BIZARROS')
linha()

for c in range(1,11):
    print('.')
    sleep(0.05)


inicio = [
    'Narrador: Para iniciar o game basta digitar ‘start’',
    'Narrador: Se quiser sair do game basta digitar ‘exit’',
    'Narrador: Não seja burro é sem as aspas'
]

imprimir(inicio)

start = str(input('Deseja iniciar o game?   ')).upper()

if start == 'START':
    for c in range(1,11):
        print('.')
        sleep(0.05)
elif start == 'EXIT':
    print('ainda nn tem')
elif start != 'START' and start != 'EXIT':
    print('Narrador: erro, não reconhecido a escolha do jogador, apenas respostas como start ou exit.')
    print('Narrador: não seja burro')
    print('Narrador: o jogo irá dar reset em 5 segundos')
    for c in range(1,6):
        print('.')
        c += 1
        sleep(1)
    reset()


# sorte e seleção de arma

