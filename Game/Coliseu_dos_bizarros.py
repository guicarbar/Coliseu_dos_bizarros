# area dos imports

import sys
import os
from time import sleep
from random import randint

# area das variaveis


# sorte = int(randint(1,3))


sorte = 3

vida = 50
dano = 5
velocidade = 5
arma = 'espada'
defesa = 0

alet = randint(1,10)

# vida dos oponentes

oponente1 = 30
oponente2 = 40
oponente3 = 50




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
    
    
def pontos(n):
    for c in range(1, n+1):
        print('.')
        sleep(0.05)
        c += 1
        

def close():
    sys.exit()
    
    
def espada():
    global dano, velocidade
    dano = 5
    velocidade = 5
    arma = str('espada')
    
def machado():
    global dano, velocidade
    dano = 8
    velocidade = 3
    arma = str('Machado')


def adaga():
    global dano, velocidade
    dano = 3
    velocidade = 8
    arma = str('Adaga')

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
    'Narrador: e cada uma dessas armas terão atributos diferentes que iram influenciar em suas batalhas no coliseu.',
    'Narrador: escolha com sabedoria, boa sorte!!!'
]

tutorial_no = [
    'Narrador: vejo que você é o espertalhão.',
    'Narrador: boa sorte então!',
    'Narrador: que os jogos comecem',
    '...'
]

tutorial = str(input('Narrador: deseja saber como funciona o game ? S ou N    ')).upper()

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
    
  
# abertura do game

pontos(10)

linha()
print('         COLISEU DOS BIZARROS')
linha()

pontos(10)


menu = [
    'Narrador: Para iniciar o game basta digitar start',
    'Narrador: Se quiser sair do game basta digitar exit',
]

imprimir(menu)

comecar = 'Narrador: vamos lá então!!!'

close = [
    'Narrador: que pena, te vejo em uma proxima vez!',
    'Narrador: o programa vai ser fechado em 5 segundos.'
]

burro = [
    'Narrador: erro, não reconhecido a escolha do jogador, apenas respostas como start ou exit.',
    'Narrador: não seja burro',
    'Narrador: o jogo irá dar reset em 5 segundos'
]

start = str(input('Narrador: deseja iniciar o game?   ')).upper()

if start == 'START':
    imprimir(comecar)
    pontos(10)
elif start == 'EXIT':
    imprimir(close)
    pontos(10)
    close()
elif start != 'START' and start != 'EXIT':
    imprimir(burro)
    pontos(10)
    reset()

 

# sorte e seleção de arma


if sorte == 1:
    print(f'Narrador: sua sorte é {sorte}, parabéns você vai se ferrar muito.')
elif sorte == 2:
    print(f'Narrador: sua sorte é {sorte}, eeehhh da pro gasto, não vai passar tanto sufoco assim.')
elif sorte == 3:
    print(f'Narrador: sua sorte é {sorte}, OLHAAA ELE, VAI SER MOLEZINHA !!!')
    

pontos(5)


armas1 = [
    'Narrador: agora vamos escolher sua arma ...',
    'Narrador: lembrando que você tem 3 opções.',
    'Narrador: espada de cavaleiro – ela esta meio velha e gasta, mas ainda dá pra usar, vai aguentar bem.',
    'Narrador: ela é uma arma balanceada nem tão forte por ter o fio de sua lâmina já gasto.',
    'Narrador: e também não é tão rápida, o ferreiro que fez ela devia estar brava com o cavaleiro, ela é um pouco desequilibrada.'
]

armas2 = [
    'Narrador: machado de bárbaro – um machado grande e bem afiada com um cabo de mogno.',
    'Narrador:  seu antigo dono devia ser alguém q gostava de matar pois ele foi feito pra destruir tudo pela frente.',
    'Narrador: porem ele e com certeza mais pesado que a espada, por isso esse machado está aqui e não com o dono ...'
]

armas3 = [
    'Narrador: adaga de ladrão – uma bela adaga muito bonita, seu dono morreu a alguns minutos no coliseu ...',
    'Narrador: deve ser extremamente rápida em batalha.',
    'Narrador:  porem em lutas mano a mano vai ser difícil de causar o ataque que ela e capaz de infringir.'
]


imprimir(armas1)
pontos(3)

imprimir(armas2)
pontos(3)

imprimir(armas3)
pontos(3)


armas4 = [
    'Narrador: anda logo, escolhe sua arma',
    'Narrador: pra escolher e só digitar, espada, machado ou adaga, para a arma que você quer'
]

imprimir(armas4)
pontos(3)



escolha = str(input('Narrador: qual arma você quer?     ')).upper()


espada = [
    'Narrador: voce escolheu a espada.',
    'Narrador: uma boa escolha, neutra eu diria.',
    'Narrador: não me decepcione.'
]

machado = [
    'Narrador: você escolheu a machado.',
    'Narrador: essa escolha sua e interessante, vamos ver como você vai se sair.',
    'Narrador: não me decepcione.'
]

adaga = [
    'Narrador: você escolheu a adaga.',
    'Narrador: essa escolha sua e interessante, vamos ver como você vai se sair.',
    'Narrador: não me decepcione.'
]


if escolha == 'ESPADA':
    imprimir(espada)
    espada()
elif escolha == 'MACHADO':
    imprimir(machado)
    machado()
elif escolha == 'ADAGA':
    imprimir(adaga)
    adaga()


# apresentando atributos do jogados


pontos(10)

atributos = [
    'Narrado: vamos lembrar ...',
    'Narrado: seus atributos nessa partida são ...',
    f'Vida: {vida}'
    f'Arma: {arma}',
    f'Sorte: {sorte}',
    f'Dano: {dano}',
    f'Velocidade: {velocidade}'
    'Agora vamos continuar.'
]

pontos(5)
linha()



# inicio do game


luta1 = [
    'Narrador: após alguns minutos sentado no banco a grade da cela começa a se levantar lentamente.',
    f'Narrador: você pega sua {arma} e olha para o velho ...',
    'Velho: Boa sorte jovem!',
    'Narrador: você agradece com a cabeça e sai de sua cela ...',
    'Narrador: a multidão do coliseu está totalmente maluca, esperando uma luta das boas, já que as ultimas lutas não foram tão boas assim ...',
    'Narrador: você olha o redor e todos estão te assistindo e vê uma pessoa vindo em sua direção.',
    'Narrador: vocês dois começam a andar um na direção do outro.',
    'Narrador: quando chegam mais perto um do outro você o analisa.',
    'Narrador: é um homem em panos cheias de sangue, sem um braço e uma espada longa com um escudo redondo de ferro nas costas.',
    'Narrador: ele entra em posição de ataque com sua espada.',
    'Narrador: vc acena com a cabeça e entra em pose de ataque.',
    'Narrador: acho que a briga vai começar agora ...'
]

imprimir(luta1)

pontos(10)
linha()
print('         Soldado da solidão')
linha()
pontos(10)


'''


def azarataque():
    global dano, arma, alet
    
    if alet == 10:
        golpe = dano + 1
    elif 10 > alet > 5:
        golpe = dano - 1
    else:
        golpe = dano -2
        
               
def neutroataque():
    global dano, arma, alet
    
    if alet >= 9:
        golpe = dano + 2
    elif 10 > alet > 5:
        golpe = dano
    else:
        golpe = dano -1


def sorteataque():
    global dano, arma, alet
    
    if alet == 10:
        golpe = dano + 3
    elif 10 > alet > 5:
        golpe = dano + 1
    else:
        golpe = dano
        

def ataque():
    global sorte
    
    if sorte == 1:
        azarataque()
    elif sorte == 2:
        neutroataque()
    else:
        sorteataque()
        



















