
print("PARDAL")
print("¨¨" * 3)
multa = 0
SpeedCar = float(input("Lendo velocidade do carro: "))
if SpeedCar >80:
    multa = 7.0 * (SpeedCar-80)
    print("Você ultrapassou a velocidade limite!")
    print("Você foi multado em R${} reais.".format(multa))

