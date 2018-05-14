""" Gpu element """

from Component import *

class Ram(Component):

	m_isActive = False

	def get_info(self):
		return(self.m_info)

	def get_stats(self):
		return(self.m_stats)

	def update_info(self):
		return(print("info updated"))

	def update_stats(self):
		return(print("stats updated"))
