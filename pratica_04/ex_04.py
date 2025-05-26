def contar_pares_impares():

    pares = 0
    impares = 0

    print("Digite números inteiros. Para terminar, digite 'fim'.")

    while True:
        entrada = input("Digite um número ou 'fim': ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    print("\n--- Resumo ---")
    print(f"Quantidade de números pares inseridos: {pares}")
    print(f"Quantidade de números ímpares inseridos: {impares}")


if __name__ == "__main__":
    contar_pares_impares()
