class Car(object):
    condition = 'New'
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        self.condition = 'Used'

Mercedes = Car('Mercedes', 'S Class', 'Red')

print (Mercedes.color)


'''from subprocess import call

class CallPy(object):
	def __init___(self, path="Teacher.py"):
		self.path=path
		pass
	def call_python_file(self):
		call(["Python3", "{}".format(self.path)])

if __name__ == "__main__":
	c = CallPy()
	c.call_python_file()'''
