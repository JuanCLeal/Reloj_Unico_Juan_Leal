Segundero = 0
Minutero = 0
Horario = 0

def setup():
    size(500, 500)
    
def draw():
    global Segundero
    global Minutero
    global Horario
    background (0)
    noStroke ()
    fill(0, 0, 255)
    Horario = map(hour(), 0, 24, 0, TWO_PI)
    arc(250, 250, 400, 400, 0, Horario)
    fill(0, 255, 0)
    Minutero = map(minute(), 0, 59, 0, TWO_PI)
    arc(250, 250, 275, 275, 0, Minutero)
    fill (255, 0, 0)
    Segundero = map(second(), 0, 59, 0, TWO_PI)
    arc(250, 250, 150, 150, 0, Segundero)
