from matplotlib import pyplot 
import numpy as np 
#Parametros de la seccion cuadrada para el calculo del momento de inercia 
b = 30 #base 
h_0 = 50 #altura cero

L_32=[h_0] #lista 32 bits 
L_64=[h_0] #lista 64 bits

for i in range(15): 
   H_anterior32=(L_32[-1]) 
   Inercia32 = b*H_anterior32^3/12
   L_32.append(np.float32(Inercia32)) 
   H_anterior64=(L_64[-1]) 
   Inercia64 = b*H_anterior64^3/12 
   L_64.append(np.float64(Inercia64))
	
ERROR = []
for i in range(15): 
  ERROR.append(abs(L_64[i]-abs(L_32[i]))/abs(L_64[i])) 
pyplot.plot(ERROR)
	
for i in range(15): 
  print "Inercia 32:",L_32[i],", Inercia 64:",L_64[i],",Error:",ERROR[i]
