class Shape:

	description = "Simple Quadrilaterals"
	author = "Brooks Lybrand"

	def __init__(self, length, width):
		self.x = length
		self.y = width

	def area(self):
		return self.x*self.y

	def perimeter(self):
		return 2*self.x + 2*self.y

class Square(Shape):

	def __init__(self, side):
		self.x = side
		self.y = side

def main():

	myRectangle = Shape(20, 30)
	print(myRectangle.description)
	print(myRectangle.author)
	print(myRectangle.area())
	print(myRectangle.perimeter())

	mySquare = Square(10)
	print(mySquare.description)
	print(mySquare.author)
	print(mySquare.area())
	print(mySquare.perimeter())

if __name__ == "__main__":
	main()