import json

nome_arquivo_json = 'pessoa.json'


dados_pessoa_para_escrever = {
    "nome": "Gabriel",
    "idade": 22,
    "cidade": "Petrópolis"
}

try:
    with open(nome_arquivo_json, mode='w', encoding='utf-8') as arquivo_json_escrita:
        json.dump(dados_pessoa_para_escrever, arquivo_json_escrita,
                  indent=4, ensure_ascii=False)

    print(f"Dados escritos com sucesso no arquivo '{nome_arquivo_json}'!")
    print(f"Conteúdo escrito: {dados_pessoa_para_escrever}\n")

except IOError:
    print(
        f"Erro: Não foi possível escrever no arquivo '{nome_arquivo_json}'. Verifique as permissões.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao escrever o JSON: {e}\n")


try:
    with open(nome_arquivo_json, mode='r', encoding='utf-8') as arquivo_json_leitura:
        dados_pessoa_lidos = json.load(arquivo_json_leitura)

    print("Dados lidos com sucesso do arquivo JSON:")
    print(f"  Nome: {dados_pessoa_lidos.get('nome')}")
    print(f"  Idade: {dados_pessoa_lidos.get('idade')}")
    print(f"  Cidade: {dados_pessoa_lidos.get('cidade')}")


except FileNotFoundError:
    print(
        f"Erro: O arquivo '{nome_arquivo_json}' não foi encontrado para leitura.")
    print("Certifique-se de que o arquivo foi criado na etapa de escrita ou já existe.")
except json.JSONDecodeError:
    print(
        f"Erro: O arquivo '{nome_arquivo_json}' não contém um JSON válido ou está corrompido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao ler o JSON: {e}")
