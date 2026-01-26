import math
c_o = float(input('Valor do cateto oposto: '))
c_a = float(input('Valor do cateto adsjacente:'))
soma_catetos = (c_o**2) + (c_a**2)
print('Valor da hipotenusa do triângulo retângulo é igual a {:.2}.'.format(math.sqrt(soma_catetos))) 
