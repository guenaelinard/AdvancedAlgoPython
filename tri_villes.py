from tkinter import *
from tkinter import filedialog
import csv
import time
import folium
from haversine import haversine


class Ville:
    def __init__(self, nom_commune, codes_postaux, latitude, longitude, dist, distanceFromGrenoble):
        self.nom_commune = nom_commune
        self.codes_postaux = codes_postaux
        self.latitude = latitude
        self.longitude = longitude
        self.dist = dist
        self.distanceFromGrenoble = distanceFromGrenoble


def loadFile():
    listVille.clear()
    filename = filedialog.askopenfilename(initialdir="./",
                                          title="Selection du Fichier",
                                          filetypes=(("Text files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    changeLabelFile("Fichier : " + filename)
    with open(filename, 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            data = row[0].split(";")
            try:
                ville = Ville(data[8], data[9], float(data[11]), float(data[12]), float(data[13]), 0)
                ville.distanceFromGrenoble = getDistanceFromGrenoble(ville)
                listVille.append(ville)
            except:
                continue


def getDistanceFromGrenoble(ville):
    lat_grenoble = 45.166667
    lon_grenoble = 5.716667

    distance = haversine((lat_grenoble, lon_grenoble), (ville.latitude, ville.longitude))
    distance = round(distance, 2)

    return distance


def getDistance(ville1, ville2):
    distance = haversine((ville1.latitude, ville1.longitude), (ville2.latitude, ville2.longitude))
    distance = round(distance, 2)
    return distance


def isLess(listVille, i, j):
    if listVille[i].distanceFromGrenoble < listVille[j].distanceFromGrenoble:
        return True


def swap(listVille, i, j):
    temp_file = listVille[i]
    listVille[i] = listVille[j]
    listVille[j] = temp_file
    return True


def changeLabelFile(text):
    labelFileExplorer = Label(fenetre,
                              text=text,
                              width=120, height=4,
                              fg="black", background="#579BB1")
    labelFileExplorer.place(x=150, y=offset + 40)


def changeLabelButtonSubmit(text):
    buttonValidation['text'] = text
    buttonValidation.place(x=150, y=offset + 120)


def onSelectTypeTri(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        global typeTriSelection
        typeTriSelection = data
        changeLabelButtonSubmit("Lancement du {}".format(data))


def sort():
    # effacement de la liste affichée
    listVilleSortedBox.delete(0, END)
    listVilleSorted = listVille.copy()

    if typeTriSelection == "Tri par insertion":
        listVilleSorted = insert_sort(listVilleSorted)
    elif typeTriSelection == "Tri par sélection":
        listVilleSorted = selection_sort(listVilleSorted)
    elif typeTriSelection == "Tri à bulles":
        listVilleSorted = bubble_sort(listVilleSorted)
    elif typeTriSelection == "Tri de Shell":
        listVilleSorted = shell_sort(listVilleSorted)
    elif typeTriSelection == "Tri par fusion":
        listVilleSorted = merge_sort(listVilleSorted)
    elif typeTriSelection == "Tri par tas":
        listVilleSorted = heap_sort(listVilleSorted)
    elif typeTriSelection == "Tri rapide":
        listVilleSorted = quick_sort(listVilleSorted, 0, len(listVilleSorted) - 1)
    elif typeTriSelection == "Tri Nearest":
        listVilleSorted = nearest_sort(listVilleSorted)
    elif typeTriSelection == "Tri Glouton":
        listVilleSorted = glouton_sort(listVilleSorted)
    elif typeTriSelection == "Tri 2-opt":
        listVilleSorted = two_opt_sort(listVilleSorted)

    for ville in range(len(listVilleSorted)):
        listVilleSortedBox.insert(END, listVilleSorted[ville].nom_commune + " - (" + str(
            listVilleSorted[ville].distanceFromGrenoble)
                                  + " km de Grenoble)")
        listVilleSortedBox.itemconfig(ville, fg="black")

    listVilleSortedBox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listVilleSortedBox.yview)


# -------------------------------------------------- SORT FUNCTIONS --------------------------------------------------

def insert_sort(listVille):
    n = len(listVille)
    for i in range(n):
        temp = listVille[i]
        j = i
        while j > 0 and isLess(listVille, j, j - 1):
            listVille[j] = listVille[j - 1]
            j = j - 1
            listVille[j] = temp

    return listVille


def selection_sort(listVille):
    n = len(listVille)
    for i in range(n):
        minVal = i
        for j in range(i + 1, n):
            if isLess(listVille, j, minVal):
                swap(listVille, j, minVal)

    return listVille


def bubble_sort(listVille):
    n = len(listVille)
    passage = 0
    permute = True
    while permute:
        permute = False
        for i in range(n - 1 - passage):
            if isLess(listVille, i + 1, i):
                swap(listVille, i, i + 1)
                permute = True
        passage = passage + 1

    return listVille


def shell_sort(listVille):
    length = len(listVille)
    n = 0
    while n < int(length / 3):
        n = 3 * n + 1  # Ceci est le gap

    while n > 0:
        for i in range(n, length):
            j = i
            while j > n - 1 and isLess(listVille, j, j - n):
                swap(listVille, j, j - n)
                j = j - n
        n = int((n - 1) / 3)
    return listVille


def merge_sort(listVille):
    print("implement me !")
    return listVille


def heap_sort(listVille):
    print("implement me !")
    return listVille


def quick_sort(listVille, first, last):
    if first < last:
        p = partition(listVille, first, last)
        quicksort(listVille, first, p - 1)
        quicksort(listVille, p + 1, last)

    return listVille


def partition(listVille, first, last):
    pivot = listVille[last]
    i = first - 1
    for j in range(first, last):
        if isLess(listVille, j, last):
            i = i + 1
            listVille[i], listVille[j] = listVille[j], listVille[i]
    listVille[i + 1], listVille[last] = listVille[last], listVille[i + 1]
    return i + 1


def nearest_sort(listVille):
    optimizedPath = [listVille[0]]
    while len(listVille) != 0:
        temp = 0
        minDistance = float('inf')
        for i in range(0, len(listVille) - 1):
            distance = getDistance(optimizedPath[len(optimizedPath) - 1], listVille[i])
            if distance < minDistance and listVille[i] != optimizedPath[len(optimizedPath) - 1]:
                minDistance = distance
                temp = i
        optimizedPath.append(listVille[temp])
        listVille.remove(listVille[temp])
    return optimizedPath


# Creation de la fenêtre
fenetre = Tk()
width = 1000
height = 180
offset = 10
listVille = []
listTri = ["Tri par insertion",
           "Tri par sélection",
           "Tri à bulles",
           "Tri de Shell",
           "Tri par fusion",
           "Tri par tas",
           "Tri rapide",
           "Tri Nearest",
           "Tri Glouton",
           "Tri 2-opt"]

typeTriSelection = "Tri par insertion"

labelFileExplorer = Label()
canvas = Canvas(fenetre, width=width + 2 * offset,
                height=height + 2 * offset, bg='white')
buttonValidation = Button(command=sort)

list = Listbox(fenetre, width=20, height=len(listTri), selectmode="single")
list.place(x=offset, y=offset)
list.bind("<<ListboxSelect>>", onSelectTypeTri)

for typeTri in range(len(listTri)):
    list.insert(END, listTri[typeTri])
    list.itemconfig(typeTri, fg="black")

buttonFile = Button(
    fenetre, text="Importation du fichier", command=loadFile)
buttonFile.place(x=150, y=offset)

changeLabelButtonSubmit("Lancement du {}".format(typeTriSelection))

changeLabelFile("Aucun Fichier ...")

canvas.pack()

listVilleSortedBox = Listbox(
    fenetre, width=100, height=25, selectmode="single")
listVilleSortedBox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(fenetre, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)
fenetre.mainloop()
