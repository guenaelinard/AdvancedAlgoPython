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


def getDistance(i,j):
    distance = haversine(i,j)
    distance = round(distance, 2)
    return distance

def getTotalDistance(arr):
    total_dist = 0
    for i in range(len(arr)-1):
        lat1, lon1 = arr[i]
        lat2, lon2 = arr[i + 1]
        total_dist += haversine((lat1, lon1), (lat2, lon2))
    return total_dist

def nearest_neigbour() :
    optimizedPath = [positionsArray[0]]
    while len(positionsArray) != 0 :
        temp = 0
        minDistance = float('inf')
        for i in range(0,len(positionsArray)-1) :
            distance = getDistance(optimizedPath[len(optimizedPath)-1], positionsArray[i])
            if distance < minDistance and positionsArray[i] != optimizedPath[len(optimizedPath)-1] and optimizedPath[0] != len(optimizedPath)-1 :
                minDistance = distance
                temp = i
        optimizedPath.append(positionsArray[temp])
        positionsArray.remove(positionsArray[temp])
    return optimizedPath

print('optimized : ', optimizedPath, '\npositions : ',positionsArray)
optimizedPath = nearest_neigbour()
print('optimized : ', optimizedPath, '\npositions : ',positionsArray, '\ntotal distance : ',getTotalDistance(optimizedPath))
markCities(optimizedPath, map)
map.save("index.html")

