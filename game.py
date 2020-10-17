
if teclado.key_pressed("ESC"):
    restart()
    GameState = 0

ganhou = True
for x in inimigos:
    for y in x:
        if y != 0:
            ganhou = False
if ganhou:
    tiros = []
    vezesganhadas += 1
    if vezesganhadas < 3:
        descida += inimigo1.width/2
        spawn()
    else:
        GameState = 0
        restart()

ganhou = False
#movimentacao da nave

if nave.x <= 0 and teclado.key_pressed("LEFT"):
    nave.x = nave.x
elif nave.x >= janela.width - nave.width and teclado.key_pressed("RIGHT"):
    nave.x = nave.x
else:
    if teclado.key_pressed("LEFT"):
        nave.x = nave.x - velnave * janela.delta_time()
    if teclado.key_pressed("RIGHT"):
        nave.x = nave.x + velnave * janela.delta_time()

#tiros
tiro = Sprite("GameImages\stiro2.png")
tiro.x = nave.x
tiro.y = nave.y
for aaa in tiros:
    aaa.y -= veltiro*janela.delta_time()

tempinho += 1
if teclado.key_pressed("SPACE") and tempinho >= 50*dificuldade:
    tiros += [tiro]
    tempinho = 0



#tiros dos inimigos
if random.random()*100 >= 99:
    tiroinimigo = Sprite("GameImages\stiro3.png")
    k = int(random.random() * len(atirador(inimigos))-1)
    tiroinimigo.x = atirador(inimigos)[k].x + inimigo1.width/2
    tiroinimigo.y = atirador(inimigos)[k].y + inimigo1.height
    tirosinimigos += [tiroinimigo]
for rrr in tirosinimigos:
    rrr.y += veltiro2*janela.delta_time()

#removendo os tiros quando sairem da tela
if len(tiros) >= 1:
    if tiros[0].y <= (-1)*tiro.height:
        tiros.pop(0)
if len(tirosinimigos) >= 1:
    if tirosinimigos[0].y >= janela.width:
        tirosinimigos.pop(0)

mov_inimigos()

#colisao dos tiros com os inimigos
if len(tiros) > 0:
    for x in tiros:
        # if x.y <= ultima_linha(inimigos).y + inimigo1.height and x.x >= esquerda(inimigos) and x.x <= direita(inimigos) + inimigo1.width:
        for linha in range(10):
            for coluna in range(10):
                for b in tiros:
                    if inimigos[linha][coluna] != 0:
                        if Collision.collided(inimigos[linha][coluna],b):
                            inimigos[linha][coluna] = 0
                            tiros.remove(b)
                            score += 50

for x in tiros:
    if x.y >= ovni.y:
        if Collision.collided(x,ovni):
            tiros.remove(x)
            ovni.x = janela.width
            score+= 150

#colisao dos tiros inimigos com a nave
for x in tirosinimigos:
    if x.y >= nave.y and x.x >= nave.x and x.x <= nave.x + nave.width:
        if Collision.collided(x,nave):
            restart()

#OVNI
tempinho2 += 1
if tempinho2 >= 500:
    if random.random()*1000 >= 999 and ovni.x >= janela.width:
        ovni.x = 0
        tempinho2 = 0

if ovni.x <= janela.width:
    ovni.move_x(velovni * janela.delta_time())


#fps
tempotranscorrido += janela.delta_time()
contador += 1
if tempotranscorrido >= 1:
    fps = contador
    contador = 0
    tempotranscorrido = 0


janela.set_background_color([0,0,0])
for tey in tiros:
    tey.draw()
for teytey in tirosinimigos:
    teytey.draw()
nave.draw()
for x in inimigos:
    for i in range(10):
        if x[i] != 0:
            x[i].draw()


ovni.draw()
janela.draw_text("%d" %fps, 0, 0, 30,(255,255,255),"Arial", False, False)
janela.draw_text("%d" %score, 100, 0, 30,(255,255,255),"Arial", False, False)
janela.update()