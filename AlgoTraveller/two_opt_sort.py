import random
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
        folium.PolyLine(positionsArray + [cities[0]]).add_to(map)


map = folium.Map(location=[45.16667, 5.71667], zoom_start=12)


def distance(point1, point2):
    # Calculate Euclidean distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def total_distance(route, cities):
    # Calculate the total distance of a route
    total = 0
    for i in range(len(route) - 1):
        total += distance(cities[route[i]], cities[route[i + 1]])
    total += distance(cities[route[-1]], cities[route[0]])  # Return to the starting city
    return total


def two_opt(route, cities):
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
                if total_distance(new_route, cities) < total_distance(route, cities):
                    route = new_route
                    improved = True
                    break
            if improved:
                break
    return route


# Example usage
initial_route = list(range(24))
random.shuffle(initial_route)  # Shuffle the initial route
print("Initial route:", initial_route)
print("Initial total distance:", total_distance(initial_route, positionsArray))
optimized_route = two_opt(initial_route, positionsArray)
print("Optimized route:", optimized_route)
print("Optimized total distance:", total_distance(optimized_route, positionsArray))

markCities(positionsArray, map)
map.save("index.html")
