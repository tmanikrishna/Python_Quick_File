import numpy as np

degree_value = float(input('Enter a value in degrees: ')  )

def radian(degree_value):

    return degree_value * (np.pi/180)


c = radian(degree_value)

print(c)


radian_value = float(input('Enter a value in radian: '))

def degree(radian_value):

    return radian_value * (180/np. pi)

d = degree(radian_value)

print(d)