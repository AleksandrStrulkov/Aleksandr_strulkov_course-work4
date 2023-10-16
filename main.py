from src.class_saver import JSONSaver
# from src.class_userinput import UserInput, user_input_city_profession, function_user1, function_start_menu
from src.class_api import HeadHunter_API, SuperJob_API
from pprint import pprint
import json

from src.class_userinput import UserInput
from src.class_vacancy import Vacancy
from src.userinput import userinput1

if __name__ == '__main__':
	userinput = UserInput()
	userinput()




	# user_input_city_profession()
	# print()
	# function_start_menu()



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
	# user_input = UserInput()
	# user_input()
	# city_user = input("Введите город в каком городе готовы работать: ").capitalize()
	# prof_user = input("Введите профессию которую рассматриваете : ").capitalize()
	# hh_block = HeadHunter_API("Москва", "Python developer")
	# vacancy_sourse = hh_block.get_vacancies()


	# 	hh_block = HeadHunter_API("Москва", "Python")
	# 	vacancy_sourse = hh_block.get_vacancies()
	# 	vacancy_readable = Vacancy(vacancy_sourse)
	# # # print(len(vacancy_readable.get_vacancies_items()))
	# 	vacancy_readable_viewer = vacancy_readable.readable_view_vacancy_hh()
# from_all_vac = JSONSaver(vacancy_readable_viewer)
	#  vacancy_json_viewer = from_all_vac.saver_vacancies()
	# sorted = from_all_vac.get_vacancies_salary_minimum(600000)
	# sorted = from_all_vac.get_vacancies_schedule("Удаленная работа")
# del_vacancy = from_all_vac.delete_vacancies_favorite()
	# min_salary = from_all_vac.getter_vacancies()
	# sorted = from_all_vac.get_vacancies_salary_minimum(20000)
	# sorted = from_all_vac.saver_vacancies_favorite('87927087')
	# delete_vacancies_favorite()


	# pprint(sorted, indent=2)



	# pprint(vacancy_readable_viewer, indent=2)
	# pprint(vacancy_readable.filtered_vacancies_by_minimum_salary_hh(300_000), indent=2)
	# pprint(vacancy_readable.сomparison_by_minimum_wage_hh(4, ), indent=2)

	# print(len(vacancy_readable_viewer))

	# 'Дата публикации': '2023-10-13 20:22:54',
	# hh_block = SuperJob_API("Москва", "Pathon")
	# vacancy_sourse = hh_block.get_vacancies()
	# vacancy_readable = Vacancy(vacancy_sourse)
	# print(len(vacancy_readable.get_vacancies_items()))
	# # pprint(vacancy_readable.get_vacancies_items(), indent=2)
	# vacancy_readable_viewer = vacancy_readable.readable_view_vacancy_sj()
	# pprint(vacancy_readable_viewer, indent=2)
	# print(len(vacancy_readable_viewer))

	# shed = JSONSaver(vacancy_readable_viewer)
	# shed = shed.get_vacancies_schedule("Полный день")
	# pprint(shed, indent=2)

