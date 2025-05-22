produto = {"nome":'Teclado',
           "preco_unitario":250.00,
           "quantidade":5}

print(f'''
Nome do produto: {produto["nome"]}
Preço unitário: {produto["preco_unitario"]}
Quantidade: {produto["quantidade"]}
Preço total: R${produto["preco_unitario"] * produto["quantidade"]}
      ''')