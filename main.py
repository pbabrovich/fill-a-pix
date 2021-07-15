import numpy
import sys
from numpy import loadtxt
import random


def generateAnswers(tab):
    x = len(tab)
    y = len(tab[0])
    answers = numpy.empty([x, y], dtype=str)
    for i in range(x):
        for j in range(y):
            counter = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    tempX = i + k
                    tempY = j + l
                    if tempX < 0 or tempX > x - 1 or tempY < 0 or tempY > y - 1:
                        continue
                    if tab[tempX][tempY] == 1:
                        counter += 1
            answers[i][j] = counter

    minimizeSteps = 5
    for i in range(x):
        for n in range(minimizeSteps):
            duplicates = calculateRowDuplicates(i, answers)
            if duplicates > 3:
                for j in range(duplicates):
                    answers[i][random.randint(0, y-1)] = " "

    return answers


def calculateRowDuplicates(row, values):
    y = len(values[row])
    maxDuplicates = 0
    for i in range(10):
        duplicates = 0
        for j in range(y):
            temp = "{}".format(i)
            if values[row][j] == temp:
                duplicates += 1
        if duplicates > maxDuplicates:
            maxDuplicates = duplicates
    return maxDuplicates


def checkSolution(solution, answersArray):
    x = len(solution)
    y = len(solution[0])
    for i in range(x):
        for j in range(y):
            counter = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    tempX = i + k
                    tempY = j + l
                    if tempX < 0 or tempX > x - 1 or tempY < 0 or tempY > y - 1:
                        continue
                    if solution[tempX][tempY] == 1:
                        counter += 1
            if answersArray[i][j] != " " and answersArray[i][j] != str(counter):
                return False
    return True


def printArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], "| ", end='')
        print("")


def show_picture(arrayToPrint):
    CBLACK = '\33[30m'
    CWHITE = '\33[38m'
    for i in range(len(arrayToPrint)):
        for j in range(len(arrayToPrint[0])):
            if arrayToPrint[i][j] == 1:
                sys.stdout.write(CBLACK)
                print("▇", end='')
                print("▇", end='')
                sys.stdout.write(CWHITE)
            else:
                sys.stdout.write(CWHITE)
                print("▇", end='')
                print("▇", end='')
                sys.stdout.write(CBLACK)

        print("")


def main():
    picture = loadtxt("data.txt", comments="#", delimiter=",", unpack=False)

    print("Initial array:")
    printArray(picture)

    answers = generateAnswers(picture)

    print("\nTable to solve:")
    printArray(answers)

    falseSolution = loadtxt("false_solution.txt", comments="#", delimiter=",", unpack=False)

    result = checkSolution(falseSolution, answers)

    print("\nChecking false solution :", result)
    printArray(falseSolution)

    result = checkSolution(picture, answers)

    print("\nChecking right solution :", result)
    printArray(picture)

    print("\nSolved picture: ")
    show_picture(picture)


if __name__ == '__main__':
    main()
