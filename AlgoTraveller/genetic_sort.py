import random
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


map = folium.Map(location=[45.16667, 5.71667], zoom_start=12)


# -------------------------------------------------- FUNCTIONS --------------------------------------------------

def getDistance(i, j):
    distance = haversine(i, j)
    distance = round(distance, 2)
    return distance


def getTotalDistance(arr):
    lat1, lon1 = arr[0]
    lat2, lon2 = arr[-1]
    total_dist = haversine((lat1, lon1), (lat2, lon2))
    for i in range(len(arr) - 1):
        lat1, lon1 = arr[i]
        lat2, lon2 = arr[i + 1]
        total_dist += haversine((lat1, lon1), (lat2, lon2))
    return total_dist


def swap(listVille, i, j):
    temp_file = listVille[i]
    listVille[i] = listVille[j]
    listVille[j] = temp_file
    return True

def generateStartingPoints():
    shuffledPath = positionsArray.copy()
    random.shuffle(shuffledPath)
    starting_route = shuffledPath[:3]
    return starting_route

def two_opt(route):
    # Implementation of 2-opt algorithm
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue  # No point in reversing a single edge
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # Reverse the segment between i and j
                if getTotalDistance(new_route) < getTotalDistance(route):
                    route = new_route
                    improved = True
                    break
            if improved:
                break
    return route


def glouton_sort(targetArray):
    tested_path = generateStartingPoints()
    while len(optimizedPath) != len(targetArray):
        n = len(targetArray)
        for value in range(len(tested_path), n):
            minDistance = float("inf")
            for testedPosition in range(len(tested_path) + 1):
                tested_path.insert(testedPosition, targetArray[value])
                distance = getTotalDistance(tested_path)
                if distance < minDistance:
                    minDistance = distance
                    temp = testedPosition
                tested_path.remove(tested_path[testedPosition])
            optimizedPath.insert(temp, targetArray[value])
    return optimizedPath


def create_population(size):
    shuffled_list = []
    for i in range(size):
        shuffled_list.insert(i, positionsArray.copy())
        random.shuffle(shuffled_list[i])
        glouton_sort(shuffled_list[i])
        population.append(shuffled_list[i])
    glouton_sort(population)
    return population


def crossover(daron1, daron2):
    son = []
    pivot = random.randint(1, len(daron1) - 1)
    for firstGenes in range(len(daron1) - pivot):
        son.append(daron1[firstGenes])
    for secondGenes in range(len(daron2)):
        if daron2[secondGenes] not in son:
            son.append(daron2[secondGenes])
    return son


def mutation(son):
    pos1 = random.randint(0, len(son) - 1)
    pos2 = random.randint(0, len(son) - 1)
    son[pos1], son[pos2] = son[pos2], son[pos1]
    return son


def get_optimized_path(population):
    minDistance = float('inf')
    temp = 0
    for i in range(len(population) - 1):
        distance = getTotalDistance(population[i])
        if distance < minDistance:
            minDistance = distance
            temp = i
    return population[temp]


def reinsertion(population):
    maxDistance = 0
    temp = 0
    for i in range(len(population) - 1):
        distance = getTotalDistance(population[i])
        if distance > maxDistance:
            maxDistance = distance
            temp = i
    return population[temp]


def genetic_sort(arr, populationSize, testRange, mutationRate):
    create_population(populationSize)
    print('initial optimized distance : ', getTotalDistance(get_optimized_path(arr)))
    for j in range(testRange):
        for i in range(len(arr) - 1):
            dice = random.randint(0, len(arr) - 1)
            son = crossover(arr[i], arr[dice])
            # mutation(son)
            # two_opt(son)
            dice2 = mutationRate
            if dice2 >= 3:
                swap(son, i, dice2)
        two_opt(son)
        totalSon = getTotalDistance(son)
        if totalSon < getTotalDistance(arr[i]) and totalSon < getTotalDistance(arr[dice]):
            arr.append(son)
            arr.remove(reinsertion(arr))
            print('new optimized distance : ', getTotalDistance(get_optimized_path(population)))
    return get_optimized_path(population)


optimizedPath = genetic_sort(population, 10, 50, random.randint(1, 6))
print(len(optimizedPath), optimizedPath)
print('final distance : ', getTotalDistance(optimizedPath))
markCities(optimizedPath, map)
map.save("index.html")
