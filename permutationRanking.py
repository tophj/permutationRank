# ----------------------------------------------------------------------------
#  _______________________________
# < Permutation Ranking - by Christopher Jones >
#  -------------------------------
#
# A way to mathematically figure out a word's rank among it's permutations
# 
# Usage:
# Correct usage is: python permutationRanking.py INPUTWORD
#
# Steps:
# 1. Convert letters to ascii value
# 2. Iterate over, figure out how many ascii values are lower than
#    the current value(including duplicates)
#    EX. BAAA = [66,65,65,65] = [3,0,0,0]
# 3. While iterating, calculate the production
#    of the factorial of all duplicates
#    EX. BAAA (current is B) = (# of A's)! * (# of B's)! = 3! * 1! = 6
# 4. Factor out the number of duplicates, by dividing the number found in 2,
#    by the number found in 3
#    EX. BAAA = [3,0,0,0] (found 2), and [6,2,1,1] (from 3)
#             = 3/6, 0/2, 0/1, 0/1 = [1/2,0,0,0]
# 5. Find the total number of permutations p, of the current letter.
#    EX. BAAA = [3!,2!,1!,0!]
# 6. The rank is equal to the summation of (value from 4 * value from 5) + 1
#    EX. BAAA = (1/2 * 3!) + (0 * 2!) + (0 * 1!) + (0 * 0!) + 1
#             = 2 + 0 + 0 + 0 + 1 = 3
#
# ----------------------------------------------------------------------------


import sys
from math import factorial

#
# Reads in the command line parameter, checks if it's a word, and finds it's
# permutation ranking using the steps above
#
def readInput(argv, output=sys.stdout):

    inputWord = argv[1].rstrip()

    if inputWord is not None and inputWord.isalpha():

        wordList = stringToAsciiList(inputWord)
        precedingList = calcluatePrecedingValues(wordList)
        permutationsLost = calculateDuplicates(wordList)
        rank = calculateRank(inputWord, precedingList, permutationsLost)
        output.write("Rank of " + inputWord + " is: " + str(rank) + '\n')

    else:
        output.write("Error: Word can only contain letters in the alphabet.\n")


#
# Takes an input word as a string, and converts each character to ascii
# and adds it to a list
#
def stringToAsciiList(word):

    wordList = []
    for i in range(0, len(word)):
        currentChar = word[i].upper()
        wordList.append(ord(currentChar))
    return wordList


#
# Takes a list of characters as input, and returns a list contains the number
# of values less then that value to the right in the original list
#
def calcluatePrecedingValues(word):

    precedingList = []
    for i in range(0, len(word)):
        numbersLessThenCurrent = 0
        for x in range(i, len(word)):
            if word[x] < word[i]:
                numbersLessThenCurrent += 1
        precedingList.append(numbersLessThenCurrent)
    return precedingList

#
# Takes a list of characters as input and returns a dictionary
# containing the ascii value and its frequency in the list
#
def characterFrequencies(word):

    characterFrequency = dict()

    for i in range(0, len(word)):
        currentChar = word[i]
        if currentChar in characterFrequency:
            characterFrequency[currentChar] += 1
        else:
            characterFrequency[currentChar] = 1

    return characterFrequency

#
# Takes a list of characters as input, and returns a list containing the
# number of permutations lost by duplications
#
def calculateDuplicates(word):

    permutationsLost = []
    currentValue = 1
    characterFrequency = characterFrequencies(word)

    # currentValue is equal to (number of duplications per letter)!
    for key in characterFrequency:
        if key != 1:
            currentValue *= factorial(characterFrequency[key])

    # next, iterate down the characters and figure out the number of
    # duplications with the [i-1] character removed from the dictionary
    for i in range(0, len(word)):
        currentChar = word[i]
        permutationsLost.append(currentValue)
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
def calculateRank(word, precedingList, duplications):

    rank = 1
    for i in range(0, len(word)):
        rank += float(precedingList[i]) / \
            (float(duplications[i])) * (factorial(len(word) - (i + 1)))
    return int(rank)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "permutationRanking: incorrect usage"
        print "Correct usage is: python permutationRanking.py INPUTWORD\n"
        sys.exit(0)
    readInput(sys.argv)
