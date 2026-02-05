# Desenvolva um programa que pergunte a distância de uma Viagem em Km(FLOAT). 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# E R$0,45 para viagens mais longas

print("PREÇO DAS PASSAGENS")
print("¨¨" * 10)
km = float(input("Qual a distância da sua viagem em Km: "))
print("Você está prestes a começar sua viagem de {}Km.".format(km))
if km <= 200:
    print("E o preço da passagem será: {:.2f}.".format(0.50 * km))
elif km > 200:
    print("E o preço da passagem será: {:.2f}.".format(0.40 * km))