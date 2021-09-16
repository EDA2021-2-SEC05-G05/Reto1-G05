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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Cargar adquisiciones por fecha de adquisición")
    print("0- Salir")

def initCatalog(tipo):
    return controller.initCatalog(tipo)


def loadData(catalog):
    controller.loadData(catalog)

def printSortResults(artworks, sample=10):
    size = lt.size(artworks)
    if size > sample:
        print("Las primeras ", sample, " obras ordenadas son:")
        i=1
        while i <= sample:
            artwork = lt.getElement(artworks,i)
            print('Titulo: ' + artwork['Title'] + ' Date Acquired: ' + artwork['DateAcquired'])
            i+=1
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = input("""Escriba ARRAY_LIST si desea una representación de
                      tipo array_list o LINKED_LIST si desea de tipo linked_list: """)
        catalog = initCatalog(tipo)
        loadData(catalog)
    elif int(inputs[0]) == 2:
        ext = input("Ingrese la cantidad de elementos que desea ver, no debe ser mayor a " + str(lt.size(catalog["artworks"])) +": ")
        sorttype = input("Escriba el tipo de algoritmo de ordenamiento que desea que se use para ordenar el catálogo de obras, estos son: insertion, shell, merge o quick: ")
        artworks = controller.sortArtWork(catalog, int(ext), sorttype)
        printSortResults(artworks[1])
    else:
        sys.exit(0)
sys.exit(0)
