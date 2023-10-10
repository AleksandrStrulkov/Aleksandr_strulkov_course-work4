from src.class_userinput import UserInput
from src.class_api import HeadHunter_API
from pprint import pprint

if __name__ == '__main__':
	# user_input = UserInput()
	# UserInput()
	hh_api = HeadHunter_API("Москва", "Водитель")
	data = hh_api.get_vacancies()
	pprint(data, indent=4)
	pprint(len(data))