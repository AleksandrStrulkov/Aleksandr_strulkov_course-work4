from src.class_userinput import UserInput
from src.class_api import HeadHunter_API, SuperJob_API
from pprint import pprint
import json

if __name__ == '__main__':
	# user_input = UserInput()
	# UserInput()
	# hh_api = HeadHunter_API("Москва", "Водитель")
	# data = hh_api.get_vacancies()
	# pprint(data, indent=4)
	# pprint(len(data))
	# sj_api = SuperJob_API("Ухта", "Водитель")
	# data = sj_api.get_vacancies()
	# pprint(data, indent=4)
	# pprint(len(data))
	# user_input = UserInput()
	# pprint(user_input, indent=2)
	user_input = UserInput()
	user_input()


