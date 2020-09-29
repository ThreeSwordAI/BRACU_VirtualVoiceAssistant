import pandas as pd

def information(faculty):
	s = faculty
	if "sir" in s:
		s=s.replace('sir', '')
		s=s.replace(' ', '')
	elif "miss" in s:
		s=s.replace('sir', '')
		s=s.replace(' ', '')
		#print("model_teacher")
	df = pd.read_csv("data.csv")
	df1=df[df['Small_Name'].str.contains(s, regex=False)]

	return df1


class Model_teacher(object):
	def __init__(self, faculty):
		df1 = information(faculty)
		self.name=df1.values[0][3]
		self.initial=df1.values[0][1]
		self.room=df1.values[0][5]
		self.email=df1.values[0][6]
		#print("model_teacher2")