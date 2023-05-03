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
        {'cidade': inicio.nomeCidade, 'historicoCaminho': [inicio.nomeCidade],'distancia': 0, 'faro' : inicio.distanciaParaFaro}
    )

    try:
        i = 0
        while True and i <= 75:
            
            i += 1

            # encontrar o proximo no a expandir
            proximoNoExpandir = encontrarMenorKM(cidadesParaExpandir)
            
            # verificar se e o destino
            if (proximoNoExpandir['cidade'] == destino.nomeCidade):
                print(proximoNoExpandir['historicoCaminho'])
                print(proximoNoExpandir['distancia'], "kms")
                break

            # adicionar os vizinhos do no que foi expandido
            # distancia entre as cidades
            cidade = mapa.obterCidade(proximoNoExpandir['cidade'])
            for vizinho in cidade.vizinhos:
                cidadesParaExpandir.append({
                        'cidade': vizinho,
                        'historicoCaminho': proximoNoExpandir['historicoCaminho'] + [vizinho],
                        'distancia': cidade.vizinhos[vizinho]['distancia'] + proximoNoExpandir['distancia'],
                        'faro' : cidade.vizinhos[vizinho]['cidade'].distanciaParaFaro
                    }
                )

            # remover o no que foi totalmente expandido
            cidadesParaExpandir.remove(proximoNoExpandir)

    except:
        print("Ocorreu um erro ao encontrar caminho.")