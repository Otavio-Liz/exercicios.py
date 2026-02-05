# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salário inferiores o aumento é de 15%.
print("AUMENTO SALARIAL")
print("¨¨" * 10)
funcionario = str(input("Digite seu nome: "))
salario = float(input("Qual o valor do seu salário? "))
if salario > 1.250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f"{funcionario}, o seu aumento salarial é de R${aumento} REAIS.")
print(f"Você recebia R${salario} REAIS. Com o aumento, passará a receber R${salario + aumento} REAIS.")