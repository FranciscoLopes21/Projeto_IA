def encontrarMenorNo (cidadesParaExpandir):
    # VERIFICAR ESTE DISTANCIA AUXILIAR
    distancia = cidadesParaExpandir[0]['distancia'] + cidadesParaExpandir[0]['faro']
    cidade = cidadesParaExpandir[0]

    for candidato in cidadesParaExpandir:
        if ((candidato['distancia'] + candidato['faro'])  < distancia):
            distancia = candidato['distancia'] + candidato['faro']
            cidade = candidato

    return cidade

def aMais (mapa, inicio, destino):

    cidadesParaExpandir = []

    # adicionamos o ponto de partida
    cidadesParaExpandir.append (
       {'cidade': inicio.nomeCidade, 'historicoCaminho': [inicio.nomeCidade],'distancia': 0, 'faro' : inicio.distanciaParaFaro}
    )

    while True:

        # encontrar o proximo no a expandir
        proximoNoExpandir = encontrarMenorNo(cidadesParaExpandir)
        
        # verificar se e o destino
        if (proximoNoExpandir['cidade'] == destino.nomeCidade):
            print(proximoNoExpandir['historicoCaminho'])
            print(proximoNoExpandir['distancia'])
            break

        # adicionar os vizinhos do no que foi expandido
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