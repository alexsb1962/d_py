from dataclasses import *
import math
import turtle


class OneAllTime:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is not None:
            return cls.__instance
        else:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            return  cls.__instance


class Cl:
    a = 1
    b = 2
    c = 3

    def mtd(self, arg):
        self.a = arg

var = Cl()
var1 = Cl()
var.a = 'new'
var
var1

wndow = turtle.Screen()
wndow.title("Screen & Button")
wndow.setup(500, 500)

btn1 = turtle.Turtle()
btn1.hideturtle()
for i in range(2):
    btn1.fd(80)
    btn1.left(90)
    btn1.fd(30)
    btn1.left(90)
btn1.penup()
btn1.goto(11,7)
btn1.write("Push me", font=("Arial", 12, "normal"))

def btnclick(x, y):
    if 0<x<80 and 0<y<30:
        print("Кнопка нажата!")
        btn1.clear()
        ball = turtle.Turtle()
        turtle.fillcolor("orange")
        turtle.pencolor("purple")
        turtle.shape("circle")

turtle.listen()
turtle.onscreenclick(btnclick, 1)
turtle.done()



@dataclass
class SomeData:
    v1: int = 5
    v2: float = math.pi


s = SomeData()
s.v1 = 1
print(dir(s))

if s.v1 == 2:
    pass

match s.v1:
    case 1:
        pass
    case _:
        pass

angle = math.atan2(165, 285) * 180 / math.pi
print(f'{angle}=')


def go_main():
    pass


if __name__ == '__main__':
    go_main()
