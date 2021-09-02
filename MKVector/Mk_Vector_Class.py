import math
import numpy as np

class Vector2:
	def calc_angle(self):
		self.d = math.sqrt(self.x**2 + self.y**2)
		xv = 1
		yv = 0

		dot = self.x*xv + self.y*yv
		cross = self.x*yv + self.y*xv

		self.angle = math.atan2(abs(cross),dot)

		if cross<0:
			self.angle = math.radians(360-math.degrees(self.angle))


	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.d = math.sqrt(self.x**2 + y**2)
#		self.angle = 0
		
		self.calc_angle()

	def add(self,vector):
		self.calc_angle()	

		self.x = self.x + vector.x
		self.y = self.y + vector.y

		self.d = math.sqrt((self.x-0)**2 + (self.y-0)**2)
		self.adjacent = math.sqrt((self.x - 0)**2 + (0 - 0)**2)
		
		self.calc_angle()

	def sub(self,vector):
		self.calc_angle()

		self.x = self.x - vector.x
		self.y = self.y - vector.y

		self.d = math.sqrt((self.x-0)**2 + (self.y-0)**2)
		self.adjacent = math.sqrt((self.x - 0)**2 + (0 - 0)**2)
		
		self.calc_angle()

	def mult(self,scalar):
		self.calc_angle()

		
		if self.x != 0:
			self.x = (self.d * scalar) * math.cos(self.angle)
			self.y = (self.d * scalar) * math.sin(self.angle)

			self.d = math.sqrt((self.x-0)**2 + (self.y-0)**2)
			self.adjacent = math.sqrt((self.x - 0)**2 + (0 - 0)**2)
		else:
			self.x = self.x
			self.y = self.y * scalar

		
		self.calc_angle()

	def div(self,scalar):
		self.calc_angle()

		if self.x != 0:
			self.x = (self.d / scalar) * math.cos(self.angle)
			self.y = (self.d / scalar) * math.sin(self.angle)

			self.d = math.sqrt((self.x-0)**2 + (self.y-0)**2)
			self.adjacent = math.sqrt((self.x - 0)**2 + (0 - 0)**2)
		else:
			self.x = self.x
			self.y = self.y / scalar
	def normalize(self):
		self.calc_angle()
		
		self.x = self.x/self.d
		self.y = self.y/self.d
		
		self.calc_angle()

def sub_vectors(vector1,vector2):
	x = vector1.x - vector2.x
	y = vector1.y - vector2.y

	newVector = Vector2(x,y)
	return newVector

def add_vectors(vector1,vector2):
	x = vector1.x + vector2.x
	y = vector1.y + vector2.y

	newVector = Vector2(x,y)
	return newVector