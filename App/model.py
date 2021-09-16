"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ml
from DISClib.Algorithms.Sorting import insertionsort as pq
from DISClib.Algorithms.Sorting import quicksort as rf
assert cf
import time
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo):
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList(tipo, cmpfunction=cmpArtworkByDateAcquired)
    catalog['artists'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

# Funciones para creacion de datos



# Funciones de consulta

#def getCronologicalAd (catalog, date0, datef):
    #artworks = catalog["artworks"]
    #cronologicalad = lt.newList()
    #for i in range(1, (lt.size(artworks))):
        #artwork = lt.getElement(artworks, i)
        #date = artwork["Date"]
        #if date != "Unknown" or date != "n.d.":    
            #if date >= date0 and date <= datef:
                #lt.addLast(cronologicalad, artwork)
    
    #return cronologicalad

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"] == "" or artwork2["DateAcquired"] == "":
        return 1
    else:
        return (artwork1["DateAcquired"]<artwork2["DateAcquired"])

# Funciones de ordenamiento
def sortArtWork(catalog, size, sort_type):
    sub_list = lt.subList(catalog["artworks"], 1, size)
    sub_list = sub_list.copy()   
    start_time = time.process_time() 
    if sort_type == "shell":
            sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif sort_type == "merge":
            sorted_list = ml.sort(sub_list, cmpArtworkByDateAcquired)
    elif sort_type == "insertion":
            sorted_list = pq.sort(sub_list, cmpArtworkByDateAcquired)
    elif sort_type == "quick":
            sorted_list = rf.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()        
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
#def sortArtworksDate(cronologicalad):
    #sa.sort(cronologicalad, comparedate)

