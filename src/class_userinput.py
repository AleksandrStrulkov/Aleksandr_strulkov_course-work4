from src.class_api import HeadHunter_API, SuperJob_API
from src.class_vacancy import Vacancy
from src.class_saver import JSONSaver
from pprint import pprint


class UserInput:
	"""Класс интерфейса для пользователя"""

	def __init__(self):
		"""Инициализация для работы с пользователем"""
		self.jsonfile_vacancy_instance = self.output_vacancy()

	def output_vacancy(self):
		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print("Вас приветствует программа сбора вакансий c платформ Headhunter и SuperJob!")
			print("Чтобы мы продолжили, выберите город поиска и профессию.")
			print("<><><><><><><><><><><><><><><><><><>")
			user_city = input("Город: ").capitalize()
			user_profile = input("Профессия: ").capitalize()
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print(
					f"Вы выбрали поиск работы в городе '{user_city}'\n"
					f"по профессии '{user_profile}'."
			)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			hh_platform_instance = Vacancy(
					HeadHunter_API(user_city, user_profile).get_vacancies()
			).readable_view_vacancy_hh()
			sj_platform_instance = Vacancy(
					SuperJob_API(user_city, user_profile).get_vacancies()
			).readable_view_vacancy_sj()
			all_vacancies = hh_platform_instance + sj_platform_instance
			jsonfile_vacancy_instance = JSONSaver(all_vacancies)
			saver_file_json = jsonfile_vacancy_instance.saver_vacancies()
			if len(hh_platform_instance) or len(sj_platform_instance) > 0:
				print(f'На платформе Headhunter найдено {len(hh_platform_instance)} вакансий!')
				print(f'На платформе SuperJob найдено {len(sj_platform_instance)} вакансий!')
				print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			else:
				print("Введенные параметры не корректны")
				continue
			return jsonfile_vacancy_instance

	def __call__(self):
		"""Первый вывод пользователю"""
		while True:
			print(
					"Введите варианты команд:\n"
					"1 - Анализ вакансий\n"
					"2 - Вывести на экран список избранных вакансий\n"
					"3 - Очистить список избранных вакансий\n"
					"0 - Выход"
			)

			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			user_input = int(input())

			if user_input == 0:
				quit()
			elif user_input == 1:
				self.select_parameters()
			elif user_input == 2:
				getter_vac_fav = self.jsonfile_vacancy_instance.getter_vacancies_favorite()
				if self.jsonfile_vacancy_instance.getter_vacancies_favorite():
					for item in getter_vac_fav:
						pprint(item, indent=2)
						print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			elif user_input == 3:
				self.jsonfile_vacancy_instance.delete_vacancies_favorite()
			else:
				print("Непонятная команда")
				continue

	def select_parameters(self):
		"""Основной вывод пользователю"""
		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print(
					"Введите варианты команд:\n"
					"1 - Вывести вакансии на экран\n"
					"2 - Отфильтровать вакансии по минимальной заработной плате\n"
					"3 - Отфильтровать вакансии по расписанию работы\n"
					"4 - Отфильтровать вакансии по опыту работы\n"
					"5 - Сортировать по минимальной заработной плате\n"
					"0 - Выйти в начальное меню"
			)

			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			user_input = int(input())

			if user_input == 0:
				self.__call__()
			elif user_input == 1:
				for item in self.jsonfile_vacancy_instance.getter_vacancies():
					pprint(item, indent=2)
					print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			elif user_input == 2:
				self.vacancy_filtred_salary()
			elif user_input == 3:
				self.vacancy_filtred_schedule()
			elif user_input == 4:
				self.vacancy_filtred_experience()
			elif user_input == 5:
				self.vacancy_filter_salary()
			else:
				print("Непонятная команда")
				continue

	def vacancy_filtred_salary(self):
		"""Метод фильтрации по заработной плате"""
		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print(
					"Мы можем отфильтровать найденные вакансии по заработной плате\n"
			)

			user_input = int(input("Укажите минимальную оплату по которой готовы трудиться: "))
			user_salary_min = self.jsonfile_vacancy_instance.get_vacancies_salary_minimum \
				(user_input)

			for item in user_salary_min:
				pprint(item, indent=2)
				print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			print(
					"Мы можем записать вакансию в избранное\n"
					"1 - Записать\n"
					"0 - Нет\n"
			)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_input_yes_no = int(input("Укажите значение: "))

			if user_input_yes_no == 0:
				break
			if user_input_yes_no == 1:
				self.record_vacancy_favorite()
			else:
				break

	def record_vacancy_favorite(self):

		while True:
			user_id__vacancy_input = int(input("Укажите id выбранной вакансии: "))
			user_record_vacancy_favorite = self.jsonfile_vacancy_instance.add_vacancies_favorite \
					(user_id__vacancy_input)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			break

		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_input = int(
					input(
							"Укажите следующие значения:\n"
							"0 - Выйти  в меню выбора города и профессии\n"
							"1 - Выйти в первое меню\n"
							"2 - Выйти во второе меню\n"
							"3 - Продолжить запись в избранное\n"
					)
			)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			if user_input == 0:
				self.output_vacancy()

			elif user_input == 1:
				self.__call__()

			elif user_input == 2:
				self.select_parameters()

			elif user_input == 3:
				self.record_vacancy_favorite()

			else:
				print("Непонятная команда")
				continue

	def vacancy_filtred_schedule(self):
		"""Метод фильтрации вакансий по графику работы"""
		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_input = int(
					input(
							"Укажите какие возможные условия вас интересуют:\n"
							"1 - Полный рабочий день\n"
							"2 - Гибкий график\n"
							"3 - Удаленная работа\n"
							"4 - Неполный рабочий день\n"
							"5 - Сменный график работы\n"
							"6 - Вахтовый метод:\n"
							"0 - Выйти\n"
					)
			)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
				(user_input)

			if user_input == 0:
				break
			elif user_input == 1:
				user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
					("Полный рабочий день" or "Полный день")
			elif user_input == 2:
				user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
					("Гибкий график")
			elif user_input == 3:
				user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
					("Удаленная работа" or "Неполная дистанционная занятость")
			elif user_input == 4:
				user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
					("Неполный рабочий день")
			elif user_input == 5:
				user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
					("Сменный график" or "Сменный график работы")
			elif user_input == 6:
				user_filtred_schedule = self.jsonfile_vacancy_instance.get_vacancies_schedule \
					("Вахтовый метод" or "Работа вахтовым методом")
			else:
				print("Непонятная команда")
				continue

			for item in user_filtred_schedule:
				pprint(item, indent=2)
				print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			print(
					"Мы можем записать вакансию в избранное, укажите ее id ниже в поле\n"
					"1 - Записать\n"
					"0 - Нет\n"
			)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_input_yes_no = int(input("Укажите значение: "))

			if user_input_yes_no == 0:
				break
			if user_input_yes_no == 1:
				self.record_vacancy_favorite()
			else:
				break

	def vacancy_filtred_experience(self):
		"""Метод фильтрации вакансий по требуемому опыту работы"""
		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print("Мы можем отфильтровать найденные вакансии по требуемому опыту работы\n")
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_input = int(
					input(
							"Укажите какой у вас опыт работы и на каких условиях готовы\n"
							"отозваться на вакансию:\n"
							"1 - Нет опыта\n"
							"2 - От 1 года\n"
							"3 - От 3 лет\n"
					)
			)

			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_filtred_experience = self.jsonfile_vacancy_instance.get_vacancies_experience \
				(user_input)

			if user_input == 1:
				user_filtred_experience = self.jsonfile_vacancy_instance.get_vacancies_experience \
					("Нет опыта" or "Без опыта")
			elif user_input == 2:
				user_filtred_experience = self.jsonfile_vacancy_instance.get_vacancies_experience \
					("От 1 года до 3 лет" or "От 1 года")
			elif user_input == 3:
				user_filtred_experience = self.jsonfile_vacancy_instance.get_vacancies_experience \
					("От 3 до 6 лет" or "От 3 лет")
			else:
				print("Непонятная команда")
				continue

			for item in user_filtred_experience:
				pprint(item, indent=2)
				print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

			print(
					"Мы можем записать вакансию в избранное, укажите ее id ниже в поле\n"
					"1 - записать\n"
					"0 - нет\n"
			)
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			user_input_yes_no = int(input("Укажите значение: "))

			if user_input_yes_no == 0:
				break
			if user_input_yes_no == 1:
				self.record_vacancy_favorite()
			else:
				break

	def vacancy_filter_salary(self):
		"""Метод сортировки по заработной плате всех найденных вакансий"""
		while True:
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print("Выполняем сортировку по заработной плате всех вакансий по убыванию")

			vac_filter_sal = self.jsonfile_vacancy_instance.get_vacancies_sorted()

			for item in vac_filter_sal:
				pprint(item, indent=2)
				print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			break