import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from permutationRanking import readInput
from permutationRanking import stringToAsciiList
from permutationRanking import calcluatePrecedingValues
from permutationRanking import characterFrequencies
from permutationRanking import calculateDuplicates
from permutationRanking import calculateRank
from StringIO import StringIO


class TestPermutationRanking(unittest.TestCase):

    def testReadInput(self):
        testWord = ["permutationRanking", "ABAB"]
        testWord2 = ["permutationRanking", "AAAB"]
        testWord3 = ["permutationRanking", "BAAA"]
        testWord4 = ["permutationRanking", "QUESTION"]
        testWord5 = ["permutationRanking", "BOOKkeeper"]
        testWordError = ["permutationRanking", "123452!@#%"]

        output = StringIO()
        readInput(testWord, output=output)
        self.assertEqual(
            output.getvalue(), "Rank of " + testWord[1] + " is: 2\n")

        output2 = StringIO()
        readInput(testWord2, output=output2)
        self.assertEqual(
            output2.getvalue(), "Rank of " + testWord2[1] + " is: 1\n")

        output3 = StringIO()
        readInput(testWord3, output=output3)
        self.assertEqual(
            output3.getvalue(), "Rank of " + testWord3[1] + " is: 4\n")

        output4 = StringIO()
        readInput(testWord4, output=output4)
        self.assertEqual(
            output4.getvalue(), "Rank of " + testWord4[1] + " is: 24572\n")

        output5 = StringIO()
        readInput(testWord5, output=output5)
        self.assertEqual(
            output5.getvalue(), "Rank of " + testWord5[1] + " is: 10743\n")

        output6 = StringIO()
        readInput(testWordError, output=output6)
        self.assertEqual(
            output6.getvalue(),
            "Error: Word can only contain letters in the alphabet.\n")

    def teststringToAsciiList(self):
        inputWord = "ABCDEFGHIJKLMNOPQRSTUVWXY"
        inputWordReverse = "YXWVUTSRQPONMLKJIHGFEDCBA"
        inputWordLowerCase = "abcdefghijklmnopqrstuvwxy"

        outputWord = stringToAsciiList(inputWord)
        outputWordReverse = stringToAsciiList(inputWordReverse)
        outputWordLowerCase = stringToAsciiList(inputWordLowerCase)

        for i in range(0, len(outputWord)):
            self.assertEqual(
                outputWord[i], outputWordReverse[len(outputWord) - i - 1])
            self.assertEqual(i, outputWord[i] - 65)
            self.assertEqual(outputWord[i], outputWordLowerCase[i])

        lowerCaseWord = "abcdefghijklmnopqrstuvwxy"

    def testcalcluatePrecedingValues(self):
        inputWord = "ABCDEFGHIJKLMNOPQRSTUVWXY"
        inputWordReverse = "YXWVUTSRQPONMLKJIHGFEDCBA"

        outputWord = stringToAsciiList(inputWord)
        outputWordReverse = stringToAsciiList(inputWordReverse)

        minimumList = calcluatePrecedingValues(outputWord)
        maximumList = calcluatePrecedingValues(outputWordReverse)

        for i in range(0, len(minimumList)):
            self.assertEqual(0, minimumList[i])
            self.assertEqual(len(minimumList) - i - 1, maximumList[i])

    def testCharacterFrequencies(self):

        inputWordSingle = "ABCDEFGHIJKLMNOPQRSTUVWXY"
        inputWordDouble = "AABBCCDDEEFFGGHHIIJJKKLL"
        inputWordIncrease = "ABBCCCDDDDEEEEEFFFFFF"

        outputWordSingle = stringToAsciiList(inputWordSingle)
        outputWordDouble = stringToAsciiList(inputWordDouble)
        outputWordIncrease = stringToAsciiList(inputWordIncrease)

        dictSingle = characterFrequencies(outputWordSingle)
        dictDouble = characterFrequencies(outputWordDouble)
        dictIncrease = characterFrequencies(outputWordIncrease)

        for key in dictSingle:
            self.assertEqual(1, dictSingle[key])
        for key in dictDouble:
            self.assertEqual(2, dictDouble[key])

        self.assertEqual(1, dictIncrease[65])
        self.assertEqual(2, dictIncrease[66])
        self.assertEqual(3, dictIncrease[67])
        self.assertEqual(4, dictIncrease[68])
        self.assertEqual(5, dictIncrease[69])
        self.assertEqual(6, dictIncrease[70])

    def testCalculateDuplicates(self):

        testWord = "ABAB"
        testWord2 = "AAAB"
        testWord3 = "BAAA"
        testWord4 = "QUESTION"
        testWord5 = "BOOKkeeper"
        testWord6 = "ENGINEERING"

        wordList = stringToAsciiList(testWord)
        wordList2 = stringToAsciiList(testWord2)
        wordList3 = stringToAsciiList(testWord3)
        wordList4 = stringToAsciiList(testWord4)
        wordList5 = stringToAsciiList(testWord5)
        wordList6 = stringToAsciiList(testWord6)

        dictABAB = [4, 2, 1, 1]
        dictAAAB = [6, 2, 1, 1]
        dictBAAA = [6, 6, 2, 1]
        dictQUESTION = [1, 1, 1, 1, 1, 1, 1, 1]
        dictBOOKEEPER = [24, 24, 12, 12, 6, 6, 2, 1, 1, 1]
        dictENGINEERING = [144, 48, 16, 8, 4, 2, 1, 1, 1, 1, 1]

        self.assertEqual(calculateDuplicates(wordList), dictABAB)
        self.assertEqual(calculateDuplicates(wordList2), dictAAAB)
        self.assertEqual(calculateDuplicates(wordList3), dictBAAA)
        self.assertEqual(calculateDuplicates(wordList4), dictQUESTION)
        self.assertEqual(calculateDuplicates(wordList5), dictBOOKEEPER)
        self.assertEqual(calculateDuplicates(wordList6), dictENGINEERING)

    def testCalculateRank(self):
        testWord = "ABAB"
        testWord2 = "AAAB"
        testWord3 = "BAAA"
        testWord4 = "QUESTION"
        testWord5 = "BOOKkeeper"
        testWord6 = "ENGINEERING"

        wordList = stringToAsciiList(testWord)
        wordList2 = stringToAsciiList(testWord2)
        wordList3 = stringToAsciiList(testWord3)
        wordList4 = stringToAsciiList(testWord4)
        wordList5 = stringToAsciiList(testWord5)
        wordList6 = stringToAsciiList(testWord6)

        precedingList = calcluatePrecedingValues(wordList)
        precedingList2 = calcluatePrecedingValues(wordList2)
        precedingList3 = calcluatePrecedingValues(wordList3)
        precedingList4 = calcluatePrecedingValues(wordList4)
        precedingList5 = calcluatePrecedingValues(wordList5)
        precedingList6 = calcluatePrecedingValues(wordList6)

        permutationsLost = calculateDuplicates(wordList)
        permutationsLost2 = calculateDuplicates(wordList2)
        permutationsLost3 = calculateDuplicates(wordList3)
        permutationsLost4 = calculateDuplicates(wordList4)
        permutationsLost5 = calculateDuplicates(wordList5)
        permutationsLost6 = calculateDuplicates(wordList6)

        self.assertEqual(
            calculateRank(testWord, precedingList, permutationsLost), 2)
        self.assertEqual(
            calculateRank(testWord2, precedingList2, permutationsLost2), 1)
        self.assertEqual(
            calculateRank(testWord3, precedingList3, permutationsLost3), 4)
        self.assertEqual(
            calculateRank(testWord4, precedingList4, permutationsLost4), 24572)
        self.assertEqual(
            calculateRank(testWord5, precedingList5, permutationsLost5), 10743)
        self.assertEqual(
            calculateRank(testWord6, precedingList6, permutationsLost6), 53032)

if __name__ == '__main__':
    unittest.main()
