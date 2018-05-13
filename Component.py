""" This a mining rig component Class along with its Interaface Class """
from abc import ABC, abstractmethod

class IComponent(ABC):
	@abstractmethod
	def get_info(self):
		pass

	@abstractmethod
	def get_stats(self):
		pass

	@abstractmethod
	def update_info(self):
		pass

	@abstractmethod
	def update_stats(self):
		pass

class Component(IComponent):
	m_id = ""      # component name
	m_info = {}    # dictionary with info
	m_stats = {}   # dictionary with stats
	
	@abstractmethod
	def get_info(self):
		pass

	@abstractmethod
	def get_stats(self):
		pass	

	@abstractmethod
	def update_info(self):
		pass

	@abstractmethod
	def update_stats(self):
		pass
