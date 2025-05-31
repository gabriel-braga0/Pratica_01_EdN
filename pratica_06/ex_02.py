import requests


def gerar_perfil():

    url_api = "https://randomuser.me/api/?inc=name,email,location"

    resposta = requests.get(url_api)

    dados_usuario = resposta.json()

    usuario = dados_usuario["results"][0]

    nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print(f"""
    Perfil de Usuário Aleatório
    Nome: {nome_completo}
    Email: {email}
    País: {pais}
    -------------------------------------------\n""")


if __name__ == "__main__":
    gerar_perfil()
