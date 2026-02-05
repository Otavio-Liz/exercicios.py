


from random import randint
print("--+--" * 10)
print("Vou pensar em um número entre 0-5. Tente advinhar...")
print("--+--" * 10)
comp = randint(0, 5)
jogador = (int(input("Que número eu pensei?")))
if jogador == comp:
    print("Parabéns, você venceu!\nVocê escolheu o número {} e eu o número {}.".format(jogador, comp) )
else:
    print("Perdeu! Eu escolhi o número {}!".format(comp))
