import turtle

col=('red','green','cyan','blue','white','yellow')

t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(100):

    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
    '''my name is subhadip hensh'''
