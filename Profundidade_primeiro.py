def profundidadePrimeiro(mapa, inicio, destino):
    cidadesParaExpandir = []
    cidadesJaVisitadas = []

    # adicionamos o ponto de partida a pilha
    cidadesParaExpandir.append (
        {'cidade': inicio.nomeCidade, 'distancia': 0, 'historicoCaminho': [inicio.nomeCidade]}
    )

    numeroIteracoes = 0 

    while numeroIteracoes <= 150:

        if (len(cidadesParaExpandir) == 0):
            print("Nao foi possivel encontrar o caminho")
            return

        proximoNoExpandir = cidadesParaExpandir.pop(0)
        
        # adicionamos a cidade ja visitada numa lista, de modo a evitar futuros loops
        cidadesJaVisitadas.append(proximoNoExpandir['cidade'])

        cidade = mapa.obterCidade(proximoNoExpandir['cidade'])
        for vizinho in cidade.vizinhos:
            # verificar se o no destino
            if (vizinho == destino.nomeCidade):
                print(proximoNoExpandir['historicoCaminho'] + [vizinho])
                print(proximoNoExpandir['distancia'] + cidade.vizinhos[vizinho]['distancia'])
                print(numeroIteracoes)
                return
        
            # caso nao seja adicionamos os novos vizinhos a lista
            if vizinho not in cidadesJaVisitadas:
                cidadesParaExpandir.append({
                    'cidade': vizinho,
                    'distancia': cidade.vizinhos[vizinho]['distancia'] + proximoNoExpandir['distancia'],
                    'historicoCaminho': proximoNoExpandir['historicoCaminho'] + [vizinho]
                })
        
        numeroIteracoes += 1
        
    
    print("crashhhhhh")