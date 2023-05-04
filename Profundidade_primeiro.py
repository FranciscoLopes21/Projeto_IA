import Mapa as mapa

def profundidadePrimeiro(mapa, inicio, destino,visitado=None,caminho=None):
    if visitado is None:
        visitado = set()
    if caminho is None:
        caminho= []
    visitado.add(inicio)
    caminho=caminho + [inicio]
    if inicio == destino:
        return caminho
    print('caminho:',caminho)
    for vizinho in mapa[inicio]:
        if vizinho not in visitado:
            novo_caminho = profundidadePrimeiro(mapa,vizinho,destino,visitado,caminho)
            if novo_caminho:
                return novo_caminho
    return []

 #teste
inicio = 'Porto'
destino = 'Castelo Branco'
caminho = profundidadePrimeiro(mapa, inicio, destino)
print('Caminho encontrado:', caminho)
             

