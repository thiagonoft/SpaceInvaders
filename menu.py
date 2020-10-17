#isso eh pra clicar e ir pros lugares
if mouse.is_over_area([jogar1.x, jogar1.y],[jogar1.x + jogar1.width, jogar1.y + jogar1.height]) and mouse.is_button_pressed(1):
    time.sleep(0.2)
    GameState = 1
if mouse.is_over_area([dificuldade1.x, dificuldade1.y],[dificuldade1.x + dificuldade1.width, dificuldade1.y + dificuldade1.height]) and mouse.is_button_pressed(1):
    time.sleep(0.2)
    GameState = 2
if mouse.is_over_area([rank1.x, rank1.y],[rank1.x + rank1.width, rank1.y + rank1.height]) and mouse.is_button_pressed(1):
    time.sleep(0.2)
    GameState = 3
if mouse.is_over_area([sair1.x, sair1.y],[sair1.x + sair1.width, sair1.y + sair1.height]) and mouse.is_button_pressed(1):
    janela.close()

# isso eh pra mudar de cor
fundo.draw()
if mouse.is_over_area([jogar1.x, jogar1.y],[jogar1.x + jogar1.width, jogar1.y + jogar1.height]):
    jogar2.draw()
else:
    jogar1.draw()
if mouse.is_over_area([dificuldade1.x, dificuldade1.y],[dificuldade1.x + dificuldade1.width, dificuldade1.y + dificuldade1.height]):
    dificuldade2.draw()
else:
    dificuldade1.draw()
if mouse.is_over_area([rank1.x, rank1.y],[rank1.x + rank1.width, rank1.y + rank1.height]):
    rank2.draw()
else:
    rank1.draw()
if mouse.is_over_area([sair1.x, sair1.y],[sair1.x + sair1.width, sair1.y + sair1.height]):
    sair2.draw()
else:
    sair1.draw()
janela.update()

