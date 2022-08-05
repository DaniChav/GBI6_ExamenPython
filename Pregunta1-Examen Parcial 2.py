Ejercicio 1 [2 puntos]
Cree el archivo miningscience.py con las siguientes dos funciones:

i. download_pubmed: para descargar la data de PubMed utilizando el ENTREZ de Biopython. El parámetro de entrada para la función es el keyword.

ii. science_plots: la función debe

utilizar como argumento de entrada la data descargada por download_pubmed
ordenar los conteos de autores por país en orden ascedente y
seleccionar los cinco más abundantes. Con esta selección debe graficar un pie_plot. Como guía para el conteo por países puede usar el ejemplo de MapOfScience.
iii Cree un docstring para cada función.

Luego de crear las funciones, cargue el módulo miningscience como msc e imprima docstring de cada función.

# Escriba aquí su código para el ejercicio 1

# Importanto la libreria
import miningscience as msc

# Docstrings de las funciones del archivo 'miningscience.py' 
help(msc.download_pubmed)
help(msc.science_plots)

# Resolución

Help on function download_pubmed in module miningscience:

download_pubmed(keyword)
    Permite buscar artículos científicos en pubmed con un filtrado mediante el uso de palabras claves

Help on function science_plots in module miningscience:

science_plots(archivo)
    Permite generar un diagrama de pastel de los países a los que pertenecen los autores que han realizado publicaciones sobre un tema en particular