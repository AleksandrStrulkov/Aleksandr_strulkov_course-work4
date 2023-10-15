class Vacancy:
	def __init__(self, vacancy_info: dict):
		self.vacancy_info = vacancy_info

	def vacancy_valid_hh(self):
		"""Валидация данных с вакансий с платформы HeadHunter"""
		hh_valid_vacancy = []
		for vacancy in self.vacancy_info:
			if isinstance(vacancy["id"], str) and vacancy["id"].isdigit():
				vacancy_id = vacancy["id"]

			if isinstance(vacancy["name"], str):
				vacancy_name = vacancy["name"]

			if vacancy['salary']['from'] is not None and isinstance(vacancy['salary']['from'], int):
				vacancy_salary_from = vacancy['salary']['from']
			else:
				vacancy['salary']['from'] = "Информация отсутствует"
				vacancy_salary_from = vacancy['salary']['from']

			if vacancy['salary']['to'] is not None and isinstance(vacancy['salary']['to'], int):
				vacancy_salary_to = vacancy['salary']['to']
			else:
				vacancy['salary']['to'] = "Информация отсутствует"
				vacancy_salary_to = vacancy['salary']['to']

			if isinstance(vacancy['area']['name'], str):
				vacancy_area = vacancy['area']['name']

			if "https://" in vacancy["alternate_url"]:
				vacancy_url = vacancy["alternate_url"]

			if isinstance(vacancy["schedule"]["name"], str):
				vacancy_schedule = vacancy["schedule"]["name"]

			if isinstance(vacancy['experience']['name'], str):
				vacancy_experience = vacancy['experience']['name']

			if (vacancy_id and vacancy_name
				and vacancy_salary_from
				and vacancy_salary_to
				and vacancy_area
				and vacancy_url
				and vacancy_schedule
				and vacancy_experience):
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
					"Ссылка на вакансию": vacancy['url'],
					"Расписание работы": vacancy['schedule']['name'],
					"Опыт работы": vacancy['experience']['name']
			}
			hh_vacancy_readable.append(vacancies_items)
		return hh_vacancy_readable

	def get_vacancies_items(self):
		return self.vacancy_info