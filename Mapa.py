from Cidade import Cidade

class Mapa:
    
    def __init__ (self, nomeMapa, listaCidades):
        self.listaCidades = listaCidades
        
    def obterCidade (self, nomeCidade):
        for cidadeDaLista in self.listaCidades:
            if cidadeDaLista.nomeCidade == nomeCidade:
                return cidadeDaLista
        
        return None
                
    def mostrarCidades (self):
        for cidadeDaLista in self.listaCidades:
            print(cidadeDaLista.nomeCidade)
    