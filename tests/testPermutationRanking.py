import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from permutationRanking import stringToAsciiList
from permutationRanking import calcluatePrecedingValues
from permutationRanking import characterFrequencies

class TestPermutationRanking(unittest.TestCase):

	
	def teststringToAsciiList(self):
		inputWord = "ABCDEFGHIJKLMNOPQRSTUVWXY"
		inputWordReverse = "YXWVUTSRQPONMLKJIHGFEDCBA"
		inputWordLowerCase = "abcdefghijklmnopqrstuvwxy"

		outputWord = stringToAsciiList(inputWord)
		outputWordReverse = stringToAsciiList(inputWordReverse)
		outputWordLowerCase = stringToAsciiList(inputWordLowerCase)

		for i in range(0,len(outputWord)):
			self.assertEqual(outputWord[i], outputWordReverse[len(outputWord) - i -1])
			self.assertEqual(i,outputWord[i]-65)
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
			self.assertEqual(len(minimumList)-i-1, maximumList[i])


	def testCharacterFrequencies(self):

		inputWordSingle = "ABCDEFGHIJKLMNOPQRSTUVWXY"
		inputWordDouble = "AABBCCDDEEFFGGHHIIJJKKLL"
		inputWordIncrease = "ABBCCCDDDDEEEEEFFFFFF"

		outputWordSingle = stringToAsciiList(inputWordSingle)
		outputWordDouble = stringToAsciiList(inputWordDouble)
		outputWordIncrease= stringToAsciiList(inputWordIncrease)

		dictSingle = characterFrequencies(outputWordSingle)
		dictDouble = characterFrequencies(outputWordDouble)	
		dictIncrease= characterFrequencies(outputWordIncrease)

		for key in dictSingle:
			self.assertEqual(1,dictSingle[key])
		for key in dictDouble:
			self.assertEqual(2, dictDouble[key])

		self.assertEqual(1, dictIncrease[65])
		self.assertEqual(2, dictIncrease[66])
		self.assertEqual(3, dictIncrease[67])
		self.assertEqual(4, dictIncrease[68])
		self.assertEqual(5, dictIncrease[69])
		self.assertEqual(6, dictIncrease[70])
			


if __name__ == '__main__':
    unittest.main()