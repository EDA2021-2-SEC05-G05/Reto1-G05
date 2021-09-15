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
    return (int(artwork1["Date"])<int(artwork2["Date"]))

# Funciones de ordenamiento
def sortArtWork(catalog, size, sort_type):

    start_time = time.process_time()

    if sort_type == "shellsort":
            sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif sort_type == "mergesort":
            sorted_list = ml.sort(sub_list, cmpArtworkByDateAcquired)
    elif sort_type == "insertionsort":
            sorted_list = pq.sort(sub_list, cmpArtworkByDateAcquired)
    elif sort_type == "quicksort":
            sorted_list = rf.sort(sub_list, cmpArtworkByDateAcquired)

    sub_list = lt.subList(sorted_list, 0, size)
    
    return sorted_list
#def sortArtworksDate(cronologicalad):
    #sa.sort(cronologicalad, comparedate)

