Ejercicio 5 [2 puntos]
Para algún gen de las enzimas que intervienen en la ruta metabolica de la gluconeogenesis (Lista de genes por tipología), realice lo siguiente:

Una búsqueda en la página del NCBI nucleotide.

Descargue el Accession List de su búsqueda y guarde en la carpeta data.

Cargue el Accession List en este notebook y haga una descarga de las secuencias de los quince primeros IDs de la accesión.

Arme un árbol filogenético para los resultados del paso 3.

Guarde su arbol filogénetico en la carpeta img

Interprete el árbol del paso 4.

# Escriba aquí su código para el ejercicio 6

from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator 
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio import Phylo
from Bio import Entrez
from Bio import SeqIO
import Bio
import warnings
warnings.filterwarnings('ignore')
import os
import matplotlib
import matplotlib.pyplot as plt

with open("Data/glyceraldehyde-3-phosphate dehydrogenase .seq","r") as archivo:
    b=archivo.read()
    c=b.split('\n')
    a=0
    ListID=[]
    for line in c:
        if a != 15:
            ListID.append(line)
            a=a+1

Entrez.email = "A.N.Other@example.com" 
ofile=open('Data/Sequences.gb','w')
with Entrez.efetch( db="nucleotide", rettype="gb", retmode="text", id= ListID) as handle: 
    for seq_record in SeqIO.parse(handle, "gb"): 
        ofile.write(">"+str(seq_record.id)+str(seq_record.description[:50])+'\n')
        ofile.write(str(seq_record.seq)+'\n')
        ofile.write('\n')

ffile=open('Data/Sequences.fasta','w')
with open("Data/Sequences.gb",'r') as genbank:
    c=genbank.read()
    for line in c:
        ffile.write(str(line))
        
clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile = "Data/Sequences.fasta")
assert os.path.isfile(clustalw_exe), "Clustal_W executable is missing or not found"
stout,stderr = clustalw_cline()

ClustalAlign = AlignIO.read("Data/Sequences.aln", "clustal")

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(ClustalAlign)

constructor = DistanceTreeConstructor(calculator)
Data_tree = constructor.build_tree(ClustalAlign)
Data_tree.rooted = True

Phylo.write(Data_tree, "Data/Data_tree.xml", "phyloxml")

fig = plt.figure(figsize=(20, 25), dpi=200)  
matplotlib.rc('font', size=12)               
matplotlib.rc('xtick', labelsize=10)       
matplotlib.rc('ytick', labelsize=10)       
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(Data_tree, axes=axes)