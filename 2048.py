#2048 game developed in python 3.4.3
from sys import stdout
from random import choice

#function up (in progress)
def upfun(matrix = []):
	print(matrix)

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
		a position wich has 0 value'''
		while(matrix[x1][x2] != 0):
			x1 = choice('0123')
			x2 = choice('0123')
			x1 = int(x1)
			x2 = int(x2)
		matrix[x1][x2] = rand #the final pos receives 0

	'''for loop to check if all the elements in the matrix	are
	different than 0, if so that means the matrix is full
	and the game is over''' 	
	aux = 0 #"aux" variable to help supporting "progress" variable
	for i in range(size):
		for j in range(size):
			if (matrix[i][j] != 0):
				aux += 1

	#prints matrix
	for i in range(size):
		for j in range(size):
			temp = str(matrix[i][j])
			stdout.write(temp)
			stdout.write(' ')
		print('')

	'''if aux equals to 16 that means all 16 elements in the
	matrix are not 0, therefore the game is over, leaves loop'''
	if (aux == 16): 
		break

	#gets command from user
	cmd = input()
	cmd = int(cmd)

	'''executes commands, if command is wrong, it asks the user
	to type a valid command''' 	
	while (cmd != 8 and cmd != 2 and cmd != 4 and cmd != 6):
		if (cmd == 8):
			upfun(matrix)		
		else:
			print("""Wrong command, please type a value either
				8 (up), 2 (down), 4 (left) or 6 (right):""")
			cmd = input()
			cmd = int(cmd)
			
'''by this line the game is over and it asks user if playing 
again or exiting''' 
print('GAME OVER:')
print('1 - try again')
print('2 - exit')
z = input()