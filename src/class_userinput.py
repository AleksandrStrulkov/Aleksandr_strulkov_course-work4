import copy
from src.class_api import HeadHunter_API, SuperJob_API
from src.class_vacancy import Vacancy
from src.class_saver import JSONSaver
from pprint import pprint


class UserInput:
	"""Класс пользовательского интерфейса"""

	def __init__(self):
		"""Инициализация для работы с пользователем"""
		self.jsonfile_vacancy_instance = self.output_vacancy()
		# self.favorite_list =

	def output_vacancy(self):
		print("<><><><><><><><><><><><><><><><><><>")
		print("Вас приветствует программа сбора вакансий c платформ Headhunter и SuperJob!")
		print("Чтобы мы продолжили, выберите город поиска и профессию.")
		print("<><><><><><><><><><><><><><><><><><>")
		user_city = input("Город: ").capitalize()
		user_profile = input("Профессия: ").capitalize()
		print("<><><><><><><><><><><><><><><><><><>")
		print(
				f"Вы выбрали поиск работы в городе '{user_city}'\n"
				f"по профессии '{user_profile}'."
		)
		print("<><><><><><><><><><><><><><><><><><>")
		hh_platform_instance = Vacancy(HeadHunter_API(user_city, user_profile).get_vacancies()).readable_view_vacancy_hh()
		sj_platform_instance = Vacancy(SuperJob_API(user_city, user_profile).get_vacancies()).readable_view_vacancy_sj()
		all_vacancies = hh_platform_instance + sj_platform_instance
		jsonfile_vacancy_instance = JSONSaver(all_vacancies)
		saver_file_json = jsonfile_vacancy_instance.saver_vacancies()
		if len(hh_platform_instance) or len(sj_platform_instance) > 0:
			print("<><><><><><><><><><><><><><><><><><>")
			print(f'На платформе Headhunter найдено {len(hh_platform_instance)} вакансий!')
			print(f'На платформе SuperJob найдено {len(sj_platform_instance)} вакансий!')
			print("<><><><><><><><><><><><><><><><><><>")
		return jsonfile_vacancy_instance

	def __call__(self):
		"""Первый вывод пользователю"""
		while True:
			print("<><><><><><><><><><><><><><><><><><>")
			print("Введите варианты команд:\n"
				  "1 - Анализ вакансий\n"
				  "2 - Вывести на экран избранные вакансии\n"
				  "0 - Выход")

			print("<><><><><><><><><><><><><><><><><><>")

			user_input = int(input())

			if user_input == 0:
				quit()
			elif user_input == 1:
				self.select_parameters()
			elif user_input == 2:
				if self.favorite_list:
					print(self.favorite_list)
				print("Список избранного пуст!")

	def select_parameters(self):
		"""Второй вывод пользователю"""
		while True:
			print("<><><><><><><><><><><><><><><><><><>")
			print("Введите варианты команд\n"
				  "1 - вывести на экран все найденные вакансии\n"
				  "2 - отфильтровать вакансии по удовлетворяющей заработной плате\n"
				  "3 - отфильтровать вакансии по расписанию работы\n"
				  "4 - отфильтровать вакансии по опыту работы\n"
				  "5 - отфильтровать по всем условиям\n"
				  "0 - выйти в начало")

			print("<><><><><><><><><><><><><><><><><><>")

			user_input = int(input())

			if user_input == 0:
				self.__call__()
			elif user_input == 1:
				for item in self.jsonfile_vacancy_instance.getter_vacancies():
					pprint(item, indent=2)
					print("<><><><><><><><><><><><><><><><><><>")
			elif user_input == 2:
				self.vacancy_filtred_salary()
			elif user_input == 3:
				self.vacancy_filtred_schedule()
			elif user_input == 4:
				self.vacancy_filtred_experience()
			elif user_input == 5:
				self.vacancy_filtred_all()
			else:
				print("Непонятная команда")

	def vacancy_filtred_salary(self):
		pass

	def vacancy_filtred_schedule(self):
		pass

	def vacancy_filtred_experience(self):
		pass

	def vacancy_filtred_all(self):
		pass

	def output_format(self):
		pass





