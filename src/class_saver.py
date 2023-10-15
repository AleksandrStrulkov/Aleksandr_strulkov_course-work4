import json
from abc import ABC, abstractmethod
from operator import itemgetter
FILE_ALL_VACANCY = "./data/vacancies_all.json"
FILE_ALL_FAVORITE = "./data/vacancies_favorite.json"

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
		"""Метод для добавления всех вакансий в файл"""
		with open(FILE_ALL_FAVORITE, "w", encoding="utf-8") as file:
			json.dump(self.vacancies, file, indent=4, ensure_ascii=False)

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
		# file = self.getter_vacancies
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
			if item['Расписание работы'] == schedule:
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

	def saver_vacancies_favorite(self, id_favorite):
		"""Метод для добавления вакансий в избранное"""
		experience_user = []
		for item in self.vacancies:
			if item['id вакансии'] == id_favorite:
				experience_user.append(item)
			with open(FILE_ALL_FAVORITE, "w", encoding="utf-8") as file:
				json.dump(experience_user, file, indent=4, ensure_ascii=False)

	def getter_vacancies_favorite(self):
		"""Метод получения данных из файла избранного"""
		with open(FILE_ALL_FAVORITE, "r", encoding="utf-8") as file:
			vacancy = json.load(file)
			return vacancy

	@classmethod
	def delete_vacancies_favorite(cls):
		"""Метод удаления данных из файла"""
		with open(FILE_ALL_FAVORITE, "w+") as file:
			file.seek(0)
			file.truncate()


class CLSSaver(Saver):
	pass


class XLSXSaver(Saver):
	pass
