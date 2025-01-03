import numpy as np


x = int(input('What Values you want, type 1 for degrees and 2 for the radian - '))


if x == 2:

    degree_value = float(input('Enter a value in degrees: ')  )

    def radian(degree_value):

        return degree_value * (np.pi/180)


c = radian(degree_value)
print(c)


elif x == 1:

    radian_value = float(input('Enter a value in radian: '))
    
    def degree(radian_value):

        return radian_value * (180/np. pi)

d = degree(radian_value)
print(d)

else:

    print('Error ')