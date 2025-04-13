# Python code​​​​​​‌‌​‌​​‌​​​‌​​‌​‌​‌​‌​​​‌​ below
class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):
		num_chars = 2 * i+1
		total_width = 2* self.height -1
		#centering it
		spaces = (total_width - num_chars) //2
		print(' ' * spaces + self.printChar * num_chars + ' ' * spaces)