import requests


def consultar_cep(cep):

    cep = cep.replace("-", "").replace(".",
                                       "").strip()
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Por favor, digite um CEP com 8 dígitos numéricos.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados_endereco = response.json()

        if "erro" in dados_endereco:
            print(f"CEP {cep} não encontrado.")
            return None

        return dados_endereco

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")
        return None
    except ValueError:
        print("Erro ao processar a resposta da API.")
        return None


if __name__ == "__main__":
    cep_usuario = input("Digite o CEP (apenas números ou com traço): ")
    informacoes = consultar_cep(cep_usuario)

    if informacoes:
        print(f"""
        Informações do Endereço 
        CEP: {informacoes.get('cep', 'N/A')}
        Logradouro: {informacoes.get('logradouro', 'N/A')}
        Bairro: {informacoes.get('bairro', 'N/A')}
        Estado: {informacoes.get('uf', 'N/A')}
        Cidade: {informacoes.get('localidade', 'N/A')}
""")
