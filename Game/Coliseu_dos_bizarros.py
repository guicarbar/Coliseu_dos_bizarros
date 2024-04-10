# area dos imports

import sys
import os
from time import sleep
from random import randint

# area das variaveis


sorte = int(randint(1,3))

vida = 50
dano = 0
velocidade = 0
arma = 0
escudo = False

golpe = 0
sofrido = 0

# vida dos oponentes

oponente1 = 30
danooponente1 = 4

oponente2 = 40
danooponente2 = 5

oponente3 = 50
danooponente3 = 6




# Area reservada para as funções

def write(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.001)
        

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
    global dano, velocidade, arma
    dano = 5
    velocidade = 5
    arma = 'espada'


def machado():
    global dano, velocidade, arma
    dano = 8
    velocidade = 3
    arma = 'Machado'


def adaga():
    global dano, velocidade, arma
    dano = 3
    velocidade = 8
    arma = 'Adaga'


def azarataque():
    global dano
    
    alet = randint(1,20)
    
    if alet == 20:
        golpe = dano + 1
    elif 20 > alet >= 9:
        golpe = dano - 1
    else:
        golpe = dano -2
    return golpe

      
def neutroataque():
    global dano
    
    alet = randint(1,20)
    
    if alet >= 18:
        golpe = dano + 2
    elif 17 >= alet >= 7:
        golpe = dano
    else:
        golpe = dano -1
    return golpe


def sorteataque():
    global dano
    
    alet = randint(1,20)
    
    if alet > 16:
        golpe = dano + 3
    elif 16 >= alet >= 5:
        golpe = dano + 1
    else:
        golpe = dano
    return golpe

def azarataquepesado():
    global dano
    
    alet = randint(1,100)
    
    if alet > 95:
        golpe = dano * 2
    elif alet <= 95 or alet > 60:
        golpe = dano 
    else:
        golpe = dano - 1
    return golpe

      
def neutroataquepesado():
    global dano
    
    alet = randint(1,100)
    
    if alet > 90:
        golpe = dano * 2
    elif alet <= 90 or alet > 50:
        golpe = dano 
    else:
        golpe = dano - 1
    return golpe


def sorteataquepesado():
    global dano
    
    alet = randint(1,100)
    
    if alet > 85:
        golpe = dano * 2
    elif alet <= 85 or alet > 40:
        golpe = dano 
    else:
        golpe = dano - 1
    return golpe


def ataquepesado():
    global sorte, golpe
    
    if sorte == 1:
        golpe = azarataquepesado()
    elif sorte == 2:
        golpe = neutroataquepesado()
    else:
        golpe = sorteataquepesado()


def ataqueleve():
    global sorte, golpe
    
    if sorte == 1:
        golpe = azarataque()
    elif sorte == 2:
        golpe = neutroataque()
    else:
        golpe = sorteataque()


def menosvidao(oponente):
    global golpe, oponente1, oponente2, oponente3
    
    if oponente == 'oponente1':
        oponente1 -= golpe
        return oponente1
    elif oponente == 'oponente2':
        oponente2 -= golpe
        return oponente2
    elif oponente == 'oponente3':
        oponente3 -= golpe
        return oponente3


def esquivaazarada(z):
    global velocidade, sofrido
    
    if velocidade == 8:
        sofrido = z
    elif velocidade == 5:
        sofrido = z + 1
    elif velocidade == 3:
        sofrido = z + 2
    return sofrido


def esquivaneutra(z):
    global velocidade, sofrido
    
    if velocidade == 8:
        sofrido = z -1
    elif velocidade == 5:
        sofrido = z
    elif velocidade == 3:
        sofrido = z + 1
    return sofrido


def esquivasortuda(z):
    global velocidade, sofrido
    
    if velocidade == 8:
        sofrido = z - 2
    elif velocidade == 5:
        sofrido = z - 1
    elif velocidade == 3:
        sofrido = z
    return sofrido


def esquiva(z):
    global sorte, sofrido
    
    if sorte == 1:
        sofrido = esquivaazarada(z)
    elif sorte == 2:
        sofrido = esquivaneutra(z)
    else:
        sofrido = esquivasortuda(z)


def escudoouesquiva(z):
    global escudo, sofrido
    
    if escudo == False:
        esquiva(z)
    if escudo == True:
        escolhadefesa(z)


def menosvida():
    global sofrido, vida

    vida -= sofrido

def pegarescudo():
    global escudo
    
    escudo = True


def escudoazar(z):
    global velocidade, sofrido
    
    if velocidade == 8:
        sofrido = z - 1
    elif velocidade == 5:
        sofrido = z - 2
    elif velocidade == 3:
        sofrido = z - 3
    return sofrido


def escudoneutro(z):
    global velocidade, sofrido
    
    if velocidade == 8:
        sofrido = z 
    elif velocidade == 5:
        sofrido = z - 1
    elif velocidade == 3:
        sofrido = z - 2
    return sofrido


def escudosorte(z):
    global velocidade, sofrido
    
    if velocidade == 8:
        sofrido = z - 1
    elif velocidade == 5:
        sofrido = z - 2 
    elif velocidade == 3:
        sofrido = z - 3
    return sofrido


def usarescudo(z):
    global sorte
    
    if sorte == 1:
        escudoazar(z)
    elif sorte == 2:
        escudoneutro(z)
    else:
        escudosorte(z)


def escolhadefesa(z):
    ddef = str(input('usar escudo ou esquiva ?')).upper()
    
    if ddef == 'ESCUDO':
        usarescudo(z)
    elif ddef == 'ESQUIVA':
        esquiva(z)
    else:
        print('sorry nn entendi')
        escolhadefesa(z)


def vereificarvidaplayer():
    if vida <= 0:
        imprimir(mensagemmorte)
        pontos(10)
        reset()
    else:
        imprimir(mensagemcontinuar)


def beber():
    global vida
    
    vida += 20
    print('Narrador: voce sente suas feridas se fechando')


def quebrar():
    global sorte
    
    sorte += 1
    print('Narrador: voce sente sua sorte aumentando')


def pocao():
    beberounao = str(input('vc vai beber ou nao a poção? s ou n')).upper()
    
    if beberounao == 'S':
        beber()
    elif beberounao == 'N':
        quebrar()
    else:
        print('Narrador: não é uma opção valida, vamos lá cara ...')
        pocao()



# introdução do game



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
    mensagemerro = [
        'Narrador: erro, não reconhecido a escolha do jogador, apenas respostas como s ou n.',
        'Narrador: o jogo irá dar reset em 5 segundos'
    ]
    imprimir(mensagemerro)
    for c in range(1,6):
        print('.')
        c += 1
        sleep(1)
    reset()
    

  
# abertura do game



pontos(10)

linha()
mensagemabertura = ['         COLISEU DOS BIZARROS']
imprimir(mensagemabertura)
linha()

pontos(10)


menu = [
    'Narrador: Para iniciar o game basta digitar start',
    'Narrador: Se quiser sair do game basta digitar exit',
]

imprimir(menu)

comecar = ['Narrador: vamos lá então!!!']

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
    mensagemazar = [f'Narrador: sua sorte é {sorte}, parabéns você vai se ferrar muito.']
    imprimir(mensagemazar)
elif sorte == 2:
    mensagemneutra = [f'Narrador: sua sorte é {sorte}, eeehhh da pro gasto, não vai passar tanto sufoco assim.']
    imprimir(mensagemneutra)
elif sorte == 3:
    mensagemsorte = [f'Narrador: sua sorte é {sorte}, OLHAAA ELE, VAI SER MOLEZINHA !!!']
    imprimir(mensagemsorte)


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

mensagemespada = [
    'Narrador: voce escolheu a espada.',
    'Narrador: uma boa escolha, neutra eu diria.',
    'Narrador: não me decepcione.'
]

mensagemmachado = [
    'Narrador: você escolheu a machado.',
    'Narrador: essa escolha sua e interessante, vamos ver como você vai se sair.',
    'Narrador: não me decepcione.'
]

mensagemadaga = [
    'Narrador: você escolheu a adaga.',
    'Narrador: essa escolha sua e interessante, vamos ver como você vai se sair.',
    'Narrador: não me decepcione.'
]


if escolha == 'ESPADA':
    imprimir(mensagemespada)
    espada()
elif escolha == 'MACHADO':
    imprimir(mensagemmachado)
    machado()
elif escolha == 'ADAGA':
    imprimir(mensagemadaga)
    adaga()
else:
    print("Opção inválida! Por favor, escolha entre 'ESPADA', 'MACHADO' ou 'ADAGA'.")



# apresentando atributos do jogados



pontos(10)

atributos = [
    'Narrado: vamos lembrar ...',
    'Narrado: seus atributos nessa partida são ...',
    f'Vida: {vida}',
    f'Arma: {arma}',
    f'Sorte: {sorte}',
    f'Dano: {dano}',
    f'Velocidade: {velocidade}',
    'Agora vamos continuar.'
]

imprimir(atributos)

pontos(5)



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
    'Narrador: aquele escudo parece ser um item bom ...'
    'Narrador: ele entra em posição de ataque com sua espada.',
    'Narrador: vc acena com a cabeça e entra em pose de ataque.',
    'Narrador: acho que a briga vai começar agora ...'
]

imprimir(luta1)

pontos(10)
linha()
adversario1 = ['         Soldado da solidão']
imprimir(adversario1)
linha()
pontos(10)



mensagens1luta1 = ['Narrador: você cheio de confiança parte para atacar primeiro ...']

imprimir(mensagens1luta1)


mensagemmorte = [
    'Narrador: você e péssimo nesse jogo, HORRIVEL.',
    'Narrador: vamos começar de novo.',
    'Narrador: jogo reiniciara em 5 segundos.'
]

mensagemcontinuar = [
    'Narrador: tudo certo, vamos continuar.'
]


mensagens2luta1 = [
        f'Narrador: você causou {golpe} de dano ao seu oponente',
        f'Narrador: ele ficou com {oponente1} de vida restante.',
        'Narrador: enquanto se recupera do golpe que acabou de desferir, seu oponente vem em sua direção para te atacar.',
        'Narrador: acho q é sua vez de se defender.'
    ]


mensagens3luta1 = [            
        f'Narrador: você se esquivou tomando apenas {sofrido} de dano do seu oponente.',
        f'Narrador: após esse golpe você ficou com {vida} de vida restante.',
        'Narrador: tome cuidado na proxima vez'
    ]


def ciclodeluta1():
    global oponente1
    
    atq = input('atque leve ou pesado ? resposta leve ou pesado').upper()
    
    if atq == 'LEVE':
        ataqueleve()
    elif atq == 'PESADO':
        ataquepesado()
    else:
        print('erro ao reconhecer a escolha')
        pontos(5)
        ciclodeluta1()
    
    
    menosvidao('oponente1')

    imprimir(mensagens2luta1)

    escudoouesquiva(danooponente1)
    
    menosvida()
    
    imprimir(mensagens3luta1)



while oponente1 > 0:    
    vereificarvidaplayer()
    ciclodeluta1()



# entre lutas



terminodeluta1 = [
    'Narrador: e com um último golpe você finaliza seu oponente.',
    'Narrador: o coliseu inteiro entra em alvoroço por ver a melhor luta da noite até esse momento.',
    'Narrador:  mas a única coisa que você consegue escutar é o ultimo suspiro de seu adversário.',
    'Narrador: ele morre em silencio com um olhar de agradecimento.',
    'Narrador: enquanto escuta o barulho da multidão observa o escudo amarrado nas costas do corpo dele ...',
    'Narrador: e pensa ser uma boa ideia usar esse escudo nas próximas lutas, já q parece que essa não será a última luta da noite ...',
    'Narrador:  você pega o escudo e o empunha na outra mão.',
    'Narrador: após alguns segundo parado ali com o barulho da multidão diminuído cada vez mais, você sente ficar mais forte.',
    'Narrador: enquanto pensa de onde vem essa força percebe que tem outra cela se abrindo.',
    'Narrador: dela sai uma figura correndo em sua direção.',
    'Narrador: você entra em posição de ataque e se prepara para a próxima luta ...'
]

pegarescudo()

imprimir(terminodeluta1)

pontos(10)
linha()
print('         O maniaco')
linha()
pontos(10)



# luta 2



def ciclodeluta2():
    global oponente2
    
    atq = input('atque leve ou pesado ? resposta leve ou pesado').upper()
    
    if atq == 'LEVE':
        ataqueleve()
    elif atq == 'PESADO':
        ataquepesado()
    else:
        print('erro ao reconhecer a escolha')
        pontos(5)
        ciclodeluta2()

    menosvidao('oponente2')

    imprimir(mensagens2luta1)
    
    escudoouesquiva(danooponente2)
    
    menosvida()
    
    imprimir(mensagens3luta1)


while oponente2 > 0:
    vereificarvidaplayer()
    ciclodeluta2()



# entre as lutas


terminodeluta2 = [
    'Narrador: você desfere um golpe fatal em seu oponente.',
    'Narrador: ele segura seu braço e olha nos eu olhos enquanto morre.',
    'Narrador: você pode ver a vida esvaindo de seu corpo.',
    'Narrador: e nesse momento você consegue analisar como era seu oponente.',
    'Narrador: a luta início tão rápida que nem consegui ver que ele era forte e tinha o corpo inteiro cheio de cicatrizes.',
    'Narrador: enquanto pensa nessa luta e sente ficando mais forte escuta uma gargalhada ...',
    'Narrador: olha para a plateia e vê um rei dando risada, ele joga um frasco para você.',
    'Narrador: você o agarra e percebe que ele tem um liquido verde dentro.',
    'Narrador: você não sabe para que serve e muito menos o que é.'
]

imprimir(terminodeluta2)

pocao()

proxima = [
    'Narrador: enquanto sente a magia acontecendo dentro do seu corpo.',
    'Narrador: você vê outra cela se abrindo.',
    'Narrador: nesse momento a plateia fica em silencio pela primeira vez.',
    'Narrador: de dentro da sombra da cela sai um homem alto e muto forte com um martelo gigante nas mãos.',
    'Narrador: ele anda calmamente em sua direção.',
    'Narrador: quanto mais se aproxima dele, você vê que ele está chorando e resmungando em uma língua desconhecida ...',
    'Narrador: você acha engraçado isso, talvez esse foi o primeiro sorriso da noite.',
    'Narrador: mas mesmo assim se prepara para a luta.',
    'Narrador: e do nada o homem da uma marretada no chão extremamente furioso, enxuga suas lagrimas e se prepara.',
    'Narrador: que a luta comece então.'
]

pontos(10)
linha()
print('         O gigante lamentador')
linha()
pontos(10)



# luta 3



def ciclodeluta3():
    global oponente3
    
    atq = input('atque leve ou pesado ? resposta leve ou pesado').upper()
    
    if atq == 'LEVE':
        ataqueleve()
    elif atq == 'PESADO':
        ataquepesado()
    else:
        print('erro ao reconhecer a escolha')
        pontos(5)
        ciclodeluta3()

    menosvidao('oponente3')

    imprimir(mensagens2luta1)
    
    escudoouesquiva(danooponente3)
    
    menosvida()
    
    imprimir(mensagens3luta1)



while oponente3 > 0:
    vereificarvidaplayer()
    ciclodeluta3()


# fim do game


lutafinal = [
    'Narrador: com dois golpes cansados você finaliza seu oponente.',
    'Narrador: e pela segunda vez nessa noite a plateia fica em silencio.',
    'Narrador: você olha para o gigante caído no chão e sente alivio.',
    'Narrador: pensa que está prestes a ter um infarto, seu coração não para de bater desesperadamente.',
    'Narrador: nesse momento você olha para o rei, ele já está te encarando.',
    'Narrador: da uma gargalhada e puxa uma alavanca que estava do seu lado.',
    'Narrador: e fala te agradecendo.',
    'Rei: você divertiu minha noite, você está livre para ir embora.',
    'Narrador: você percebe que um portão de madeira se abre, parece ser uma saída.',
    'Narrador: você caminha em direção ...',
    'Narrador: atravessa e percebe que está em uma cidade livre para ir e vir a hora que quiser.',
    'Narrador: você anda por uns minutos pela cidade, você só queria sair de perto daquele lugar.',
    'Narrador: encontra uma praça e senta em um banco.',
    'Narrador: acaba pegando no sono ali mesmo ...',
    'Narrador: assim acaba sua jornada.',
    'Narrador: obrigado por jogar'
]


final = str(input('Gostou do game ? s ou n')).upper()

if final == 'S':
    print('Narrador: que otimo, te agradeço por isso!')
elif final == 'N':
    print('Narrador: nao ligo para a sua opniao, tchau')
else:
    print('Narrador: burro dmais não é possivel ...')

pontos(10)
close()