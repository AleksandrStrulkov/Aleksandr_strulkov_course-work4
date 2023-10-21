import json
from abc import ABC, abstractmethod
from operator import itemgetter

FILE_ALL_VACANCY = "./data/vacancies_all.json"



class Saver(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def saver_vacancies(self):
		pass

	@abstractmethod
	def getter_vacancies(self):
		pass

	@abstractmethod
	def delete_vacancies(self):
		pass


class JSONSaver(Saver):
	"""Класс для добавления вакансий в файл json"""

	def __init__(self, vacancies):
		self.vacancies = vacancies

	def saver_vacancies(self):
		"""Метод для добавления вакансий в файл"""
		with open(FILE_ALL_VACANCY, "w", encoding="utf-8") as file:
			json.dump(self.vacancies, file, indent=2, ensure_ascii=False)





	def getter_vacancies(self):
		"""Метод получения данных из файла"""
		with open(FILE_ALL_VACANCY, "r", encoding="utf-8") as file:
			vacancy = json.load(file)
			return vacancy

	@classmethod
	def delete_vacancies(cls):
		"""Метод удаления данных из файла"""
		with open(FILE_ALL_VACANCY, "w+") as file:
			file.seek(0)
			file.truncate()

	def get_vacancies_salary_minimum(self, salary):
		"""Метод получения вакансий по минимальной заработной плате"""
		salary_min = []
		for item in self.getter_vacancies():
			if item['Минимальная зарплата'] >= salary:
				salary_min.append(item)
		if len(salary_min) > 0:
			return salary_min
		return 'Не удалось найти вакансию с такой минимальной заработной платой'

	def get_vacancies_schedule(self, schedule):
		"""Метод получения вакансий по условиям графика работы"""
		schedule_user = []
		for item in self.getter_vacancies():
			if item['График работы'] == schedule:
				schedule_user.append(item)
		return schedule_user

	def get_vacancies_experience(self, experience):
		"""Метод получения вакансий по требуемому опыту работы"""
		experience_user = []
		for item in self.getter_vacancies():
			if item['Опыт работы'] == experience:
				experience_user.append(item)
		return experience_user

	def get_vacancies_sorted(self):
		"""Сортировка вакансий по заработной плате"""
		return sorted(self.getter_vacancies(), key=itemgetter('Минимальная зарплата'), reverse=True)