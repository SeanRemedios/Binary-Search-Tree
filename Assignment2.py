'''
Sean Remedios - 14sr84 - 10190433
“I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.”
'''

import random

class BinaryTreeVertex:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0 
		# Keeps track of the depth of the tree, each level is one more than the last.
		# A tree of:
		#				6
		#			3	    10
		#				  8   20
		# Will have a depth of 6. 0 for the root, 1 for '3', 1 for '10', 2 for '8' and
		# 2 for '20'. Which is 0+1+1+2+2=6
		# The children's depth is calculated by adding one to the parent's to the size
	def insertBST(self, val, root):
		if (self.root == None or root == None):
			self.root = BinaryTreeVertex(val)
		else:
			self.size += 1 # Adds one to the depth of the tree
			if (val < root.value):
				if (root.left != None):
					self.insertBST(val, root.left)
				else:
					root.left = BinaryTreeVertex(val)
			else:
				if(root.right != None):
					self.insertBST(val, root.right)
				else:
					root.right = BinaryTreeVertex(val)

	def SearchPath(self, val, visited, root):
		if (self.root == None or root == None):
			del visited[:]
			return visited
		elif (root.value == val):
			visited.append(val)
			return visited
		elif (root.value > val):
			visited.append(root.value)
			return self.SearchPath(val, visited, root.left)
		else:
			visited.append(root.value)
			return self.SearchPath(val, visited, root.right)

	def Total_DepthBST(self):
		return self.size

	def printTree(self):
		if(self.root != None):
			self._printTree(self.root)

	def _printTree(self, node):
		if(node != None):
			self._printTree(node.left)
			print (str(node.value) + ' ')
			self._printTree(node.right)

def main():
	BSTree = BinarySearchTree()
	count = 0
	for i in range(0, 400):
		arr = random.sample(range(1, 16000+1), 1000)
		for val in arr:
			BSTree.insertBST(val, BSTree.root)
			count += 1
		if (count % 50 == 0):
			print("Checkpoint")
		count += 1 
		#print(BSTree.Total_DepthBST())
	return None


	arr = [6, 10, 20, 8, 3, 23, 25]
	for i in arr:
		Tree.insertBST(i, Tree.root)
	Tree.printTree()
	visited = []
	Tree.SearchPath(8, visited, Tree.root)
	print(visited)
	size = Tree.Total_DepthBST()
	print(size)
#main()