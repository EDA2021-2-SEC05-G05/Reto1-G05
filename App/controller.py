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
 """


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

from os import abort
import config as cf
import model
import csv

# Funciones para la carga de datos

def initCatalog():
    catalog = model.newCatalog()
    return catalog

def loadData(catalog):
    loadArtworks(catalog)
    loadArtists(catalog)
    
    

def loadArtists(catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


# Funciones de ordenamiento

def sortArtists(catalog):
    model.sortArtists(catalog)

def sortArtWorks(catalog):
    model.sortArtWorks(catalog)



# Funciones de consulta sobre el catálogo
def getArtistsByBD (catalog, date0, datef):
    sortArtists(catalog)
    return model.getArtistsByBD(catalog, date0, datef)

def getArtworksByDA (catalog, date0, datef):
    sortArtWorks(catalog)
    return model.getArtworksByDA (catalog, date0, datef)

def getArtists (catalog, artwork):
    return model.getArtists(catalog, artwork)
def checkArtists(artists):
    return model.checkArtists(artists)
def checkSTR(str):
    return model.checkSTR(str)
def checkED (ed):
    return model.checkED(ed)

def ArtworksPerNationality (catalog):
    return model.ArtworksPerNationality(catalog)
def sortDic(dic):
    return model.sortDic(dic)
def checkartworks(artworks):
    return model.checkartworks(artworks)
def DepartmentCost(depa, catalog):
    return model.DepartmentCost(depa, catalog)

def tecniqueByArtist(catalog, artistName):
    return model.tecniqueByArtist(catalog, artistName)