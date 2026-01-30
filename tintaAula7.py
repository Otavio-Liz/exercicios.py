tinta = float(input('Quantos metros serão pintados? '))
litros = tinta / 6
preco = litros * 25.00
print(f'Serão necessários {litros:.2f} litros de tinta.')
print(f'O preço total da tinta será R$ {preco:.2f}.')