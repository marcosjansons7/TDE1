def realizar_uniao(conjunto1, conjunto2):
    return conjunto1.union(conjunto2), "União"


def realizar_intersecao(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2), "Interseção"


def realizar_diferenca(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2), "Diferença"


def realizar_produto_cartesiano(conjunto1, conjunto2):
    return {(x, y) for x in conjunto1 for y in conjunto2}, "Produto Cartesiano"


def processar_operacoes(nome_arquivo):
    operacoes = {
        'U': realizar_uniao,
        'I': realizar_intersecao,
        'D': realizar_diferenca,
        'C': realizar_produto_cartesiano
    }

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    num_operacoes = int(linhas[0].strip())
    indice = 1
    resultados = []

    for _ in range(num_operacoes):
        codigo_operacao = linhas[indice].strip()
        conjunto1 = set(map(str.strip, linhas[indice + 1].strip().split(',')))
        conjunto2 = set(map(str.strip, linhas[indice + 2].strip().split(',')))

        if codigo_operacao in operacoes:
            resultado, nome_operacao = operacoes[codigo_operacao](conjunto1,
                                                                  conjunto2)
        else:
            print(f"Operação '{codigo_operacao}' não reconhecida. Pulando...")
            indice += 3
            continue

        if codigo_operacao != 'C':
            resultado_str = ', '.join(sorted(resultado))
            resultados.append(
                f"{nome_operacao}: conjunto 1 {{{', '.join(sorted(conjunto1))}}}, conjunto 2 {{{', '.join(sorted(conjunto2))}}}. Resultado: {{{resultado_str}}}."
            )
        else:
            resultado_str = ', '.join(
                [f"({x}, {y})" for x, y in sorted(resultado)])
            resultados.append(
                f"{nome_operacao}: conjunto 1 {{{', '.join(sorted(conjunto1))}}}, conjunto 2 {{{', '.join(sorted(conjunto2))}}}. Resultado: {{{resultado_str}}}."
            )

        indice += 3

    return resultados


def main():
    nome_arquivo = 'input.txt'
    resultados = processar_operacoes(nome_arquivo)

    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    main()

#EXEMPLOS ENTRADA DE ARQUIVOS DE TEXTO(input.txt)

#EXEMPLO 1:
#3
#U
#1, 2, 3
#3, 4, 5
#I
#3, 20, 30
#20, 40, 50
#D
#100, 200, 300
#200, 400, 500

#EXEMPLO 2:
#4
#U
#5, 10, 15
#20, 25, 30
#I
#7, 14, 21
#14, 28, 35
#D
#9, 8, 7
#7, 6, 5
#C
#1, 2
#3, 4

#EXEMPLO 3:
#2
#U
#100, 200
#300, 400
#C
#50, 60
#70, 80


