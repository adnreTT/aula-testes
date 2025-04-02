#(1) Carregamento das Bibliotecas
import numpy as np

import scipy as sp


#(2) Entrada de Dados
dureza= [83.3, 80.7, 86.4, 88.3, 84.7,  85.2, 82.8, 87.8, 86.9, 86.2, 83.5, 84.4, 87.2, 85.5, 86.3 ]


#(3) Processamento dos Dados
media = np.mean(dureza)
mediana = np.median(dureza)

# variancia
variancia = np.var(dureza)


#Desvio-padrao
desviopadrao = np.sqrt(variancia)




# Arredondamento
media = np.round(media,decimals=2)
mediana = np.round(mediana, decimals=2)
desviopadrao = np.round(desviopadrao,decimals=2)
variancia = np.round(variancia,decimals=2)






#4 Apresentação e Vizualizão dos Resultados
print("A média da dureza é: ", media)
print("A mediana da dureza é: ", mediana)
print("O desvio-padrao da dureza é:", desviopadrao)






