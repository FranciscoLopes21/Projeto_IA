# abre sempre o no com menor custo da lista

def encontrarMenorNo (cidadesParaExpandir):
    distancia = cidadesParaExpandir[0]['distancia']
    cidade = cidadesParaExpandir[0]

    for candidato in cidadesParaExpandir:
        if (candidato['distancia'] < distancia):
            distancia = candidato['distancia']
            cidade = candidato

    return cidade

def custoUniforme (mapa, inicio, destino):

    cidadesParaExpandir = []

    # adicionamos o ponto de partida
    cidadesParaExpandir.append (
        {'cidade': inicio.nomeCidade, 'distancia': 0, 'historicoCaminho': [inicio.nomeCidade]}
    )

    while True:

        # encontrar o proximo no a expandir
        proximoNoExpandir = encontrarMenorNo(cidadesParaExpandir)
        
        # verificar se e o destino
        if (proximoNoExpandir['cidade'] == destino.nomeCidade):
            print(proximoNoExpandir['historicoCaminho'])
            break

        # adicionar os vizinhos do no que foi expandido
        cidade = mapa.obterCidade(proximoNoExpandir['cidade'])
        for vizinho in cidade.vizinhos:
            cidadesParaExpandir.append({
                    'cidade': vizinho,
                    'distancia': cidade.vizinhos[vizinho]['distancia'] + proximoNoExpandir['distancia'],
                    'historicoCaminho': proximoNoExpandir['historicoCaminho'] + [vizinho]
                }
            )

        # remover o no que foi totalmente expandido
        cidadesParaExpandir.remove(proximoNoExpandir)