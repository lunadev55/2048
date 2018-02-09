#2048 game developed in python 3.4.3
import sys

size = 4 #size of the matrix of the game
score = 0 #score in the current game 
best = 0 #highest score obtained so far

#making the 4 x 4 matrix and setting all elements to 0
matrix = [[0 for x in range(size)] for y in range(size)]

'''
bool var to check if player is able to play next,
and aux var to support it 
'''
progress = 1  
aux = 0

'''
for loop to check if all the elements in the matrix	are
different than 0, if so that means the matrix is full
and the game is over
''' 
for i in range(size):
	for j in range(size):
		if (matrix[i][j] != 0):
			aux += 1

'''
if aux equals to 16 that means all 16 elements in the
matrix are not 0, therefore the game is over 
'''
if (aux == 16): 
	#progress equals 0 and player cant continue
	progress = 0 

#printing matrix for testing
for i in range(size):
	for j in range(size):
		temp = str(matrix[i][j])
		sys.stdout.write(temp)
		sys.stdout.write(' ')
	print('')
		