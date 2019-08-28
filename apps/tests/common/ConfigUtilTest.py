'''
Created on Aug 28, 2019

@author: aking
'''
import unittest

from labbenchstudios.common.ConfigUtil import ConfigUtil

"""
Test class for the ConfigUtil module.
"""
class ConfigUtilTest(unittest.TestCase):

	"""
	Placeholder function for setup process. Not needed for this test.
	"""
	def setUp(self):
		self.configUtil = ConfigUtil()
		self.configUtil.loadConfig()
		pass

	"""
	Placeholder function for tear down process. Not needed for this test.
	"""
	def tearDown(self):
		pass
	
	"""
	Tests retrieval of a boolean property.
	"""
	def testGetBooleanProperty(self):
		# TODO: implement this
		pass
	
	"""
	Tests retrieval of an integer property.
	"""
	def testGetIntegerProperty(self):
		# TODO: implement this
		pass
	
	"""
	Tests retrieval of a string property.
	"""
	def testGetProperty(self):
		# TODO: implement this
		pass
	
	"""
	Tests if a property exists.
	"""
	def testHasProperty(self):
		# TODO: implement this
		pass

	"""
	Tests if a section exists.
	"""
	def testHasSection(self):
		# TODO: implement this
		pass
	
	"""
	Tests if the configuration is loaded.
	"""
	def testIsConfigDataLoaded(self):
		if self.configUtil.isConfigDataLoaded():
			pass
		else:
			self.fail("Configuration data not loaded.")
	
if __name__ == "__main__":
	unittest.main()
