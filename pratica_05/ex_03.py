def calcular_idade_em_dias(ano_nascimento):

    ano_atual = 2025
    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365
    return idade_em_dias


print(
    f"Uma pessoa que nasceu em 2003 tem aproximadamente {calcular_idade_em_dias(2003)} dias de vida.")
