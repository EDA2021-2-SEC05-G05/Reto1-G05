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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

# Funciones para creacion de datos



# Funciones de consulta

def getCronologicalAd (catalog, date0, datef):
    artworks = catalog["artworks"]
    cronologicalad = lt.newList()
    for i in range(1, (lt.size(artworks))):
        artwork = lt.getElement(artworks, i)
        date = artwork["Date"]
        date = checkdate(date)
        if date != "Unknown" or date != "n.d.":    
            if date >= date0 and date <= datef:
                lt.addLast(cronologicalad, artwork)
    
    return cronologicalad

# Funciones utilizadas para comparar elementos dentro de una lista

def comparedate(artwork1, artwork2):
    return (int(artwork1['Date']) > int(artwork2['Date']))

# Funciones de ordenamiento

def sortArtworksDate(cronologicalad):
    sa.sort(cronologicalad, comparedate)

def checkdate (date):
    if "." in date:
        date = date.replace(".", "")
    if "(" in date or ")" in date:
        date = date.replace("(", "")
        date = date.replace(")", "")
    if "c. " in date or "-" == date[0] or "Before " in date or "before " in date:
        date = date[-4:]
    if "newspaper published " in date:
        date = date.replace("newspaper published ", "")
    if "s" == date[len(date)-1]:
        date.replace(date[len(date)-1], "")
    return date