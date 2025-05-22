produto = {'nome': 'camiseta',
           'preco_original': 50}

desconto = 0.20

print(
    f"O preço final da {produto['nome']} é R$ {produto['preco_original'] * (1 - desconto):.2f}, o desconto foi de R$ {produto['preco_original'] * desconto:.2f}")
