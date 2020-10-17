fundo.draw()

f = open("rankings.txt", "r")
scores = [line.strip() for line in f]
scores3 = [int(x) for x in scores]

maioresScores = sorted(scores3, reverse=True)[:5]
if len(maioresScores) >0:
    score1 = str(maioresScores[0])
    janela.draw_text("1- " + score1, janela.width / 2 - 50, (float(janela.height) / 1.47164), 50, (255, 255, 255), "Arial",
                     False, False)
else:
    janela.draw_text("SEM SCORES, INICIE UMA PARTIDA!", 100, (float(janela.height) / 1.47164), 50, (255, 255, 255),
                     "Arial",
                     False, False)
if len(maioresScores) > 1:
    score2 = str(maioresScores[1])
    janela.draw_text("2- " + score2, janela.width / 2 - 50, (float(janela.height) / 1.47164 ) + 50, 50, (255, 255, 255),
                     "Arial",
                     False, False)
if len(maioresScores) > 2:
    score3 = str(maioresScores[2])
    janela.draw_text("3- " + score3, janela.width / 2 - 50, (float(janela.height) / 1.47164) + 100, 50, (255, 255, 255),
                     "Arial",
                     False, False)
if len(maioresScores) > 3:
    score4 = str(maioresScores[3])
    janela.draw_text("4- " + score4, janela.width / 2 - 50, (float(janela.height) / 1.47164) + 150, 50, (255, 255, 255),
                     "Arial",
                     False, False)

if teclado.key_pressed("ESC"):
    GameState = 0


janela.update()