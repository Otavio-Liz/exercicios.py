# Faça um programa que leia um ano qualquer e mostre se é BISSEXTO. 
from datetime import date
print("ANO BISSEXTO")
print("¨¨" * 6)
year = int(input("Qual o ano você quer saber se é bissexto?"))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"O ano {year} é Bissexto!")
else:    
    print(f"O ano {year} não é bissexto!")
