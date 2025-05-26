def registrar_notas_turma():

    notas = []
    soma_das_notas = 0
    quantidade_de_notas = 0

    print("Digite as notas dos alunos (entre 0 e 10).")
    print("Digite 'fim' para concluir e calcular a média.")

    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para terminar): ")

        if entrada.lower() == 'fim':
            if quantidade_de_notas == 0:
                print("Nenhuma nota válida foi inserida. Média não pode ser calculada.")
            else:
                media = soma_das_notas / quantidade_de_notas
                print(f"\n--- Resultados ---")
                print(f"Notas registradas: {notas}")
                print(f"Quantidade de notas válidas: {quantidade_de_notas}")
                print(f"Soma das notas válidas: {soma_das_notas:.2f}")
                print(f"Média da turma: {media:.2f}")
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
                soma_das_notas += nota
                quantidade_de_notas += 1
                print(f"Nota {nota:.1f} registrada com sucesso.")
            else:
                print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")


if __name__ == "__main__":
    registrar_notas_turma()
