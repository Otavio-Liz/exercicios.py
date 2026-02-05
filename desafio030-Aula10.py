# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
print("=*=" * 5)
print("IMPAR OU PAR")
print("=*=" * 5)
num = int(input("Digite um númuero inteiro: "))
if num % 2 == 0:
    print(f"O número {num} é PAR!")
else:
    print(f"O número {num} é IMPAR!")