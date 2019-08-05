Proyecto 0 Métodos Computacionales en Obras Civiles
=============
Pérdida de significancia en operaciones aritméticas
=======
En este proyecto se expone sobre el concepto de perdida de significancia en operaciones aritméticas de punto flotante. Para esta ocasión se ilustrará mediante la función que se utiliza para hallar el momento de inercia de una sección cuadrada, representada por la siguiente ecuación:
  INERCIA = b*h^3/12
donde b=base y h=altura

Resultados
=============
Se utilizó el error relativo como:
ERROR = (Promedio_Calculado - Resultado_Exacto) / Resultado_Exacto
Fueron 15 las iteraciones para obtener una mayor precisión.


Recursos
=========
- Perdida de significancia wikipedia: [https://en.wikipedia.org/wiki/Loss_of_significance]
- Ejemplos de funciones para pérdida de significancia: [https://en.wikiversity.org/wiki/Numerical_Analysis/Loss_of_Significance]

from matplotlib import pyplot
import numpy as np
#Parametros de la seccion cuadrada para el calculo del momento de inercia
b = 30 #base
h_0 = 50 #altura cero 


L_32=[h_0] #lista 32 bits
L_64=[h_0] #lista 64 bits

for i in range(15):
    H_anterior32=(L_32[-1])
    Inercia32=b*H_anterior32^3/12 
    L_32.append(np.float32(Inercia32))
    H_anterior64=(L_64[-1])
    Inercia64 = b*H_anterior64^3/12 
    L_64.append(np.float64(Inercia64))

ERROR = []

for i in range(15):
    ERROR.append(abs(L_64[i]-abs(L_32[i]))/abs(L_64[i]))
pyplot.plot(ERROR)

for i in range(15):  #imprimimos el recorrido de los 5 numeros
    print "Inercia 32:",L_32[i],", Inercia 64:",L_64[i],",Error:", ERROR[i]
