from turtle import*  
import colorsys 


#velocidade do deenho e mudando fundo da tela
speed(0)
bgcolor("black")

#valor de inicio

h=0

#repetições 

for i in range(16):
    for j in range (18):

#coresecirculos 
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h += 0.005
        circle(150-j*6,90)
        left(90)
        circle(150-j*6,90)
        right(180)
        circle(40,24)

