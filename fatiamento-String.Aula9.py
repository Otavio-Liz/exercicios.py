#Fatiamento de string
print("FATIAMENTO:")
frase = "  Curso em Vídeo   "

print(frase[9])

print(frase[9:10])

print(frase[9:10:2])

print(frase[9::2])

print(frase[:9])

print(frase[9:])
print()
print("ANÁLISE:")
#Análise

print(len(frase))

print(frase.count("o"))

print(frase.count("u", 0, 12))

print(frase.find("em"))
print()
print("TRANSFORMAÇÃO:")
#Transformação
print(frase.replace("Curso", "Aula"))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

print(frase.strip())

print(frase.rstrip())

print(frase.lstrip())

print("Curso" in frase)
print()
print("DIVISÃO:")
#Divisão 
print(frase.split())
print()
print("JUNÇÃO:")
#Junção
print(" ".join(frase))