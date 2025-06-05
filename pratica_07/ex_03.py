import csv

nome_arquivo_csv = 'pessoas.csv'

try:
    with open(nome_arquivo_csv, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)

        cabecalho = next(leitor_csv, None)
        if cabecalho:
            print(f"Cabeçalho: {', '.join(cabecalho)}")
            print("-" * 30)

        print("Dados das Pessoas:")
        for i, linha in enumerate(leitor_csv):

            print(
                f"Registro {i+1}: Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}")


except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_csv}' não foi encontrado.")
    print("Verifique se o arquivo existe no mesmo diretório do script ou forneça o caminho correto.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
