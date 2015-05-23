# ----------------------------------------------------------------------------
#  _______________________________
# < Word Permutation Rank - by Christopher Jones >
#  -------------------------------
# 1. convert letters to number ranking
# 2. figure out for each number calculate l, how many numbers to the
# right of it are less then it
# 3. divide by d, where d is the factorial number of duplicate numbers
# to the right of it. there may be multiple values of d
# 4. find the total number of permutations p of the current index. equal
# to the (length - 1)!
# 5. the rank = the summation of (l/d) * p. for all numbers n
#
# ----------------------------------------------------------------------------


import sys
from math import factorial


def readInput(argv):

    inputWord = argv[1].rstrip().upper()
    wordList = calculateRanking(inputWord)

    if inputWord is not None and inputWord.isalpha():

        wordList = calculateRanking(inputWord)
        lessThenList = calcluateValuesLessThenToTheRight(wordList)
        permutationsLost = calculateDuplicates(wordList)
        rank = calculateRank(inputWord, lessThenList, permutationsLost)
        print "Rank of " + inputWord + " is: " + str(rank)

    else:
        print "Error: Word can only contain letters in the alphabet.\n"


#
# Takes an input word as a string, and converts each character to ascii
# and adds it to a list
#
def calculateRanking(word):

    wordList = []
    for i in range(0, len(word)):
        currentChar = word[i]
        wordList.append(ord(currentChar))
    return wordList


#
# Takes a list of characters as input, and returns a list contains the number
# of values less then that value to the right in the original list
#
def calcluateValuesLessThenToTheRight(word):

    lessThenList = []
    for i in range(0, len(word)):
        numbersLessThenCurrent = 0
        for x in range(i, len(word)):
            if word[x] < word[i]:
                numbersLessThenCurrent += 1
        lessThenList.append(numbersLessThenCurrent)
    return lessThenList


#
# Takes a list of characters as input, and returns a list containing the
# number of permutations lost by duplications
#
def calculateDuplicates(word):

    permutationsLost = dict()
    characterFrequency = dict()
    currentValue = 1

    # first create character frequency dictionary
    for i in range(0, len(word)):
        currentChar = word[i]
        if currentChar in characterFrequency:
            characterFrequency[currentChar] += 1
        else:
            characterFrequency[currentChar] = 1

    # then iterate over all key/values, count the number of duplications
    for key in characterFrequency:
        if key != 1:
            currentValue = currentValue * factorial(characterFrequency[key])

    # next, iterate down the characters and figure out the number of
    # duplications with the [i-1] character removed from the dictionary
    for i in range(0, len(word)):
        currentChar = word[i]
        permutationsLost[i] = currentValue
        currentValue = currentValue / \
            factorial(characterFrequency[currentChar])
        characterFrequency[currentChar] -= 1
        currentValue = currentValue * \
            factorial(characterFrequency[currentChar])

    return permutationsLost


#
# Calculates the rank based off of the original word, and the number
# of permutations lost by character duplicates
#
def calculateRank(word, lessThenToTheRight, duplications):

    rank = 1
    for i in range(0, len(word)):
        rank += float(lessThenToTheRight[i]) / \
            (float(duplications[i])) * (factorial(len(word) - (i + 1)))
    return int(rank)

if __name__ == "__main__":

    readInput(sys.argv)
