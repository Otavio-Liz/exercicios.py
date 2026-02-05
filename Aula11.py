print("\033[31mOlá Mundo!")
print("\033[31;43mOlá Mundo!")
print("\033[31;1;43mOlá Mundo!\33[m")
print("\033[4;30;45mOlá Mundo!\33[m")
print("\033[7;30mOlá Mundo!\33[m")
print("\033[7;33;44mOlá Mundo!\33[m")
a = 10 
b = 47
print("Os valores são \033[33m{}\033[m e \033[31m{}\033[m...".format(a, b))
nome = "Otávio"
print("Muito prazer em te conhecer, {}{}{}.".format("\033[4;34m", nome, "\033[m"))
cores = {"limpa": "\033[m", 
         "amarelo": "\033[4;33m", 
         "vermelho": "\033[4;32m]", 
         "pretoebranco": "\033[7;30m"}
nome = "Rita de Cássia"
print("Seja muito bem vinda, {}{}{}.".format(cores["amarelo"], nome, cores["limpa"]))