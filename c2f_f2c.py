from Base_c2f_f2c import c2f,f2c

Tc = float(input('Enter Temp in Degrees: '))


Tf = c2f(Tc)

print('Tf = ' , Tf)


Tf = float(input('Enter Temp in Fahrenheit: '))

Tc = f2c(Tf)

print('Tf = ' + str(Tc))
