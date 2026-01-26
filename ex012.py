preco = float(input('Qual é o preço do produto? R$ '))
desconto = preco * 0.05
preco_final = preco - desconto
print(f'O preço com desconto é R$ {preco_final:.2f}.')