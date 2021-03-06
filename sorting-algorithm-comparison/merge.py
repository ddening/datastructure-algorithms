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

import math

def mergeSortedLists(A, B):
    newList= list()
    a = 0; b = 0
    # Füge beide Listen zusammen bis eine leer ist("Mischen")
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            newList.append(A[a])
            a += 1
        else:
            newList.append(B[b])
            b += 1
    while a < len(A): # Wenn Liste A mehr Komponentenenthält, hänge diese an die neue Liste
        newList.append(A[a])
        a += 1
    while b < len(B): # Wenn Liste B mehr Komponenten enthält, hänge diese an die neue Liste
        newList.append(B[b])
        b += 1

    return newList

def mergeSort(A):

    if len(A) <= 1: # Basisfall
        return A
    else:
        mid = math.floor(len(A)/2)

        leftHalf = mergeSort(A[:mid])
        rightHalf = mergeSort(A[mid:])

        newList = mergeSortedLists(leftHalf, rightHalf)

    return newList