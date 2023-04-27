from Cidade import Cidade
from Mapa import Mapa
from basePortugal import *
import os
# limpar ecra
Portugal = iniciarBasePortugal()

def validarEscolha(escolha):
    
    print("Inserir cidade inicio")
    cidadeInicio = input()
    
    if (escolha == "1" or escolha == "2"):
        print("Inserir cidade final")
        cidadeFinal = input()
    else:
        cidadeFinal = "Faro"
        
    if (cidadeInicio == cidadeFinal):
        print ("A cidade de inicio nao pode ser igual a final")
    else:
        cidade1 = Portugal.obterCidade(cidadeInicio)
        cidade2 = Portugal.obterCidade(cidadeFinal)
    
        if (cidade1 == None):
            print ("Cidade inicio nao e valida")
        elif (cidade2 == None):
            print ("Cidade final nao e valida")
        else:
            if (escolha == "1"):
                print ("chamar algoritmo ppp - procura(cidade1, cidade2)")
            elif (escolha == "2"):
                print ("chamar algoritmo custo uniforme")
            elif (escolha == "3"):
                print ("chamar algoritmo procura sofrega")
            elif (escolha == "4"):
                print ("chamar algoritmo a*")
            else:
                print ("Escolha um algoritmo existente")
    
    

while True:
    os.system('cls||clear')
    print("Escolha um dos metodos:")
    print("1 - Procura em profundidade primeiro")
    print("2 - Custo uniforme")
    print("3 - Procura sôfrega (destino Faro)")
    print("4 - A* (destino Faro)")
    
    escolha = input()
    
    validarEscolha(escolha)
    

