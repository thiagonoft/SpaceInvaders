from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
import time
from PPlay.sprite import *
import numpy
from PPlay.collision import *
import random


janela = Window(1024,700)
janela.set_title("Space Invaders")

fundo = GameImage("GameImages\menubackground.png")

#botoes do menu
jogar1 = GameImage("GameImages\jogar1.png")
jogar2 = GameImage("GameImages\jogar2.png")
dificuldade1 = GameImage("GameImages\dificuldade1.png")
dificuldade2 = GameImage("GameImages\dificuldade2.png")
rank1 = GameImage("GameImages\srank1.png")
rank2 = GameImage("GameImages\srank2.png")
sair1 = GameImage("GameImages\sair1.png")
sair2 = GameImage("GameImages\sair2.png")
facil1 = GameImage("GameImages\sfacil1.png")
facil2 = GameImage("GameImages\sfacil2.png")
medio1 = GameImage("GameImages\medio1.png")
medio2 = GameImage("GameImages\medio2.png")
dificil1 = GameImage("GameImages\dificil1.png")
dificil2 = GameImage("GameImages\dificil2.png")


#nave
nave = Sprite("GameImages\snave.png")
nave.y = (float(janela.height)/1.16667)
nave.x = janela.width/2 - nave.width
velnave = 250
tiros = []
veltiro = 700
score = 0
scores = []

#inimigos
tirosinimigos = []
velinimigos = 100
veltiro2 = 200
inimigos = [[0 for x in range(10)] for x in range(10)]
inimigo1 = Sprite("GameImages\sinimigo1.png")
descida = inimigo1.width/4
ovni = Sprite("GameImages\sovni.png")
velovni = 70
ovni.x = janela.width

def spawn():
    for x in range(10):
        for y in range(10):
            inimigo = Sprite("GameImages\sinimigo1.png")
            inimigo.set_position(x*inimigo.width, y*inimigo.height)
            inimigos[y][x] = inimigo
spawn()

def atirador(matriz):
    #retorna uma lista com os inimigos que vão atirar
    j = -2
    atiradores = []
    for x in matriz[-1]:
        if x != 0:
            atiradores += [x]
    while j >= len(matriz)*(-1):
        for i in range(len(matriz)):
            if matriz[j][i] != 0 and matriz[j+1][i] == 0:
                atiradores += [matriz[j][i]]
        j -= 1
    return atiradores

#otimizacao
def ultima_linha(matriz):
    # retorna um inimigo da ultima linha
    j = -1
    for i in range(len(matriz)):
        for x in matriz[j]:
            if x != 0:
                return x
        j -= 1
def esquerda(matriz):
    # retorna a posicao x do inimigo mais a esquerda
    j = -1
    l = []
    for i in range(len(matriz)):
        for x in matriz[j]:
            if x != 0:
                l += [x.x]
                break
        j -= 1
    return(min(l))

def direita(matriz):
    # retorna a posicao x do inimigo mais a direita
    j = -1
    l = []
    for i in range(len(matriz)):
        for x in reversed(matriz[j]):
            if x != 0:
                l += [x.x]
                break
        j -= 1
    return(max(l))

def mov_inimigos():
    global velinimigos
    if direita(inimigos)  >= janela.width - inimigo1.width:
        velinimigos = -100
    elif esquerda(inimigos) <= 0:
        velinimigos = 100
    for linha in range(10):
        for coluna in range(10):
            if inimigos[linha][coluna] != 0:
                inimigos[linha][coluna].move_x(velinimigos * janela.delta_time())
    if direita(inimigos) >= janela.width - inimigo1.width or esquerda(inimigos) < 0:
        for x in inimigos:
            for y in x:
                if y != 0:
                    y.y += descida

def restart():
    # reinicia o jogo
    global GameState
    global score
    global scores
    global inimigos
    global tiros
    global tirosinimigos
    global velinimigos
    GameState = 0
    del inimigos
    del tiros
    del tirosinimigos
    scores2 = open("rankings.txt","a")
    scores2.write("%d \n"  %score)
    scores2.close()
    score = 0
    descida = inimigo1.width/4
    tiros = []
    tirosinimigos = []
    inimigos = [[0 for x in range(10)] for x in range(10)]
    ovni.x = janela.width
    tempinho2 = 0
    vezesganhadas = 0
    spawn()

vezesganhadas = 0

#posicao dos botoes do menu
jogar1.x = janela.width/2 - jogar1.width/2
jogar2.x = janela.width/2 - jogar1.width/2
dificuldade1.x = janela.width/2 - dificuldade1.width/2
dificuldade2.x = janela.width/2 - dificuldade1.width/2
rank1.x = janela.width/2 - rank1.width/2
rank2.x = janela.width/2 - rank1.width/2
sair1.x = janela.width/2 - sair1.width/2
sair2.x = janela.width/2 - sair1.width/2


jogar1.y = (float(janela.height)/1.47164)
jogar2.y = (float(janela.height)/1.47164)
dificuldade1.y = (float(janela.height)/1.31374)
dificuldade2.y = (float(janela.height)/1.31374)
rank1.y = (float(janela.height)/1.18288)
rank2.y = (float(janela.height)/1.18288)
sair1.y = (float(janela.height)/1.08923)
sair2.y = (float(janela.height)/1.08923)


#posicao dos botoes dificuldade
facil1.x = janela.width/2 - facil1.width/2
facil2.x = janela.width/2 - facil2.width/2
medio1.x = janela.width/2 - medio1.width/2
medio2.x = janela.width/2 - medio2.width/2
dificil1.x = janela.width/2 - dificil1.width/2
dificil2.x = janela.width/2 - dificil2.width/2

facil1.y = (float(janela.height)/1.47164)
facil2.y = (float(janela.height)/1.47164)
medio1.y = (float(janela.height)/1.31374)
medio2.y = (float(janela.height)/1.31374)
dificil1.y = (float(janela.height)/1.18288)
dificil2.y = (float(janela.height)/1.18288)

#contador
contador = 0
tempotranscorrido = 0
fps = 0
tempinho = 100
tempinho2 = 0



mouse = Mouse()
teclado = Window.get_keyboard()


dificuldade = 2
GameState = 0
Running = True

while Running:
    while GameState == 0:
        exec(open("menu.py").read())

    while GameState == 1:
        exec(open("game.py").read())

    while GameState == 2:
        exec(open("dificuldade.py").read())

    while GameState == 3:
        exec(open("rank.py").read())


#lista de tiros, espaço add na lista, sair da tela remove da lista, desenhar toda a lista
#framerate = 1/deltatime
#tempotranscorrido += janela.deltatime()
#contador += 1
#if tmepotranscorrido >= 1  fps = contador
#contador, tempotranscorrido = 0,0
#desenhar em all os fps
