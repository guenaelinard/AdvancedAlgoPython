import random
import numpy as np
from haversine import haversine
import folium

positionsArray = [
   [45.171112, 5.695952],
   [45.183152, 5.699386],
   [45.174115, 5.711106],
   [45.176123, 5.722083],
   [45.184301, 5.719791],
   [45.184252, 5.730698],
   [45.170588, 5.716664],
   [45.193702, 5.691028],
   [45.165641, 5.739938],
   [45.178718, 5.74490],
   [45.176857, 5.76258],
   [45.188512, 5.76712],
   [45.174017, 5.70679],
   [45.174458, 5.68792],
   [45.185110, 5.73367],
   [45.185702, 5.73457],
   [45.184726, 5.73466],
   [45.184438, 5.73375],
   [45.184902, 5.73526],
   [45.174812, 5.69805],
   [45.169851, 5.69573],
   [45.180943, 5.69895],
   [45.176205, 5.69215],
   [45.171244, 5.68982]
]
optimizedPath = []
tab1 = list([0,1,8,3,4,5,7,2])
tab2 = list([3,5,7,1,0,2,8,4])
population = []
son = []

# -------------------------------------------------- MAP --------------------------------------------------

def markCities(cities, map):
    for city in cities:
        folium.Marker(
        location=[city[0], city[1]],
        tooltip=[city[0], city[1]],
        popup="This is a city " + str(city[0]) + " " + str(city[1]),
            icon=folium.Icon(icon="cloud")
        ).add_to(map)
        folium.PolyLine(optimizedPath).add_to(map)

map = folium.Map(location=[45.16667, 5.71667], zoom_start= 12)

# -------------------------------------------------- FUNCTIONS --------------------------------------------------

def getDistance(i,j):
    distance = haversine(i,j)
    distance = round(distance, 2)
    return distance

def getTotalDistance(arr):
    lat1, lon1 = arr[0]
    lat2, lon2 = arr[-1]
    total_dist =  haversine((lat1, lon1), (lat2, lon2))
    for i in range(len(arr)-1):
        lat1, lon1 = arr[i]
        lat2, lon2 = arr[i + 1]
        total_dist += haversine((lat1, lon1), (lat2, lon2))
    return total_dist

def swap(listVille, i, j):
    tempfile = listVille[i]
    listVille[i] = listVille[j]
    listVille[j] = tempfile
    return True

def réarmementDémographique():
    for i in range(24):
        shuffledList = positionsArray.copy()
        random.shuffle(shuffledList)
        population.append(shuffledList)
    return population

def crossover(daron1, daron2):
    son = []
    pivot = random.randint(1, len(daron1)-1)
    for firtGenes in range(len(daron1)-pivot):
        son.append(daron1[firtGenes])
    for secondGenes in range(len(daron2)):
        if daron2[secondGenes] not in son :
            son.append(daron2[secondGenes])
    return son

def getBestWay(population):
    minDistance = float('inf')
    temp = 0
    for i in range(len(population)-1):
        distance = getTotalDistance(population[i])
        if distance < minDistance:
            minDistance = distance
            temp = i
    return population[temp]

def iDontFeelSoGood(population):
    maxDistance = 0
    temp = 0
    for i in range(len(population)-1):
        distance = getTotalDistance(population[i])
        if distance > maxDistance:
            maxDistance = distance
            temp = i
    return population[temp]

def genetic_sort(population):
    réarmementDémographique()
    for j in range(100):
        for i in range(len(population)-1):
            dice = random.randint(0, len(population)-1)
            son = crossover(population[i], population[dice])
            dice2 = random.randint(1,6)
            if dice2 >= 3 :
                swap(son, i, dice2)
            totalSon = getTotalDistance(son)
            if totalSon < getTotalDistance(population[i]) and totalSon < getTotalDistance(population[dice]):
                population.append(son)
                population.remove(iDontFeelSoGood(population))
    return getBestWay(population)



optimizedPath = genetic_sort(population)
print(len(optimizedPath), optimizedPath)
print('distance : ',getTotalDistance(optimizedPath))
markCities(optimizedPath, map)
map.save("index.html")