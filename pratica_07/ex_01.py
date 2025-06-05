import pandas as pd

# Nome do arquivo CSV
nome_arquivo = 'logs_treinamento.csv'

try:
    df = pd.read_csv(nome_arquivo)

    if 'tempo_execucao' in df.columns:
        media_tempo_execucao = df['tempo_execucao'].mean()

        desvio_padrao_tempo_execucao = df['tempo_execucao'].std()

        print(f"Análise do Tempo de Execução do arquivo: {nome_arquivo}")
        print(
            f"Média do Tempo de Execução: {media_tempo_execucao:.2f} segundos")
        print(
            f"Desvio Padrão do Tempo de Execução: {desvio_padrao_tempo_execucao:.2f} segundos")
    else:
        print(
            f"Erro: A coluna 'Tempo_Execucao_seg' não foi encontrada no arquivo {nome_arquivo}.")
        print("Por favor, verifique o nome da coluna no seu arquivo CSV. As colunas encontradas são:")
        print(df.columns.tolist())

except FileNotFoundError:
    print(
        f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
