from Cidade import Cidade
from Mapa import Mapa
from basePortugal import *
import os

from Profundidade_primeiro import *
from Custo_Uniforme import *
from Procura_Sofrega import *
from Amais import *

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
                profundidadePrimeiro(Portugal, cidade1, cidade2)
            elif (escolha == "2"):
                custoUniforme(Portugal, cidade1, cidade2)
            elif (escolha == "3"):
                procuraSofrega(Portugal, cidade1, cidade2)
            elif (escolha == "4"):
                aMais(Portugal, cidade1, cidade2)
            else:
                print ("Escolha um algoritmo existente")

    input()

while True:
    os.system('cls||clear')
    print("Escolha um dos metodos:")
    print("1 - Procura em profundidade primeiro")
    print("2 - Custo uniforme")
    print("3 - Procura sôfrega (destino Faro)")
    print("4 - A* (destino Faro)")
    
    escolha = input()
    
    validarEscolha(escolha)
    
    # acresentar opcao de sair
