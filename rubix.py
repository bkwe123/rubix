import copy

class rubixCube():
	def __init__(self):
		self.up = [[None, None, None], [None, None, None], [None, None, None]]
		self.down = [[None, None, None], [None, None, None], [None, None, None]]
		self.left = [[None, None, None], [None, None, None], [None, None, None]]
		self.right = [[None, None, None], [None, None, None], [None, None, None]]
		self.front = [[None, None, None], [None, None, None], [None, None, None]]
		self.back = [[None, None, None], [None, None, None], [None, None, None]]
		
	def __repr__(self):
		cube = ""
		for i in range(len(self.up)):
			cube += "   "
			for square in self.up[i]:
				cube += square
			cube += '\n'
		for i in range(len(self.front)):
			for square in self.left[i]:
				cube += square
			for square in self.front[i]:
				cube += square
			for square in self.right[i]:
				cube += square
			for square in self.back[i]:
				cube += square
			cube += '\n'
		for i in range(len(self.down)):
			cube += "   "
			for square in self.down[i]:
				cube += square
			cube += '\n'
		return cube
		
	'''turns top layer clockwise'''
	def turnUp(self) -> str:
		face = copy.deepcopy(self.up)
		frontEdges = self.front[0].copy()
		for i in range(len(self.front[0])):
			self.front[0][i] = self.right[0][i]
			self.right[0][i] = self.back[0][i]
			self.back[0][i] = self.left[0][i]
			self.left[0][i] = frontEdges[i]
		for i in range(len(self.up)):
			self.up[i][2] = face[0][i]
		for i in range(len(self.up)):
			self.up[i][1] = face[1][i]
		for i in range(len(self.up)):
			self.up[i][0] = face[2][i]
		return 'U'
	'''turns top layer counter clockwise'''
	def turnUpPrime(self) -> str:
		self.turnUp()
		self.turnUp()
		self.turnUp()
		return 'U\''
	
	def turnDown(self) -> str:
		face = copy.deepcopy(self.down)
		frontEdges = self.front[2].copy()
		print(frontEdges)
		for i in range(len(self.front[2])):
			self.front[2][i] = self.left[2][i]
			self.left[2][i] = self.back[2][i]
			self.back[2][i] = self.right[2][i]
			self.right[2][i] = frontEdges[i]
		for i in range(len(self.down)):
			self.down[i][2] = face[0][i]
		for i in range(len(self.down)):
			self.down[i][1] = face[1][i]
		for i in range(len(self.down)):
			self.down[i][0] = face[2][i]
		return 'D'
	
	def turnDownPrime(self) -> str:
		self.turnDown()
		self.turnDown()
		self.turnDown()
		return 'D\''
	
	#TODO:	
	'''
	-turnRight/turnRightPrime
	-turnLeft/turnLeftPrime
	-turnFront/...
	-turnBack/...
	'''
	
if __name__ == "__main__":
	cube = rubixCube()
	'''Set faces to numbers for debugging/testing: cube.face[i][j] = str(3*i + j)'''
	for i in range(len(cube.up)):
		for j in range(len(cube.up[i])):
			cube.up[i][j] = 'y'
			
	for i in range(len(cube.down)):
		for j in range(len(cube.down[i])):
			#cube.down[i][j] = 'w'
			cube.down[i][j] = str(3*i + j)
			
	for i in range(len(cube.front)):
		for j in range(len(cube.front[i])):
			cube.front[i][j] = 'r'
			
	for i in range(len(cube.back)):
		for j in range(len(cube.back[i])):
			cube.back[i][j] = 'o'
			
	for i in range(len(cube.left)):
		for j in range(len(cube.left[i])):
			cube.left[i][j] = 'b'
			
	for i in range(len(cube.right)):
		for j in range(len(cube.right[i])):
			cube.right[i][j] = 'g'
			
	print(cube)
	print(cube.turnDown())
	print(cube)
