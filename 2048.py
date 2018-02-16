#2048 game developed in python 3.4.3
from sys import stdout
from random import choice

#function up (starting soon)
def upfun(matrix = []):
	print(matrix)

size = 4 #matrix 4 x 4
score = 0 #score of the current game
best = 0 #greatest score so far

#creates a 2d matrix with size 4 x 4
matrix = [[0 for x in range(size)] for y in range(size)]

progress = 1

print('Welcome to 2048 game!!!')

#while matrix not full, continue
while (progress == 1):
	print('Score = %d , Best = %d' % (score,best))
	
	#generates either values 2 or 4 to be put in the matrix
	rand = choice('24')
	rand = int(rand)

	'''generates 2 numbers among 0 and 4 to be the space where
	the rand variable goes'''
	x1 = choice('0123')
	x2 = choice('0123')
	x1 = int(x1)
	x2 = int(x2)

	if (matrix[x1][x2] == 0):	
		''''now the matrix in the random position receives the 
		random value either 2 or 4	'''
		matrix[x1][x2] = rand
	else:
		'''keeps randomming a new position till find
		a position which has 0 value'''
		while(matrix[x1][x2] != 0):
			x1 = choice('0123')
			x2 = choice('0123')
			x1 = int(x1)
			x2 = int(x2)
		matrix[x1][x2] = rand #the final pos receives 0

	#prints matrix
	for i in range(size):
		for j in range(size):
			temp = str(matrix[i][j])
			stdout.write(temp)
			stdout.write(' ')
		print('')


	'''for loop to check if all the elements in the matrix	are
	different than 0, if so that means the matrix is full
	and the game is over''' 	
	aux = 0 #"aux" variable to help supporting "progress" variable
	for i in range(size):
		for j in range(size):
			if (matrix[i][j] != 0):
				aux += 1
	

	'''if aux equals to 16 that means all 16 elements in the
	matrix are not 0, therefore the game is over and asks user
	whether playing again or leave'''
	if (aux == 16): 
		print('GAME OVER:')
		print('1 - try again')
		print('2 - exit')
		exit = input()
		exit = int(exit)
		#IN NEED OF DEBUG
		while (exit != 1 and exit != 2):
			if (exit == 1):
				#sets matrix again for new game
				size = 4 #matrix 4 x 4
				score = 0 #score of the current game
				best = 0 #greatest score so far
				#creates a 2d matrix with size 4 x 4
				matrix = [[0 for x in range(size)] for y in range(size)]
				#exit = 0
				print('Welcome to 2048 game!!!')
			elif (exit == 2):
				break
			else:
				print("""Wrong command, please type a value either
						1 (try again) or 2 (exit):""")
				exit = input()
				exit = int(exit)

	else:
		#gets command from user
		cmd = input()
		cmd = int(cmd)

		'''executes commands, if command is wrong, it asks the user
		to type a valid command''' 	
		while (cmd != 8 and cmd != 2 and cmd != 4 and cmd != 6):
			if (cmd == 8): #IN NEED OF DEBUG
				upfun(matrix)
				print('teste')		
			else:
				print("""Wrong command, please type a value either
					8 (up), 2 (down), 4 (left) or 6 (right):""")
				cmd = input()
				cmd = int(cmd)