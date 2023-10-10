import copy
from src.class_api import HeadHunter_API, SuperJob_API
# from src.class_mylist import Mylist


class UserInput:
	param_zero = {}
	def __init__(self):
		self.hh_api = HeadHunter_API()
		self.sj_api = SuperJob_API()
		self.mylist = Mylist()
		self.all_list = Mylist()
		self.param = copy.deepcopy(self.param_zero)


	def __call__(self):
		pass



