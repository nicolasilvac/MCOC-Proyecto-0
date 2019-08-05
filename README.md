# Proyecto 0 Métodos Computacionales en Obras Civiles

## Pérdida de significancia en operaciones aritméticas

En este proyecto se expone sobre el concepto de pérdida de significancia en operaciones aritméticas de punto flotante. Para esta ocasión se ilustrará mediante la función que se utiliza para hallar el momento de inercia de una sección cuadrada, representada por la siguiente ecuación:
  INERCIA = b*h^3/12
donde b=base y h=altura

### Código

Primero se definen los parámetros y listas de 32 y 64 dígitos de significancia:

    b = 30 #base 
    h_0 = 50 #altura cero
    L_32=[h_0] #lista 32 bits 
    L_64=[h_0] #lista 64 bits``

Luego, para 15 iteraciones se calcula el error, y así se comparan la influencia de tener 32 y 64 dígitos de significancia:

    for i in range(15):

        H_anterior32=(L_32[-1]) 

        Inercia32 = b*H_anterior32^3/12

        L_32.append(np.float32(Inercia32)) 

        H_anterior64=(L_64[-1]) 

        Inercia64 = b*H_anterior64^3/12 

        L_64.append(np.float64(Inercia64))
        
De esta forma, se crea una lista para guardar el error que hay en cada iteración para luego poder gráficar.

        ERROR = []
    for i in range(15): 
      ERROR.append(abs(L_64[i]-abs(L_32[i]))/abs(L_64[i])) 
    pyplot.plot(ERROR)

    for i in range(15): 
      print "Inercia 32:",L_32[i],", Inercia 64:",L_64[i],",Error:", ERROR[i]

### Recursos

- Perdida de significancia wikipedia: [https://en.wikipedia.org/wiki/Loss_of_significance]
- Ejemplos de funciones para pérdida de significancia: [https://en.wikiversity.org/wiki/Numerical_Analysis/Loss_of_Significance]
