class Cidade:
    
    def __init__ (self, nomeCidade, distanciaParaFaro):
        self.nomeCidade = nomeCidade
        self.vizinhos = {}
        self.distanciaParaFaro = distanciaParaFaro
        
    def adicionarVizinho (self, Cidade, distancia):
        if Cidade.nomeCidade not in self.vizinhos.keys():
            Cidade.ligarSegundoSentido (self, distancia)
            self.vizinhos[Cidade.nomeCidade] = { 'cidade': Cidade, "distancia": distancia }
    
    def ligarSegundoSentido (self, Cidade, distancia):
        self.vizinhos[Cidade.nomeCidade] = { 'cidade': Cidade, "distancia": distancia }
        
    def mostrarVizinhos(self):
        print(self.vizinhos)