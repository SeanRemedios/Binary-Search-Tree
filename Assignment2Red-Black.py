'''
Sean Remedios - 14sr84 - 10190433
“I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.”
'''

'''
Red-Black Vertex Implementation
RBTreeVertex - Holds the attributes for each node
RBSearchTree - Holds the root and size attribute and the methods to manipulate the tree
'''

from Assignment2 import BinaryTreeVertex, BinarySearchTree
import copy
import random
import time

# Used to count the number of rotations. If it was used as a class attribute, it wasn't keeping track
# of the count properly
countRotations = 0 # Use keyword 'global' <variable> at the start of a function to reference the global variable

class RBTreeVertex:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
		self.size = 1 # The depth of the node
		self.isRed = True # Red is True, Black is False

class RBSearchTree:
	def __init__(self):
		self.root = None # Root of the tree
		self.size = 0

	'''
	Function inserts a node into the tree and makes rotations and colour flips to maintain the balanace of the tree.
	Input:	root: The root (or vertex) of the tree (or subtree)
			val: A value to be inserted
	Output:	root: The root (or vertex) of the tree (or subtree)
	'''
	def insertTo(self, root, val):
		if not root:
			return RBTreeVertex(val) # Create a new node at the root
		else:
			self.size += 1 # Increases the depth of the tree
			if (val > root.val):
				root.right = self.insertTo(root.right, val) # Move down the right side of the tree
				if (root.isRed):
			 		pass
				elif (root.right is not None and root.right.right is not None and root.right.left is not None and root):
				 	if (root.right.isRed):
				 		if (root.right.right.isRed):
				 			return self.RB_right_right_fix(root) # Fix the right, right child
				 		elif (root.right.left.isRed and root.left is not None):
				 			return self.RB_right_left_fix(root) # Fix the right, left child
			else:
				root.left = self.insertTo(root.left, val) # Move down the left side of the tree
				if (root.isRed):
				 	pass
				elif (root.left is not None and root.left.left is not None and root.left.right is not None and root):
				 	if (root.left.isRed):
				 		if (root.left.left.isRed):
				 			return self.RB_left_left_fix(root) # Fix the left, left child
				 		elif (root.left.right.isRed and root.right is not None):
					 		return self.RB_left_right_fix(root) # Fix the left, right child
		return root

	'''
	Function calls the insert function with the root and value.
	Input:	val: A value to be inserted
	'''
	def insert(self, val):
		self.root = self.insertTo(self.root, val)
		if (self.root is not None):
			self.root.isRed = False # Turn the root black

	'''
	Function fixes the right right child if it is red.
	Input:	current: The current root of the subtree
	Output: current/child: The fixed child of the subtree
	'''
	def RB_right_right_fix(self, current):
		global countRotations 
		countRotations += 1
		child = current.right
		sib = current.left
		if (sib is not None):
			# No rotation, recolour and return
			if (sib.isRed):
				child.isRed = False
				sib.isRed = False
				current.isRed = True
				return current
		else:
			# Single rotation
			current.right = child.left
			child.left = current
			child.isRed = False
			current.isRed = True
			return child

	'''
	Function fixes the right left child if it is red.
	Input:	current: The current root of the subtree
	Output: current/child: The fixed child of the subtree
	'''
	def RB_right_left_fix(self, current):
		global countRotations
		countRotations += 1
		child = current.right
		sib = current.left
		if (sib.isRed):
			# No rotation
			child.isRed = False
			sib.isRed = False
			current.isRed = True
			return current
		else:
			# Double rotation
			grandchild = child.left
			child.left = grandchild.right
			current.right = grandchild.left
			grandchild.left = current
			grandchild.right = child
			grandchild.isRed = False
			current.isRed = True
			return grandchild

	'''
	Function fixes the left left child if it is red.
	Input:	current: The current root of the subtree
	Output: current/child: The fixed child of the subtree
	'''
	def RB_left_left_fix(self, current):
		global countRotations
		countRotations += 1
		child = current.left
		sib = current.right
		if (sib is not None):
			# No rotation
			if (sib.isRed):
				child.isRed = False
				sib.isRed = False
				current.isRed = True
				return current
		else:
			# Single rotation
			current.left = child.right
			child.right = current
			child.isRed = False
			current.isRed = True
			return child

	'''
	Function fixes the left right child if it is red.
	Input:	current: The current root of the subtree
	Output: current/child: The fixed child of the subtree
	'''
	def RB_left_right_fix(self, current):
		global countRotations
		countRotations += 1
		child = current.left
		sib = current.right
		if (sib.isRed):
			# No rotation
			child.isRed = False
			sib.isRed = False
			current.isRed = True
			return current
		else:
			# Double rotation
			grandchild = child.right
			child.right = grandchild.left
			current.left = grandchild.right
			grandchild.right = current
			grandchild.left = child
			grandchild.isRed = False
			current.isRed = True
			return grandchild

	'''
	Function searches the tree for a particular value and keeps track of the nodes that
	were visited.
	Input:	val: A value to be searched
			visited: A list that keeps track of the nodes that were visited
			root: The current root of the tree (or subtree)
	Output:	visited: A list that keeps track of the nodes that were visited
	'''
	def SearchPath(self, val, visited, root):
		if (self.root == None or root == None):
			del visited[:] # Reached an empty node, value wasn't found
			return visited
		elif (root.val == val):
			visited.append(val) # Value found
			return visited
		elif (root.val > val):
			visited.append(root.val) # Searches the left subtree
			return self.SearchPath(val, visited, root.left)
		else:
			visited.append(root.val) # Searches the right subtree
			return self.SearchPath(val, visited, root.right)

	'''
	Function calls the _printTree function.
	'''
	def printTree(self):
		if(self.root != None):
			self._printTree(self.root)

	'''
	Function prints the tree. Each node's value and it's colour is printed.
	Input:	node: A node to be printed
	'''
	def _printTree(self, node):
		if(node != None):
			self._printTree(node.left) # Moves down the left subtree
			print (str(node.val) + ' ', str(node.isRed))
			self._printTree(node.right) # Moves down the right subtree

	'''
	Function returns the total depth of the tree
	'''
	def Total_Depth(self):
		return self.size

'''
Main function for Experiment #1
'''
# def main():
# 	global countRotations
# 	Tree = RBSearchTree() # Creates an instant of the RBSearchTree class
# 	checkpointAvg = [0]*10
# 	for i in range(0, 500): # Creates 500 trees
# 		count = 0 # Keeps track of how many values have been added to the tree
# 		arr = random.sample(range(1, 1001), 1000) # Generates 1000 random numbers between 1 and 1000
# 		for val in arr:
# 			if (count % 100 == 0 and count is not 0):
# 				index = (int(str(count)[0])) - 1 # Gets the first digit of the checkpoint to use as an index
# 				checkpointAvg[index] += countRotations
# 				countRotations = 0 # Global variable is reset to 0
# 			Tree.insert(val)
# 			count += 1
# 		checkpointAvg[9] += countRotations
# 		countRotations = 0
# 	j = 0
# 	print(checkpointAvg)
# 	print("Checkpoint:			Average Number of Rotations:")
# 	for numRots in checkpointAvg:
# 		checkpointAvg[j] = numRots/500 # Gets the average number of rotations per checkpoint
# 		print ("   " + str((j+1)*100) + "					  " + str(checkpointAvg[j]))
# 		j += 1
# 	print(checkpointAvg)

'''
Main function for Experiment #2
'''
def main():
	AvgR = []
	for n in [1000, 2000, 4000, 8000, 16000]:
		RforN = []
		BSTDepth = 0
		RBDepth = 0
		count = 0
		for i in range(0, 500): # Creates 500 trees
			RBTree = RBSearchTree()
			BSTree = BinarySearchTree()
			arr = random.sample(range(1, n+1), 1000)
			for val in arr:
				BSTree.insertBST(val, BSTree.root)
			#if (count % 50 == 0): # Just makes sure values are being added properly
			#	print("Checkpoint for", n, "on", count) 
			for val in arr:
				RBTree.insert(val)
			count += 1
			BSTDepth = BSTree.Total_DepthBST()
			RBDepth = RBTree.Total_Depth()
			RforN.append(BSTDepth/RBDepth) # Gets the ratio of BST total depth to RB total depth per tree
		AvgR.append(copy.deepcopy(RforN)) # Appends a copy of the ratio list to the average list
		del RforN[:] # Clear the ratio list to be used for the next value of n
		BSTDepth = 0
		RBDepth = 0
		#print("--- %s seconds ---" % (time.time() - start_time)) #Checks how long it took to complete n values
	percentN = []
	for n in AvgR:
		# Dictionary to hold the number of ratios that fall into each bin
		BucketDict = {'<0.5':0, '0.5<= <0.75':0, '0.75<= <=1.25':0, '1.25< <= 1.5':0, '>1.5':0}
		for R in n:
			if (R < 0.5):
				BucketDict['<0.5'] += 1
			elif (0.5 <= R and R < 0.75):
				BucketDict['0.5<= <0.75'] += 1
			elif (0.75<= R <=1.25):
				BucketDict['0.75<= <=1.25'] += 1
			elif (1.25< R <= 1.5):
				BucketDict['1.25< <= 1.5'] += 1
			elif (R >1.5):
				BucketDict['>1.5'] += 1
		temp = []
		for v in BucketDict.values():
			temp.append(v/500) # Gets the percentage for each bin
		percentN.append(copy.deepcopy(temp))
		BucketDict.clear() # Clears the dictionary
		del temp[:]
	print (percentN)

#start_time = time.time() # Gets the start time of the program to see how long it takes
main()
#print("---Total %s seconds ---" % (time.time() - start_time))










