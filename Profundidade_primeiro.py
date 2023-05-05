def profundidadePrimeiro(mapa, inicio, destino):
    cidadesParaExpandir = []

    # adicionamos o ponto de partida a pilha
    cidadesParaExpandir.append (
        {'cidade': inicio.nomeCidade, 'distancia': 0, 'historicoCaminho': [inicio.nomeCidade]}
    )

    numeroIteracoes = 0

    while numeroIteracoes <= 500:

        if (len(cidadesParaExpandir) == 0):
            print("Nao foi possivel encontrar o caminho")
            return

        proximoNoExpandir = cidadesParaExpandir.pop(0)

        # verificar se o no destino
        if (proximoNoExpandir['cidade'] == destino.nomeCidade):
            print(proximoNoExpandir['historicoCaminho'])
            print(proximoNoExpandir['distancia'])
            return

        cidade = mapa.obterCidade(proximoNoExpandir['cidade'])
        for vizinho in cidade.vizinhos:
            # caso nao seja adicionamos os novos vizinhos a lista
            cidadesParaExpandir.insert(0,{
                'cidade': vizinho,
                'distancia': cidade.vizinhos[vizinho]['distancia'] + proximoNoExpandir['distancia'],
                'historicoCaminho': proximoNoExpandir['historicoCaminho'] + [vizinho]
            })
        numeroIteracoes += 1
        
    
    print("Limite de iteracoes atingido")