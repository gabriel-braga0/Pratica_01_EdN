import requests
from datetime import datetime


def consultar_cotacao(codigo_moeda):

    codigo_moeda = codigo_moeda.upper().strip()
    if not codigo_moeda:
        print("Código da moeda não pode ser vazio.")
        return None

    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        chave_cotacao = f"{codigo_moeda}BRL"
        if chave_cotacao in dados:
            cotacao_info = dados[chave_cotacao]
            return cotacao_info
        else:
            print(
                f"Cotação para {codigo_moeda}-BRL não encontrada na resposta da API.")
            print("Verifique se o código da moeda está correto e é suportado pela API.")

            return None

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(
                f"Erro: Cotação para a moeda {codigo_moeda} não encontrada (404). Verifique o código da moeda.")
        else:
            print(f"Erro HTTP ao consultar a cotação: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao consultar a cotação: {e}")
        return None
    except ValueError:
        print("Erro ao processar a resposta da API. O serviço pode estar indisponível ou a resposta é inválida.")
        return None


if __name__ == "__main__":
    codigo_moeda_usuario = input(
        "Digite o código da moeda desejada (ex: USD, EUR, GBP): ")

    informacoes_cotacao = consultar_cotacao(codigo_moeda_usuario)

    if informacoes_cotacao:
        timestamp_atualizacao = int(informacoes_cotacao.get('timestamp', 0))
        data_hora_atualizacao = datetime.fromtimestamp(timestamp_atualizacao).strftime('%d/%m/%Y %H:%M:%S') \
            if timestamp_atualizacao else "N/A"

        print(f"""
        Cotação {informacoes_cotacao.get('code', 'N/A')}/{informacoes_cotacao.get('codein', 'N/A')}
        Moeda: {informacoes_cotacao.get('name', 'N/A')}
        Valor Atual (Compra): R$ {informacoes_cotacao.get('bid', 'N/A')}
        Máxima do Dia: R$ {informacoes_cotacao.get('high', 'N/A')}
        Mínima do Dia: R$ {informacoes_cotacao.get('low', 'N/A')}
        Variação: {informacoes_cotacao.get('varBid', 'N/A')}
        Porcentagem de Variação: {informacoes_cotacao.get('pctChange', 'N/A')}%
        Última Atualização: {data_hora_atualizacao}
        """)
