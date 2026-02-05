
fra = str(input("Cite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(fra.count("A")))
print("A letra A aparece pela primeira vez na posição {}.".format(fra.find("A")+1))
print("A letra A aparece na frase pela ultima vez na posição {}.".format(fra.rfind("A")+1))