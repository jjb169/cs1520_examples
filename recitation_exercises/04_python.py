'''
Your task for this exercise is to complete the code for the class below.
You'll start by reading the file '04_graph.txt' and storing it as a dict, 
you can also lookup what a defaultdict is and use that instead.


A line in the '04_graph.txt' represents a friends relation. For example,
the line a;d in the txt file means that person a is friends with
person d or person d is a friend of person a (notice how this
edge is undirected). Look at the example below for clarification.


04_graph.txt
---------
a;b
b;c
---------


your dictionary (key:values) must look like this when printed
{
('a', ['b'])
('b', ['a', 'c'])
('c', ['b'])
}
You also have to complete the code for the other methods defined below
'''

from collections import defaultdict

class Graph():
	def __init__(self, file_path):
		'''
		file_path is the path to the 04_graph.txt file
		'''
		#open the file with a reader
		file = open(file_path, "r")
		
		#create an empty dict to start
		self.dict = {};
		
		#loop over the file and populate dict
		for line in file:
			line = line.strip()
			#print(line.strip())
			pair = line.split(';')
			#print(pair)
			#if the key value already exists, add a space and the next value
			if pair[0] in self.dict:
				self.dict[pair[0]] = (self.dict.get(pair[0]) + " " + pair[1])
			#if the key does not exist, add it and assign the corresponding value
			else: 
				self.dict[pair[0]] = pair[1]
				
			
		print(self.dict)
		pass


	def __str__(self):
		'''
		print the dictionary as described in the example above.
		It should be sorted by keys and each the values must 
		also appear in sorted order. Try doing this using list 
		comprehension and lambda expressions.
		'''
		pass

	def __iter__(self):
		'''
		write an iter method that returns an iter to the graph
		successively calling next on this iter  will print out
		the nodes of the graph in sorted order.
		'''
		pass


	def __next__(self):
		pass


	def isConnected(self, person1, person2):
		'''
		This arguments of this fucntion are two people and it returns a boolean
		whether those two people are conencted in the graph or not.

		Hint: try to use some search technique, this shuold take around 10-15 lines of code
		'''


if __name__ == "__main__":
	filePath = "04_graph.txt" # enter input file path here
	g = Graph(filePath)

	print("---------Testing __str__ ---------")
	print(str(g) == "{\n('a', ['c', 'd'])\n('b', ['c', 'e', 'f'])\n('c', ['a', 'b', 'g'])\n('d', ['a', 'e'])\n('e', ['b', 'd'])\n('f', ['b'])\n('g', ['c'])\n('i', ['j', 'k'])\n('j', ['i'])\n('k', ['i'])\n}")



	print("---------Testing __iter__ and __next__ ---------")
	keys = [k for k in g]
	print(keys)
	print(keys == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k'])


	print("---------Testing isConnected ---------")
	connectivity = [g.isConnected('a', 'e'), g.isConnected('g', 'd'), g.isConnected('e', 'i')]
	print(connectivity == [True, True, False])

