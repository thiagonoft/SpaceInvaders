if mouse.is_over_area([facil1.x, facil1.y],[facil1.x + facil1.width, facil1.y + facil1.height]) and mouse.is_button_pressed(1):
    dificuldade = 1
    time.sleep(0.2)
    GameState = 0


if mouse.is_over_area([medio1.x, medio1.y],[medio1.x + medio1.width, medio1.y + medio1.height]) and mouse.is_button_pressed(1):
    dificuldade = 2
    time.sleep(0.2)
    GameState = 0

if mouse.is_over_area([dificil1.x, dificil1.y],[dificil1.x + dificil1.width, dificil1.y + dificil1.height]) and mouse.is_button_pressed(1):
    dificuldade = 3
    time.sleep(0.2)
    GameState = 0



#isso eh pra mudar a cor
fundo.draw()
if mouse.is_over_area([facil1.x, facil1.y],[facil1.x + facil1.width, facil1.y + facil1.height]):
    facil2.draw()
else:
    facil1.draw()

if mouse.is_over_area([medio1.x, medio1.y],[medio1.x + medio1.width, medio1.y + medio1.height]):
    medio2.draw()
else:
    medio1.draw()

if mouse.is_over_area([dificil1.x, dificil1.y],[dificil1.x + dificil1.width, dificil1.y + dificil1.height]):
    dificil2.draw()
else:
    dificil1.draw()

janela.update()