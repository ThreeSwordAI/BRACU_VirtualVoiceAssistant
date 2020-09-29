import unittest
import controll


class TestControl(unittest.TestCase):
	
	def testfacultyinfo(self):

		controll.facultyinfo("Arif")



	def testeventinfo(self):
		controll.eventinfo()

	def testcallsearch(self):
		controll.callsearch("BUX")

		






if __name__ == "__main__":
	unittest.main()