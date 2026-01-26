km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco_km = km * 0.15    
preco_dias = dias * 60
preco_total = preco_km + preco_dias
print(f'O preço total do aluguel do carro é R$ {preco_total:.2f}.')