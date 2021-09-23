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
from DISClib.Algorithms.Sorting import mergesort as me
assert cf
import time
import math
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""



# Construccion de modelos

def newCatalog():
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

# Funciones para creacion de datos
def tecniqueByArtist(catalog, artistName):
    total_obras = 0
    contadorInicialTec = 0
    nombreTecnique = ""
    respuesta = {}

    artistId = getIdOfArtist(catalog, artistName)
    listOfMediums = []
    if artistId != None:
        for artwork in lt.iterator(catalog["artworks"]):
            if artistId in artwork['ConstituentID']:
                total_obras += 1
                if not artwork['Medium'] in listOfMediums:
                    listOfMediums.append(artwork['Medium'])
                
    for tecnique in range(len(listOfMediums)):
        contadorTecnique = getCountArtworksByTecnique(catalog, artistId, listOfMediums[tecnique])
        if contadorTecnique > contadorInicialTec:
            contadorInicialTec = contadorTecnique
            nombreTecnique = listOfMediums[tecnique]

    respuesta['Total obras'] = total_obras
    respuesta['Total tecnicas'] = len(listOfMediums)
    respuesta['Tecnica mas utilizada'] = nombreTecnique
    respuesta['Listado'] = getArtworkByTecnique(catalog, artistId, nombreTecnique)
    return respuesta

def getArtworkByTecnique(catalog, artistId, tecniqueName):
    final_list = []
    if artistId != None:
        for artwork in lt.iterator(catalog["artworks"]):
            if artistId in artwork['ConstituentID']:
                if artwork['Medium'] == tecniqueName:
                    final_dict = {}

                    tittle = artwork['Title']
                    date  = artwork['Date']
                    medio = artwork['Medium']
                    dimensiones = artwork['Dimensions']

                    final_dict['Titulo'] = tittle
                    final_dict['Fecha'] = date
                    final_dict['Tecnica'] = medio
                    final_dict['Dimensiones'] = dimensiones

                    final_list.append(final_dict)

    return final_list


def getCountArtworksByTecnique(catalog, artistId, tecniqueName):
    contador = 0
    if artistId != None:
        for artwork in lt.iterator(catalog["artworks"]):
            if artistId in artwork['ConstituentID']:
                if artwork['Medium'] == tecniqueName:
                    contador += 1
    return contador

def getIdOfArtist(catalog, artistName):
    artistId = None
    for artist in lt.iterator(catalog["artists"]):
        if artist['DisplayName'] == artistName:
            artistId = artist['ConstituentID']
    return artistId



def ArtworksPerNationality (catalog):
    artists = catalog["artists"]
    artworksbyn = {}
    for artwork in lt.iterator(catalog["artworks"]):
        id = artwork["ConstituentID"]
        id = id[1:-1]
        id = id.replace(" ", "")
        id = id.split(",")
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
                continue
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
    id = id[1:-1]
    id = id.replace(" ", "")
    id = id.split(",")
    artists = lt.newList()
    for i in range(1, lt.size(catalog["artists"])):
        artist = lt.getElement(catalog["artists"], i)
        if artist["ConstituentID"] in id:
            lt.addLast(artists, artist["DisplayName"])
            continue
    return artists

def DepartmentCost(depa, catalog):
    list = artworksbydepa(depa, catalog)
    for artwork in lt.iterator(list):
        r = checkDimensions(artwork)
        cost = r[0]
        dlist = r[1]
        if lt.size(dlist) == 2:
            pri = lt.getElement(dlist, 1)
            seg = lt.getElement(dlist, 2)
            a = (pri/100) * (seg/100)
            a = 72.00*a
        elif lt.size(dlist) ==3:
            pri = lt.getElement(dlist, 1)
            seg = lt.getElement(dlist, 2)
            ter = lt.getElement(dlist, 3)
            a = (pri/100) * (seg/100)* (ter/100)
            a = 72.00*a
        else: 
            a = 48.00
        if a > cost:
            cost =a
        if artwork["Weight (kg)"] != "0" and artwork["Weight (kg)"] != "":
            if "." in artwork["Weight (kg)"]:
                w = float(artwork["Weight (kg)"])
            else: 
                w = int(artwork["Weight (kg)"])
            w = w*72.00
            cost+=w
        cost = round(cost, 2)
        artwork["TransCost(USD)"] = cost
    return list

def getArtworksByDate (list):
    artworksbyDate = lt.newList()
    for artwork in lt.iterator(list):
        if artwork["Date"] != "":
            lt.addLast(artworksbyDate, artwork)
    return artworksbyDate  
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtistByBD (artist1, artist2):
    return (artist1["BeginDate"]<artist2["BeginDate"])
def cmpArtworkByDateAcquired(artwork1, artwork2):
    return (artwork1["DateAcquired"]<artwork2["DateAcquired"])
def cmpArtworkByDate(artwork1, artwork2):
    return (artwork1["Date"]<artwork2["Date"])
def cmpArtworkByCost(artwork1, artwork2):
    return (artwork1["TransCost(USD)"]>artwork2["TransCost(USD)"])

def compareMedium( artwork1 , artwork2):
    result = artwork1['Medium'] > artwork2['Medium']
    return result

# Funciones de ordenamiento
def sortArtists(catalog):
    me.sort(catalog["artists"], cmpArtistByBD)
def sortArtWorks(catalog):
    me.sort(catalog["artworks"], cmpArtworkByDateAcquired)
def sortArtWorksD(list):
    return me.sort(list, cmpArtworkByDate)
def sortArtWorksCost(list):
    return me.sort(list, cmpArtworkByCost)

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
def checkDimensions (artwork):
    height = artwork["Height (cm)"]
    width = artwork["Height (cm)"]
    depth = artwork["Depth (cm)"]
    diameter = artwork["Diameter (cm)"]
    lenght = artwork["Length (cm)"]
    circumference = artwork["Circumference (cm)"]
    cost = 0
    dimensions = lt.newList()
    if diameter != "0" and diameter != "":
        if circumference != "":
            if depth != "" and depth != "0":
                d = float(diameter)/100
                de = float(depth)/100
                cost = 2*math.pi*((float(d))/2)*(float(de)+((float(d))/2))
                cost = 72.00*cost
            if height != "" and height != "0":
                d = float(diameter)/100
                de = float(height)/100
                cost = 2*math.pi*((float(d))/2)*(float(de)+((float(d))/2))
                cost = 72.00*cost
            if lenght != "" and lenght != "0":
                d = float(diameter)/100
                de = float(lenght)/100
                cost = 2*math.pi*((float(d))/2)*(float(de)+((float(d))/2))
                cost = 72.00*cost
    if height !="" and height !="0":
        if "." in height:
            w = float(height)
        else: 
            w = int(height)
        lt.addLast(dimensions, w)
        
    if width != "" and width!="0":
        if "." in width:
            w = float(width)
        else: 
            w = int(width)
        lt.addLast(dimensions, w)
    if lenght != "" and lenght!="0":
        if "." in lenght:
            w = float(lenght)
        else: 
            w = int(lenght)
        lt.addLast(dimensions, w)
    if depth != "" and depth!="0":
        if "." in depth:
            w = float(depth)
        else: 
            w = int(depth)
        lt.addLast(dimensions, w)
    return cost, dimensions


    
        