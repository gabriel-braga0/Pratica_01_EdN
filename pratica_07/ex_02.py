import csv

nome_arquivo_csv = 'pessoas.csv'

cabecalho = ['Nome', 'Idade', 'Cidade']


dados_pessoas = [
    ['Ana Silva', 30, 'São Paulo'],
    ['Bruno Costa', 25, 'Rio de Janeiro'],
    ['Carlos Dias', 45, 'Belo Horizonte'],
    ['Daniela Souza', 22, 'Salvador'],
    ['Gabriel', 22, 'Petrópolis']
]

try:
    with open(nome_arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        escritor_csv.writerow(cabecalho)

        escritor_csv.writerows(dados_pessoas)

    print(f"Arquivo '{nome_arquivo_csv}' criado e dados escritos com sucesso!")
    print(
        f"O arquivo contém {len(dados_pessoas)} registros de pessoas (além do cabeçalho).")

except IOError:
    print(
        f"Erro: Não foi possível escrever no arquivo '{nome_arquivo_csv}'. Verifique as permissões.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
