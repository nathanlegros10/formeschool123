from turtle import *
import time

n=15
d = 25

def triangle():
    color('blue')
    forward(n)
    left(120)
    forward(n)
    left(120)
    forward(n)
    left(120)


def carre():
    color('red')
    forward(n)
    left(90)
    forward(n)
    left(90)
    forward(n)
    left(90)    
    forward(n)
    left(90) 



def leve():
    up()
    forward(d)
    down()

for i in range(5):
    triangle()
    leve()
    carre()
    leve()
    n = n + 10
    d = d + 10



time.sleep(10)


####   triangle()
####   carre()