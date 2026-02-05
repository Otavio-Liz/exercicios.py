"""
Faça um programa que leia um número de 0 a 9999 
e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834

unidade: 4
dezena: 3 
centena: 8
milhar: 1

"""
# 1º Forma(String)
num = input("Digite um número de 0 a 9999: ")
num.split()
print(f"Unidade: {num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}")

# 2º Forma(Convertendo variável para String)
num = int(input("Digite um número de 0 a 9999: "))
n = str(num)
print("Analizando o número {}".format(n))
print("Unidade {}".format(n[3]))
print("Dezena {}".format(n[2]))
print("Centena {}".format(n[1]))
print("Milhar {}".format(n[0]))    

"""
Essas duas maneiras estão corretas, porém, só funcionará se informarmos todos os índices. 
Se quisérmos saber apenas a unidade e centena, o python mostrará um erro
Pedindo que informemos os outros índices.

"""

# 3º Forma(Matemáticamente)
num = int(input("Digite um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analizando o número {}".format(n))
print("Unidade {}".format([u]))
print("Dezena {}".format([d]))
print("Centena {}".format([c]))
print("Milhar {}".format([m]))    