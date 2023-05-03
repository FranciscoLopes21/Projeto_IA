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
    caminho = []
    distancia = 0

    # adicionamos o ponto de partida
    cidadesParaExpandir.append (
        {'cidade': inicio.nomeCidade, 'faro' : inicio.distanciaParaFaro}
    )

    while True:

        # encontrar o proximo no a expandir
        proximoNoExpandir = encontrarMenorKM(cidadesParaExpandir)
        
        # verificar se e o destino
        if (proximoNoExpandir['cidade'] == destino.nomeCidade):
            caminho.append(destino.nomeCidade)
            print(caminho)
            break

        # remover o no que foi totalmente expandido
        cidadesParaExpandir.clear()

        caminho.append(proximoNoExpandir['cidade'])

        # adicionar os vizinhos do no que foi expandido
        cidade = mapa.obterCidade(proximoNoExpandir['cidade'])
        for vizinho in cidade.vizinhos:
            cidadesParaExpandir.append({
                    'cidade': vizinho,
                    'faro' : cidade.vizinhos[vizinho]['cidade'].distanciaParaFaro
                }
            )

        