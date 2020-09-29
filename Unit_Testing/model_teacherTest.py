import unittest
import model_teacher


class TestTeacher(unittest.TestCase):
	
	def testinformation(self):

		a=model_teacher.information("Faisal")
		self.assertIsNotNone(a)

		b=model_teacher.information("Arif")
		self.assertIsNotNone(b)







if __name__ == "__main__":
	unittest.main()