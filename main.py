#import colorgram
import random
#rgb_c=[]
#colors=colorgram.extract('img.jpg.jpeg',30)
#for color in colors:
# r=color.rgb.r
 #  g = color.rgb.g
  #  b = color.rgb.b
   # new_c=(r,g,b)
    #rgb_c.append(new_c)


#print(rgb_c)
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(0)
tim.hideturtle()
screen = Screen()
screen.colormode(255)
color_list = [(230, 238, 246), (235, 245, 240), (200, 157, 115), (43, 110, 146), (134, 172, 193), (226, 208, 113),
              (134, 84, 67), (148, 65, 85), (198, 140, 153), (193, 83, 102), (182, 159, 51), (150, 178, 164),
              (191, 98, 83), (68, 114, 94), (227, 170, 182), (36, 51, 68), (225, 177, 168), (45, 157, 186),
              (60, 47, 41), (155, 205, 218), (49, 56, 94), (22, 90, 76), (129, 38, 59), (58, 44, 52), (33, 60, 53),
              (97, 146, 125), (173, 203, 189), (178, 188, 212)]

for i in range(10):
    tim.pu()
    tim.goto(-225, -200 + (i * 50))
    tim.pd()
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.pu()
        tim.forward(50)
        tim.pd()

screen.exitonclick()





