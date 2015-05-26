# Permutation Ranking

Calculates the alphabetical ranking of a given string compared to all other permutations.

## Steps:

1. Convert letters to ascii value

2. Iterate over, figure out how many ascii values are lower than 
   the current value(including duplicates)
   EX. BAAA = [66,65,65,65] = [3,0,0,0]

3. While iterating, calculate the production
   of the factorial of all duplicates
   EX. BAAA (current is B) = (# of A's)! * (# of B's)! = 3! * 1! = 6

4. Factor out the number of duplicates, by dividing the number found in 2, 
   by the number found in 3
   EX. BAAA = [3,0,0,0](found 2), and [6,2,1,1](from 3)
            = 3/6, 0/2, 0/1, 0/1 = [1/2,0,0,0]

5. Find the total number of permutations p, of the current letter.
   EX. BAAA = [3!,2!,1!,0!]

6. The rank is equal to the summation of (value from 4 * value from 5) + 1
   EX. BAAA = (1/2 * 3!) + (0 * 2!) + (0 * 1!) + (0 * 0!) + 1
            = 2 + 0 + 0 + 0 + 1 = 3


## Usage:

Correct usage is: python permutationRanking.py WordToFindRankingOf


