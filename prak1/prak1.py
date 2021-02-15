import math

def f1(x, y, z):
    return ((y**4)/(11)+z**5+66)/(y**7 + math.e**x)+y**7+34*z**4-((math.log(x)-22*y**5)/(z**8-59*y**5))

print(f1(1,31,-15))
print(f1(87,35,-41))

def f2(x):
    if(x<111):
        return 22*x**6 + x**5
    elif(11<=x<149):
        return (x**8 - abs(x))**5 - 41*x**2
    else:
        return x**2-67*x**5 + 45

print(f2(130))
print(f2(215))