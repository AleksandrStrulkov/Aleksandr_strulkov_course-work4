class Vacancy:
	def __init__(self, vacancy_info: dict):
		self.__vacancy_info = vacancy_info
		# self.id = vacancy_info['id']
		self.type = vacancy_info['type']['name']
		self.name = vacancy_info['name']
		self.salary_from = vacancy_info['salary_from']
		self.salary_to = vacancy_info['salary_to']
		self.area = vacancy_info['area']['name']
		self.url = vacancy_info['url']
		self.schedule = vacancy_info['schedule']['name']
		self.experience = vacancy_info['experience']['name']

def vacancy_valid_hh(vacancy_inf):
	vacancy_valid_hh = []
	for vacancy in vacancy_inf:
		if isinstance(vacancy["id"], str):
			vacancy_id = vacancy["id"]

		if isinstance(vacancy["type"]["name"], str):
			vacancy_type = vacancy["type"]["name"]

		if isinstance(vacancy["name"], str):
				vacancy_name = vacancy["name"]

		if vacancy['salary'] is not None:
			vacancy_salary_from = vacancy['salary']['from'] = "Информация скрыта"

		if vacancy['salary'] is not None:
			vacancy_salary_to = vacancy['salary']['to'] = "Информация скрыта"

		if isinstance(vacancy['area']['name'], str) and vacancy['area']['name'] is not None:
			vacancy_area = vacancy['area']['name']

		else:
			vacancy_area = False

		if "https://" in vacancy["alternate_url"]:
			vacancy_url = vacancy["alternate_url"]

		if isinstance(vacancy["schedule"]["name"], str) and vacancy["schedule"]["name"] is not None:
			vacancy_schedule = vacancy["schedule"]["name"]

		else:
			vacancy_schedule = False

		if isinstance(vacancy['experience']['name'], str) and vacancy['experience']['name'] is not None:
			vacancy_experience = vacancy["schedule"]["name"]
		else:
			vacancy_experience = False

		if (vacancy_id and vacancy_type and vacancy_name and vacancy_salary_from and vacancy_salary_to and
				vacancy_area and vacancy_url and vacancy_schedule and vacancy_experience):

			vacancy_valid_hh.append(vacancy)
	return vacancy_valid_hh

	def vacancy_valid_sj(self):
		pass


def readable_view_vacancy_hh(vacancy_readable):
	"""Метод преобразования в читаемый вид"""
	hh_vacancy_readable = []
	for vacancy in vacancy_readable:
		vacancies_items = {
				"id вакансии": vacancy["id"],
				"Тип вакансии": vacancy["type"]["name"],
				"Наименование вакансии": vacancy["name"],
				"Минимальная зарплата": vacancy["salary"]["from"],
				"Максимальная зарплата": vacancy["salary"]["to"],
				"Город": vacancy["area"]["name"],
				"Ссылка на вакансию": vacancy["url"],
				"Расписание работы": vacancy["schedule"]["name"],
				"Опыт работы": vacancy["experience"]["name"]
		}
		hh_vacancy_readable.append(vacancies_items)
	return hh_vacancy_readable