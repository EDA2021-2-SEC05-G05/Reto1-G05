﻿"""
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
from DISClib.Algorithms.Sorting import mergesort as me
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

def ArtworksPerNationality (catalog):
    artists = catalog["artists"]
    artworksbyn = {}
    for artwork in lt.iterator(catalog["artworks"]):
        id = artwork["ConstituentID"]
        for artist in lt.iterator(artists):
            if artist["ConstituentID"] in id:
                if artist["Nationality"] == "":
                    artist["Nationality"] = "Unknown"
                if artist["Nationality"] not in artworksbyn:
                    aw = lt.newList()
                    artworksbyn[artist["Nationality"]] = aw
                    lt.addLast(artworksbyn[artist["Nationality"]], artwork)
                else:
                    lt.addLast(artworksbyn[artist["Nationality"]], artwork)
    return artworksbyn


# Funciones de consulta

def getArtistsByBD (catalog, date0, datef):
    artists = catalog["artists"]
    artistsbyBG = lt.newList()
    for n in range(1, lt.size(artists)):
        artist = lt.getElement(artists, n)
        if artist["BeginDate"] != "0":
            if artist["BeginDate"]>=date0:
                if artist["BeginDate"]<=datef:
                    lt.addLast(artistsbyBG, artist)
                else:
                    return artistsbyBG
    return artistsbyBG
def getArtworksByDA (catalog, date0, datef):
    artworks = catalog["artworks"]
    artworksbyDA = lt.newList()
    purchased = 0
    for n in range(1, lt.size(artworks)):
        artwork = lt.getElement(artworks, n)
        if artwork["DateAcquired"] != "":
            if artwork["DateAcquired"]>=date0:
                if artwork["DateAcquired"]<= datef:
                    lt.addLast(artworksbyDA, artwork)
                    if "Purchase" in artwork["CreditLine"] or "Purchased" in artwork["CreditLine"]:
                        purchased += 1
                else:
                    return artworksbyDA, purchased
    return artworksbyDA, purchased

def getArtists (catalog, artwork):
    id = artwork["ConstituentID"]
    artists = lt.newList()
    for i in range(1, lt.size(catalog["artists"])):
        artist = lt.getElement(catalog["artists"], i)
        if artist["ConstituentID"] in id:
            lt.addLast(artists, artist["DisplayName"])
    return artists

def DepartmentCost(depa, catalog):
    list = artworksbydepa(depa, catalog)
    for n in lt.iterator(list):
        if 
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtistByBD (artist1, artist2):
    return (artist1["BeginDate"]<artist2["BeginDate"])
def cmpArtworkByDateAcquired(artwork1, artwork2):
    return (artwork1["DateAcquired"]<artwork2["DateAcquired"])

# Funciones de ordenamiento
def sortArtists(catalog):
    me.sort(catalog["artists"], cmpArtistByBD)
def sortArtWorks(catalog):
    me.sort(catalog["artworks"], cmpArtworkByDateAcquired)

def checkID (id):
    id = id[1:-1]
    id = id.split(",")
    return id

def checkArtists (artists):
    strartists = lt.getElement(artists, 1)
    if lt.size(artists) >= 2:
                i = 2
                while i <= lt.size(artists):
                    strartists = strartists + ", "+ lt.getElement (artists, i)
                    i += 1
    return strartists

def checkSTR(str):
    if str == "":
        str = "Unknown"
    return str

def checkED(ed):
    if ed == "0":
        ed = "Aún vivo"
    return ed
def sortDic(dic):
    b = {}
    for i in dic:
        b[i] = lt.size(dic[i])
    dic = dict(sorted(b.items(), key=lambda x: x[1], reverse=True)[:10])
    return dic
def checkartwork (list, artwork):
    title = artwork["Title"]
    for n in lt.iterator(list):
        if n['Title'] == title:
            return True
def checkartworks(artworks):
    i = 1
    unique = lt.newList()
    while i < lt.size(artworks):
        aw = lt.getElement(artworks, i)
        if i == lt.size(artworks):
            lt.addLast(unique, aw)
            return unique
        else:
            nextaw = lt.getElement(artworks, i+1)
            if aw["Title"] != nextaw["Title"]:
                lt.addLast(unique, aw)
        i +=1
    return unique

def artworksbydepa (depa, catalog):
    list = lt.newList()
    for n in lt.iterator(catalog["artworks"]):
        if n["Department"] == depa:
            lt.addLast(list, n)
    return list
