import folium
from haversine import haversine


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

# -------------------------------------------------- MAP --------------------------------------------------
def markCities(cities, map):
    for city in cities:
        folium.Marker(
        location=[city[0], city[1]],
        tooltip=[city[0], city[1]],
        popup="This is a city " + str(city[0]) + " " + str(city[1]),
            icon=folium.Icon(icon="cloud")
        ).add_to(map)
        folium.PolyLine(optimizedPath+[cities[0]]).add_to(map)

map = folium.Map(location=[45.16667, 5.71667], zoom_start= 12)

def getDistance(point1, point2):
    return haversine(point1, point2)

def getTotalDistance(arr):
    lat1, lon1 = arr[0]
    lat2, lon2 = arr[-1]
    total_dist =  haversine((lat1, lon1), (lat2, lon2))
    for i in range(len(arr)-1):
        lat1, lon1 = arr[i]
        lat2, lon2 = arr[i + 1]
        total_dist += haversine((lat1, lon1), (lat2, lon2))
    return total_dist


def initMatrix(arr) :
    matrix = []
    for i in range(0,len(arr)) :
        matrix[i] = []
        for j in range(len(arr)) :
            matrix[i][j] = haversine(arr[i][j])
            getTotalDistance(matrix)
    print(matrix)
    return matrix

def glouton_sort() :
    optimizedPath = [positionsArray[0], positionsArray[1], positionsArray[2]]
    # tempArray = positionsArray.copy()
    while len(optimizedPath) != len(positionsArray) :
        n = len(positionsArray)
        for value in range(len(optimizedPath),n) :
            minDistance = float("inf")
            for testedPosition in range(len(optimizedPath)+1) :
                optimizedPath.insert(testedPosition, positionsArray[value])
                distance = getTotalDistance(optimizedPath)
                if distance < minDistance:
                    minDistance = distance
                    temp = testedPosition
                optimizedPath.remove(optimizedPath[testedPosition])
            optimizedPath.insert(temp, positionsArray[value])
    return optimizedPath

optimizedPath = glouton_sort()
print('\npositions : ',positionsArray, '\noptimized : ', optimizedPath, '\ntotal distance: ', getTotalDistance(optimizedPath))
markCities(optimizedPath, map)
map.save("index.html")