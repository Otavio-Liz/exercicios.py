# Faça um programa que leia três números e mostre qual é o maior e menor
import math
print("MAIOR E MENOR VALOR")
print("¨¨" * 10)
n1 = input("Digite o primeiro valor: ")
n2 = input("Digite o segundo valor: ")
n3 = input("Digite o terceiro valor: ")
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print("O valor {} é o maior entre os 3.".format(maior))
print("O valor {} é o menor entre os 3.".format(menor))

n4 = input("Digite o primeiro valor: ")
n5 = input("Digite o segundo valor: ")
n6 = input("Digite o terceiro valor: ")
ma = n4
if n5 > n4 and n5 > n6:
    ma = n5
if n6 > n4 and n6 > n5:
    ma = n6
me = n4
if n5 < n4 and n5 < n6:
    ma = n5
if n6 < n4 and n6 < n5:
    ma = n6
print("O valor {} é o maior entre os 3.".format(ma))
print("O valor {} é o menor entre os 3.".format(me))
