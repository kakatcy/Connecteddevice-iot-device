import unittest
from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask

"""
Test class for all requisite Module01 functionality.

Instructions:
1) Rename 'testSomething()' function such that 'Something' is specific to your needs; add others as needed, beginning each function with 'test...()'.
2) Import the relevant modules and classes to support your tests.
3) Run this class as unit test app
4) Include a screen shot of the report when you submit your assignment
"""
class Module01Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass
	
	"""
	Place your comments describing the test here.
	"""
	def testCpurate(self):
		cpurate = SystemCpuUtilTask.getDataFromSensor(self)
		assert cpurate>0.0 and cpurate<100.0
	
	def testMemrate(self):
		memrate = SystemMemUtilTask.getDataFromSensor(self)
		assert memrate>0.0 and memrate<100.0
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()