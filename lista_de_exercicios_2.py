#(1) Carregamento das Bibliotecas
import numpy as np

import scipy as sp


#(2) Entrada de Dados
marcaA = [154, 173, 134, 157, 149, 171, 162]
marcaB = [172, 163, 151, 146, 146]

#(3) Processamento dos Dados
media = np.mean(marcaA)
media2 = np.mean(marcaB)

#Variancia
variancia = np.var(marcaA)
variancia2 = np.var(marcaB)

#Desvio-padrao
desviopadrao = np.sqrt(variancia)
desviopadrao2 = np.sqrt(variancia2)



# Arredondamento
media = np.round(media,decimals=2)
media2 = np.round(media2,decimals=2)
desviopadrao = np.round(desviopadrao,decimals=2)
desviopadrao2 = np.round(desviopadrao2,decimals=2)
variancia = np.round(variancia,decimals=2)
variancia2 = np.round(variancia2,decimals=2)



#4 Apresentação e Vizualizão dos Resultados
print("A média da marca A é: ", media)
print("A média da marca B é: ", media2)

print("A variância da marca A é: ", variancia)
print("A variância da marca B é: ", variancia2)

print("O desvio-padrao da marca A é:", desviopadrao)
print("O desvio-padrao da marca B é:", desviopadrao2)


print("PERGUNTA B: De acordo com o desvio padrão das marcas a que apresenta maior consistência e previsibilidade de uso são as pilhas da marca B ")
print("PERGUNTA C: NÃO, o calculo de diferença do desvio padrão é +/- igual ")

#RESPOSTA PERGUNTA C
#CALCULO DESVIO PADRÃO
# = X157.14 - D12.41
# = X155.6 - D10.29

#MARCA A  *-144.73*  +169.55
#MARCA B  *-145.31*  +165.89
