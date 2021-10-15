"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example: N = 1, output = {a,e,i,o,u}

Important point: Lexiographically ordered

N = 3
[] [] []
Bucket1 : a,e,i,o,u
Bucket2 : a,e,i,o,u
Bucket 3: a,e,i,o,u


Simple Solution is O(5**N)

for i in range(0,len(vowels)):
	for j in range(i, len(vowels)):
		for k in range(j, len(vowels)):
			print i,j,k

Challenges:
 1. How to dynamically have the for loop for this value of N
    [0 0 0] -> List of size N initialized to 0 0 0
    [0 0 1]
    [0 0 2]
    [0 0 3]
    [0 0 4]
    [0 0 5]
    [0 1 0]
    [0 1 1]

Size of array = N
[
[1,2,3,4,5]
[1,2,3,4,5]
]

Current i Values"
[ 0 0 ]

1 1
2 1
3 1
4 1
5 1
2 2
2 3
2 4
2 5



Assumptions:
 1. The letter can't repeat. That's one letter can occur only once in the entire String
"""

vowels = ['a','e','i','o','u']
output = []
for i in range(0,len(vowels)):
	for j in range(i, len(vowels)):
		output.append(vowels[i]+vowels[j])
print(output)