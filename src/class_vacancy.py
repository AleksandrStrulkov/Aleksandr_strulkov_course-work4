import datetime
import arrow


class Vacancy:
	def __init__(self, vacancy_info: dict):
		self.vacancy_info = vacancy_info

	def vacancy_valid_hh(self):
		"""Валидация данных с вакансий с платформы HeadHunter"""
		hh_valid_vacancy = []
		for vacancy in self.vacancy_info:
			if isinstance(vacancy["id"], str) and vacancy["id"].isdigit():
				vacancy_id = vacancy["id"]
			else:
				vacancy_id = False

			if isinstance(vacancy['name'], str):
				vacancy_name = vacancy['name']
			else:
				vacancy_name = False

			if vacancy['salary']['from'] is not None and isinstance(vacancy['salary']['from'], int):
				vacancy_salary_from = vacancy['salary']['from']
			else:
				vacancy['salary']['from'] = 0
				vacancy_salary_from = vacancy['salary']['from']

			if vacancy['salary']['to'] is not None and isinstance(vacancy['salary']['to'], int):
				vacancy_salary_to = vacancy['salary']['to']
			else:
				vacancy['salary']['to'] = 0
				vacancy_salary_to = vacancy['salary']['to']

			if isinstance(vacancy['area']['name'], str):
				vacancy_area = vacancy['area']['name']
			else:
				vacancy_area = False

			if "https://" in vacancy["alternate_url"]:
				vacancy_url = vacancy["alternate_url"]
			else:
				vacancy_url = False

			if isinstance(vacancy["schedule"]["name"], str):
				vacancy_schedule = vacancy["schedule"]["name"]
			else:
				vacancy_schedule = False

			if isinstance(vacancy['experience']['name'], str):
				vacancy_experience = vacancy['experience']['name']
			else:
				vacancy_experience = False

			if (vacancy_id or vacancy_name
					or vacancy_salary_from
					or vacancy_salary_to
					or vacancy_area
					or vacancy_url
					or vacancy_schedule
					or vacancy_experience):
				hh_valid_vacancy.append(vacancy)

		return hh_valid_vacancy

	def readable_view_vacancy_hh(self):
		"""Метод преобразования в читаемый вид вакансий с платформы HeadHunter"""
		hh_vacancy_readable = []

		for vacancy in self.vacancy_valid_hh():
			vacancies_items = {
					"id вакансии": vacancy['id'],
					"Наименование вакансии": vacancy['name'],
					"Минимальная зарплата": vacancy['salary']['from'],
					"Максимальная зарплата": vacancy['salary']['to'],
					"Город": vacancy['area']['name'],
					"Ссылка на вакансию": vacancy['alternate_url'],
					"Расписание работы": vacancy['schedule']['name'],
					"Опыт работы": vacancy['experience']['name']
			}
			hh_vacancy_readable.append(vacancies_items)
		return hh_vacancy_readable

	def сomparison_vacancies_sj(self, first_num, second_num):
		"""Метод сравнения вакансий по минимальной зарплате"""
		salary_one = self.readable_view_vacancy_hh()[first_num - 1]["Минимальная зарплата"]
		salary_two = self.readable_view_vacancy_hh()[second_num - 1]["Минимальная зарплата"]

		return salary_one >= salary_two

	def vacancy_valid_sj(self):
		"""Валидация данных с вакансий с платформы SuperJob"""
		sj_valid_vacancy = []
		for vacancy in self.vacancy_info:
			if isinstance(vacancy["id"], int) or vacancy["id"] is not None:
				vacancy_id = vacancy["id"]
			else:
				vacancy_id = False

			if isinstance(vacancy["profession"], str) or vacancy["profession"] is not None:
				vacancy_name = vacancy["profession"]
			else:
				vacancy_name = False

			if vacancy['payment_from'] is not None or isinstance(vacancy["payment_from"], int):
				vacancy_salary_from = vacancy['payment_from']
			else:
				vacancy_salary_from = False

			if vacancy['payment_to'] is not None or isinstance(vacancy["payment_to"], int):
				vacancy_salary_to = vacancy['payment_to']
			else:
				vacancy_salary_to = False

			if isinstance(vacancy['town']['title'], str) or vacancy['town']['title'] is not None :
				vacancy_area = vacancy['town']['title']
			else:
				vacancy_area = False

			if "https://" in vacancy["link"]:
				vacancy_url = vacancy["link"]
			else:
				vacancy_url = False

			if isinstance(vacancy["type_of_work"]["title"], str) or vacancy["type_of_work"]["title"] is not None:
				vacancy_schedule = vacancy["type_of_work"]["title"]
			else:
				vacancy_schedule = False

			if isinstance(vacancy['experience']['title'], str) or vacancy['experience']['title'] is not None:
				vacancy_experience = vacancy['experience']['title']
			else:
				vacancy_experience = False

			if (vacancy_id or vacancy_name
					or vacancy_salary_from
					or vacancy_salary_to
					or vacancy_area
					or vacancy_url
					or vacancy_schedule
					or vacancy_experience):
				sj_valid_vacancy.append(vacancy)

		return sj_valid_vacancy

	def readable_view_vacancy_sj(self):
		"""Метод преобразования в читаемый вид вакансий с платформы SuperJob"""
		sj_vacancy_readable = []
		for vacancy in self.vacancy_valid_sj():
			vacancies_items = {
					"id вакансии": vacancy['id'],
					"Наименование вакансии": vacancy['profession'],
					"Минимальная зарплата": vacancy['payment_from'],
					"Максимальная зарплата": vacancy['payment_to'],
					"Город": vacancy['town']['title'],
					"Ссылка на вакансию": vacancy['link'],
					"Расписание работы": vacancy["type_of_work"]["title"],
					"Опыт работы": vacancy['experience']['title']
			}
			sj_vacancy_readable.append(vacancies_items)
		return sj_vacancy_readable

	def сomparison_vacancies_sj(self, first_num, second_num):
		"""Метод сравнения вакансий по минимальной зарплате"""
		salary_one = self.readable_view_vacancy_sj()[first_num - 1]["Минимальная зарплата"]
		salary_two = self.readable_view_vacancy_sj()[second_num - 1]["Минимальная зарплата"]

		return salary_one >= salary_two


