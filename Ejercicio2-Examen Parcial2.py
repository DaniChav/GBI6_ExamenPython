Ejercicio 2 [2 puntos]
Utilice dos veces la función download_pubmed para:

Descargar la data, utilizando los keyword de su preferencia.
Guardar el archivo descargado en la carpeta data.
Para cada corrida, imprima lo siguiente:

'El número artículos para KEYWORD es: XX' # Que se cargue con inserción de texto o valor que correspondea KEYWORD y XX

# Escriba aquí su código para el ejercicio 2


import os
import re
a = msc.download_pubmed("monkey pox")
b = len (a)
print ('El número artículos para KEYWORD es: ',b)
with open ("Data/pubmed-monkeypox-set.txt","w") as txt:
    txt.write(a)

# Resolución

El número artículos para KEYWORD es:  1854428
    
# Escriba aquí su código para el ejercicio 2


import os
import re
c = msc.download_pubmed("covid")
d = len (c)
print ('El número artículos para KEYWORD es: ',d)
with open ("Data/pubmed-covid.txt","w") as txt:
    txt.write(c)
    
# Resolución

El número artículos para KEYWORD es:  2002252