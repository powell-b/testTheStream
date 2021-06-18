"""
This is a Demo Helper Funktion
"""

import random

def testFunktion():
    """
    Diese Funktion erstellt eine Matrix mit der Diemension (nxn). 
    Wobei n eine zufällige Zahl zwischen 1 und 10 ist. 
    Diese Funktion benutzt das Modul random.
    
    Returns:
    ------------
        rData: List(List(int))
            Two-dimensional list with random numbers between 1 and 100 with dimension n by n 
        
        rIndex: List(String)
            List that contains the Labels for the Rows
        
        rCol: List(String)
            List that contains the Labels for the Colums

    
    Example: 
    ------------
    This would be a example output: 
    (
        [
            [72, 12, 75], 
            [11, 46, 49], 
            [16, 23, 71]],
        [
            'Zeile 1', 
            'Zeile 2', 
            'Zeile 3'
        ],
        [
            'Spalte 1', 
            'Spalte 2', 
            'Spalte 3'
            ]
    )

    """
    n = random.randint(1,10);
    rData = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(random.randint(1,100))
        rData.append(temp)

    rIndex = ["Zeile {}".format(i+1) for i in range(n)]
    rCols = ["Spalte {}".format(i+1) for i in range(n)]
    
    return rData, rIndex, rCols