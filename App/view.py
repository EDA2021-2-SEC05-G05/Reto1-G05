"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Cargar artistas por fecha de nacimiento")
    print("3- Cargar adquisiciones por fecha de adquisición")
    print("4- Clasificar obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus autores")
    print("6- Costo de transportar obras de un departamento")
    print("0- Salir")

def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    controller.loadData(catalog)

def printArtistsResults(artists):
    size = lt.size(artists)
    if size < 6:
        print("La muestra es muy pequeña")
    else:
        primeros = 1
        ultimos = 2
        while primeros <= 3:
            artist = lt.getElement(artists, primeros)
            primeros+=1
            print('Nombre: ' + artist['DisplayName'] + " | Fecha de nacimiento: " + artist["BeginDate"] + ' | Fecha de fallecimiento: ' + controller.checkED(artist['EndDate']) + " | Nacionalidad: "+ controller.checkSTR(artist['Nationality']) + " | Genero: " + controller.checkSTR(artist['Gender'])+"\n")
        print(("-\n")*3)
        while ultimos >=0:
            artist = lt.getElement(artists, (lt.size(artists)-ultimos))
            print('Nombre: ' + artist['DisplayName'] + " | Fecha de nacimiento: " + artist["BeginDate"] + ' | Fecha de fallecimiento: ' + controller.checkED(artist['EndDate']) + " | Nacionalidad: "+ controller.checkSTR(artist['Nationality']) + " | Genero: " + controller.checkSTR(artist['Gender'])+"\n")
            ultimos-=1

def printSortResults(artworks):
    size = lt.size(artworks)
    if size < 6:
        print("La muestra es muy pequeña")
    else:
        primeros = 1
        ultimos = 2
        while primeros <= 3:
            artwork = lt.getElement(artworks, primeros)
            artists = controller.getArtists(catalog, artwork)
            strartists = controller.checkArtists(artists)
            primeros+=1
            print('Titulo: ' + artwork['Title'] + " | Artista(s): " + strartists + ' | Date Acquired: ' + artwork['DateAcquired'] + " | Medium: "+ controller.checkSTR(artwork['Medium']) + " | Dimensions: " + controller.checkSTR(artwork['Dimensions'])+"\n")
        print(("-\n")*3)
        while ultimos >=0:
            artwork = lt.getElement(artworks, (lt.size(artworks)-ultimos))
            artists = controller.getArtists(catalog, artwork)
            strartists = controller.checkArtists(artists)
            print('Titulo: ' + artwork['Title'] + " | Artista(s): " + strartists + ' | Date Acquired: ' + artwork['DateAcquired'] + " | Medium: "+ controller.checkSTR(artwork['Medium']) + " | Dimensions: " + controller.checkSTR(artwork['Dimensions'])+"\n")
            ultimos-=1
def printDicResults(artworks):
    size = lt.size(artworks)
    if size < 6:
        print("La muestra es muy pequeña")
    else:
        primeros = 1
        ultimos = 2
        while primeros <= 3:
            artwork = lt.getElement(artworks, primeros)
            artists = controller.getArtists(catalog, artwork)
            strartists = controller.checkArtists(artists)
            primeros+=1
            print('Titulo: ' + artwork['Title'] + " | Artista(s): " + strartists + ' | Date: ' + controller.checkSTR(artwork['Date']) + " | Medium: "+ controller.checkSTR(artwork['Medium']) + " | Dimensions: " + controller.checkSTR(artwork['Dimensions'])+"\n")
        print(("-\n")*3)
        while ultimos >=0:
            artwork = lt.getElement(artworks, (lt.size(artworks)-ultimos))
            artists = controller.getArtists(catalog, artwork)
            strartists = controller.checkArtists(artists)
            print('Titulo: ' + artwork['Title'] + " | Artista(s): " + strartists + ' | Date: ' + controller.checkSTR(artwork['Date']) + " | Medium: "+ controller.checkSTR(artwork['Medium']) + " | Dimensions: " + controller.checkSTR(artwork['Dimensions'])+"\n")
            ultimos-=1
def printNationalityList(dic):
    for i in dic:
        print(i, ": ", dic[i], "\n")
    return dic
catalog = None



"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = initCatalog()
        loadData(catalog)
    elif int(inputs[0]) == 2:
        date0 = input("Ingrese la fecha inicial en formato YYYY: ")
        datef = input("Ingrese la fecha final en formato YYYY: ")
        artistlt = controller.getArtistsByBD(catalog, date0, datef)
        print("El número total de autores dentro del rango es de: ", lt.size(artistlt), "\n")
        printArtistsResults(artistlt)
    elif int(inputs[0]) == 3:
        date0 = input("Ingrese la fecha inicial en formato YYYY-MM-DD: ")
        datef = input("Ingrese la fecha final en formato YYYY-MM-DD: ")
        r = controller.getArtworksByDA(catalog, date0, datef)
        print("El número total de obras dentro del rango es de: ", lt.size(r[0]))
        print("El número total de obras adquiridas por compra es de: ", r[1], "\n")
        printSortResults(r[0])

    elif int(inputs[0]) == 4:
        artistName = input("Ingrese el nombre del artista: ")
        answer = controller.tecniqueByArtist(catalog, artistName)
        print("Total Obras: " + str(answer["Total obras"]))
        print("Total Tecnicas: " + str(answer["Total tecnicas"]))
        print("Tecnica más utilizada: " + str(answer["Tecnica mas utilizada"]))
        print("El listado de las obras de dicha técnica: " + str(answer["Listado"]))

    elif int(inputs[0]) == 5:
        print("Cargando clasificación... \n")
        artworksbyn = controller.ArtworksPerNationality(catalog)
        dic = controller.sortDic(artworksbyn)
        printNationalityList(dic)
        first = next(iter(dic))
        list = controller.checkartworks(artworksbyn[first])
        printDicResults(list)
    elif int(inputs[0]) == 6:
        depa = input("Ingrese el departamento que desea investigar: ")
        l = controller.DepartmentCost(depa, catalog)

    else:
        sys.exit(0)
sys.exit(0)
