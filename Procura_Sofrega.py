# abre sempre o no com menor custo da lista

def encontrarMenorKM (cidadesParaExpandir):
    distancia = cidadesParaExpandir[0]['faro']
    cidade = cidadesParaExpandir[0]

    for candidato in cidadesParaExpandir:
        if (candidato['faro'] < distancia):
            distancia = candidato['faro']
            cidade = candidato

    return cidade

def procuraSofrega (mapa, inicio, destino):

    cidadesParaExpandir = []

    # adicionamos o ponto de partida
    cidadesParaExpandir.append (
        {'cidade': inicio.nomeCidade, 'historicoCaminho': [inicio.nomeCidade], 'faro' : inicio.distanciaParaFaro}
    )

    while True:

        # encontrar o proximo no a expandir
        proximoNoExpandir = encontrarMenorKM(cidadesParaExpandir)
        
        # verificar se e o destino
        if (proximoNoExpandir['cidade'] == destino.nomeCidade):
            print(proximoNoExpandir['historicoCaminho'])
            break

        # adicionar os vizinhos do no que foi expandido
        cidade = mapa.obterCidade(proximoNoExpandir['cidade'])
        for vizinho in cidade.vizinhos:
            cidadesParaExpandir.append({
                    'cidade': vizinho,
                    'historicoCaminho': proximoNoExpandir['historicoCaminho'] + [vizinho], 
                    'faro' : inicio.distanciaParaFaro
                }
            )

        # remover o no que foi totalmente expandido
        cidadesParaExpandir.remove(proximoNoExpandir)