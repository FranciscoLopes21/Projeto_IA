from Cidade import Cidade
from Mapa import Mapa

def iniciarBasePortugal():
        
        
    # criar as cidades de Portugal
        
    Aveiro = Cidade('Aveiro', 366)
    Braga = Cidade('Braga', 454)
    Braganca = Cidade('Braganca', 487)
    Beja = Cidade('Beja', 99)
    CasteloBranco = Cidade('Castelo Branco', 280)
    Coimbra = Cidade('Coimbra', 319)
    Evora = Cidade('Evora', 157)
    Faro = Cidade('Faro', 0)
    Guarda = Cidade('Guarda', 352)
    Leiria = Cidade('Leiria', 278)
    Lisboa = Cidade('Lisboa', 195)
    Porto = Cidade('Porto', 418)
    VilaReal = Cidade('Vila Real', 429)
    Viseu = Cidade('Viseu', 363)
    VianaDoCastelo = Cidade('Viana Do Castelo', 473)
    Santarem = Cidade('Santarem', 231)
    Setubal = Cidade('Setubal', 168)
    Portalegre = Cidade('Portalegre', 228)
    
    # criar o mapa de Portugal
    
    listaCidades = [Aveiro, Braga, Braganca, Beja, CasteloBranco, Coimbra, Evora, Faro, Guarda, Leiria, Lisboa, Porto, VilaReal, Viseu, VianaDoCastelo, Santarem, Setubal, Portalegre]
    
    Portugal = Mapa ('Portugal', listaCidades)
    
    # vizinhos de Aveiro
    Aveiro.adicionarVizinho(Porto, 68)
    Aveiro.adicionarVizinho(Viseu, 95)
    Aveiro.adicionarVizinho(Coimbra, 68)
    Aveiro.adicionarVizinho(Leiria, 115)
    
    # vizinhos de Braga
    Braga.adicionarVizinho(VianaDoCastelo, 48)
    Braga.adicionarVizinho(VilaReal, 106)
    Braga.adicionarVizinho(Porto, 53)
    
    # vizinho de Braganca 
    Braganca.adicionarVizinho(VilaReal, 137)
    Braganca.adicionarVizinho(Guarda, 202)
    
    # vizinhos de Beja
    Beja.adicionarVizinho(Evora, 78)
    Beja.adicionarVizinho(Faro, 152)
    Beja.adicionarVizinho(Setubal, 142)
    
    # vizinhos de Castelo Branco
    CasteloBranco.adicionarVizinho(Coimbra, 159)
    CasteloBranco.adicionarVizinho(Guarda, 106)
    CasteloBranco.adicionarVizinho(Portalegre, 80)
    CasteloBranco.adicionarVizinho(Evora, 203)
    
    # vizinhos de Coimbra
    Coimbra.adicionarVizinho(Viseu, 96)
    Coimbra.adicionarVizinho(Leiria, 67)
    
    # vizinhos de Evora
    Evora.adicionarVizinho(Lisboa, 150)
    Evora.adicionarVizinho(Santarem, 117)
    Evora.adicionarVizinho(Portalegre, 131)
    Evora.adicionarVizinho(Setubal, 103)
    
    # vizinhos de Faro
    Faro.adicionarVizinho(Setubal, 249)
    Faro.adicionarVizinho(Lisboa, 299)
    
    # vizinhos de Guarda
    Guarda.adicionarVizinho(VilaReal, 157)
    Guarda.adicionarVizinho(Viseu, 85)
    
    # vizinhos de Leiria
    Leiria.adicionarVizinho(Lisboa, 129)
    Leiria.adicionarVizinho(Santarem, 70)
    
    # vizinhos de Lisboa
    Lisboa.adicionarVizinho(Santarem, 78)
    Lisboa.adicionarVizinho(Setubal, 50)
    
    # viznhos de Porto
    Porto.adicionarVizinho(VianaDoCastelo, 71)
    Porto.adicionarVizinho(VilaReal, 116)
    Porto.adicionarVizinho(Viseu, 133)
    
    #vizinhos de VilaReal
    VilaReal.adicionarVizinho(Viseu, 110)
    
    return Portugal