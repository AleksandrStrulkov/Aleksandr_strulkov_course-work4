import json
from abc import ABC, abstractmethod


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
		with open("vacancies.json", "w", encoding="utf-8") as file:
			json.dump(self.vacancies, file, indent=4, ensure_ascii=False)

	def getter_vacancies(self):
		"""Метод получения данных из файла"""
		with open("vacancies.json", "r", encoding="utf-8") as file:
			vacancy = json.load(file)
			return vacancy

	@classmethod
	def delete_vacancies(cls):
		"""Метод удаления данных из файла"""
		with open("vacancies.json", "w+") as file:
			file.seek(0)
			file.truncate()

	def get_vacancies_salary_minimum(self, salary):
		"""Метод получения вакансий по минимальной заработной плате"""
		for item in self.vacancies:
			if item['Зарплата от'] == salary:
				return item
			return 'Не удалось найти вакансию с такой минимальной заработной платой'

	def get_vacancies_schedule(self, schedule):
		"""Метод получения вакансий по условиям графика работы"""
		for item in self.vacancies:
			if item ['График работы'] == schedule:
				return item
			return 'Не удалось найти вакансии по указанному графику работы'

	def get_vacancies_experience(self, experience):
		"""Метод получения вакансий по требуемому опыту работы"""
		for item in self.vacancies:
			if item['Опыт работы'] == experience:
				return item
			return 'Не удалось найти вакансии по указанному опыту работы'


class CLSSaver(Saver):
	pass


class XLSXSaver(Saver):
	pass
