# area dos imports

import sys
from time import sleep

# Area reservada para as funções

def write(t):
    for letra in t:
        sys.stdout.write(letra)
        sys.stdout.flush()
        sleep(0.03)
        

def imprimir(frases):
    for f in frases:
        write('\n' + f + '\n')


# introdução do game
Abertura = [
    'Narrador: você acorda em uma cela suja e enferrujada com o barulho de uma multidão muito entusiasmada ...',
    'Narrador: não se lembra como foi parar nesse lugar.',
    'Narrador: então você se levanta e da uma olhada ao redor ...',
    'Narrador: observa que não tem nada além de uma grade que você pode ver dois soldados gladiando ao fundo e um velho sentado assistindo.',
    'Narrado: antes que você possa falar qualquer coisa o velho fala ...',
    'Velho: Você bebeu demais noite passada, posso ver que nem sabe como foi parar onde está, não tenho tempo para explicar você será o próximo a lutar, se prepare ...',
    'Narrador: o velho aponta pra umas armas em cima do banco.'
]

imprimir(Abertura)

#