import unittest
import model_calendar


class TestCalendar(unittest.TestCase):
	
	def testAuthentication(self):
		ser = model_calendar.authentication_google()
		self.assertIsNotNone(ser)

		ser = model_calendar.authentication_google()
		self.assertIsNotNone(ser)


		ser = model_calendar.authentication_google()
		self.assertIsNotNone(ser)


	def testService(self):
		ser = model_calendar.authentication_google()
		event = model_calendar.get_service(2, ser)
		self.assertIsNotNone(event)

		ser = model_calendar.authentication_google()
		event = model_calendar.get_service(2, ser)
		self.assertIsNotNone(event)

		ser = model_calendar.authentication_google()
		event = model_calendar.get_service(2, ser)
		self.assertIsNotNone(event)



if __name__ == "__main__":
	unittest.main()