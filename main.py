
import turtle  # importation du module turtle

turtle.up()  # tant que la tortue est en mode “up”,
turtle.shape('turtle')  # change la forme de la tortue (en tortue)


def rectangle(x, y, size1, size2):
    turtle.goto(x, y)

    turtle.color('light green')  # la tortue est bleue
    turtle.down()  # tant que la tortue est “down”, elle tracera la ligne de ses déplacements)
    turtle.begin_fill()  # va remplir l’intérieur de ce qui est tracé entre maintenant et le turtle.end_fill() ultérieur
    turtle.forward(size1)  # la tortue avance de 300 (à droite)
    turtle.right(90)  # la tortue effectue une rotation de 144° à droite
    turtle.forward(size2)  # avance dans la nouvelle direction
    turtle.right(90)  # rotation
    turtle.forward(size1)  # avance
    turtle.right(90)
    turtle.forward(size2)
    turtle.right(90)
    turtle.end_fill()  # remplit ce qui a été tracé entre le begin_fill et cette instruction
    turtle.up()


rectangle(0, 0, 100, 250)
rectangle(-75, -75, 250, 100)

# et cette instruction
turtle.hideturtle()  # cache la tortue
turtle.done()  # laisse l'utilisateur fermer la fenêtre
