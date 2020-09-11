import pandas as pd
import car

class Teacher(object):
	def __init__(self, n):
		df = pd.read_csv("data.csv")
		df1=df[df['Small_Name'].str.contains(n, regex=False)]
		self.name=df1.values[0][3]
		self.initial=df1.values[0][1]
		self.room=df1.values[0][5]
		self.email=df1.values[0][6]
		


Mercedes = Teacher('Faisal')

print (Mercedes.name)

M = car.Car('Mercedes', 'S Class', 'Red')

print (M.color)