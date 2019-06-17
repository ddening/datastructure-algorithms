# Seminar Uebung 07 (Testa01)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://www.geeksforgeeks.org/bubble-sort/
# https://en.wikipedia.org/wiki/Bubble_sort
# https://www.inf-schule.de/grenzen/komplexitaet/sortieren/sortieralgorithmen/selectionsort
# https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
# https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google
# https://de.wikiversity.org/wiki/Kurs:Algorithmen_und_Datenstrukturen/Vorlesung/InsertionSort

# Libraries
import random
import matplotlib.pyplot
import copy
import bubble
import insertion
import selection

# Globale scope
MAX_NUMBERS_IN_LIST = 100 + 1
MAX_INTERV = 99

def _createList(MAX_NUMBERS_IN_LIST):
    '''Hilfsfunktion um eine einzige Liste mit zufaelligen Werten zu erstellen'''

    # Definition einer leeren Liste
    myList = []

    # Fülle Liste mit zufälligen Zahlen zwischen 0 und x
    myList = [random.randint(0, MAX_INTERV) for i in range(0, MAX_NUMBERS_IN_LIST)]

    return myList
  
def testListsGenerator(MAX_NUMBERS_IN_LIST):
    '''Erzeugt Liste mit Listen, welche zufaellige Zahlen beinhalten

    Args:
        MAX_NUMBERS_IN_LIST (const): Maximale Anzahl an Nummern in der letzen Liste

    Return:
        lst: Liste bestehend aus anderen Listen mit zufaelligen Zahlen gefuellt
    '''

    lst = []
    for i in range(0, MAX_NUMBERS_IN_LIST):
        lst.append(_createList(i))
    
    return lst
  
def plot():
    '''Plottet die Laufzeiten der Sortierverfahren in einem Diagramm '''

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1,1,1)

    # Initialliste
    ogLst = testListsGenerator(MAX_NUMBERS_IN_LIST)
    # Kopie fuer Bubblesort
    bubbleLst = copy.deepcopy(ogLst)
    # Kopie fuer InsertionSort
    insertionLst = copy.deepcopy(ogLst)
    # Kopie fuer SelectionSort
    selectionLst = copy.deepcopy(ogLst)
    # Kopie fuer MergeSort
    mergeLst = copy.deepcopy(ogLst)
    # Kopie fuer QuickSort
    quickLst = copy.deepcopy(ogLst)

    # Funktion [x ; y]
    # x: Anzahl der Elemente -- y: Zeit zum sortieren
    ax.plot([i for i in range(0, MAX_NUMBERS_IN_LIST)], [bubble.bubbleSort(j) for j in bubbleLst],  '.', color='c', )
    ax.plot([i for i in range(0, MAX_NUMBERS_IN_LIST)], [insertion.insertionSort(j) for j in insertionLst],  '.', color='m')
    ax.plot([i for i in range(0, MAX_NUMBERS_IN_LIST)], [selection.selectionSort(j) for j in selectionLst],  '.', color='r', )
    
    # Legende
    ax.set_title("Elemente in Liste im Intervall (0, %d)" % MAX_INTERV)
    ax.legend(['BubbleSort', 'InsertionSort', 'SelectionSort'])
    ax.set_xlabel('Anzahl Elemente in Liste')
    ax.set_ylabel('Sortierzeit in s')
    matplotlib.pyplot.show()

def main():
    '''Main Funktion '''
    plot()
    #bubble.bubbleSort(testListsGenerator(3))
    #createList(MAX_NUMBERS_IN_LIST)

main()