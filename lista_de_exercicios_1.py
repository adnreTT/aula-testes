#(1) Carregamento das Bibliotecas
import numpy as np

import scipy as sp


#(2) Entrada de Dados
resistencia = [348.5, 340.1, 360.8, 353.2, 357.6]

#(3) Processamento dos Dados
media = np.mean(resistencia)

#Variancia
variancia = np.var(resistencia)

#Desvio-padrao
desviopadrao = np.sqrt(variancia)

#Desvio-medio
# Passo 1: Calcular as diferenças absolutas
diferencas_absolutas = [abs(x - media) for x in resistencia]

# Passo 2: Calcular o desvio médio
desvio_medio = np.mean(diferencas_absolutas)



# Arredondamento
media = np.round(media,decimals=2)
desviopadrao = np.round(desviopadrao,decimals=2)
variancia = np.round(variancia,decimals=2)
desvio_medio = np.round(desvio_medio,decimals=2)


#4 Apresentação e Vizualizão dos Resultados
print("A média é: ", media)

print("A variância é: ", variancia)

print("O desvio-padrao é:", desviopadrao)

print("O desvio-médio é:", desvio_medio)