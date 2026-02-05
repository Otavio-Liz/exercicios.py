nome = str(input("Digite seu nome: "))
if nome == "Otávio":
    print("Que nome lindo você tem!")
else: 
    print("Que nome normal!")
print("Bom dia {}!".format(nome))

nome = str(input("Digite seu nome: "))
proj = int(input("Quantos projetos realizados você tem? "))
print("Olá {}!\n".format(nome),"Nossa Parabens!" if proj >= 10 else "Vamos realizar mais projetos?")