
# 1º Forma
cid = str(input("Digite o nome de sua cidade natal: "))
nomcidade = "Santos" in cid
print(nomcidade)

# 2º Forma 
cida =  str(input("Digite o nome da cidade: ")).strip() #Strip elimina os espaços iniciais se existirem na string.
print(cida[0:].upper() == "SANTOS")
