import copy
from src.class_api import HeadHunter_API, SuperJob_API
from pprint import pprint



class UserInput:
	def __init__(self):
		self.city = HeadHunter_API(self.user_input_city(), self.user_input_prof())
		data = self.city.get_vacancies()
		pprint(data, indent=2)

	# @staticmethod
	def user_input_city(self):
		city_user = input("Введите город в каком городе готовы работать: ").capitalize()
		return city_user

	# @staticmethod
	def user_input_prof(self):
		prof_user = input("Введите профессию которую рассматриваете : ").capitalize()
		return prof_user

	def print_city(self):
		pass


	def __call__(self):
		pass



