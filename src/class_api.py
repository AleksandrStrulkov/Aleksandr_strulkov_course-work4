from abc import ABC, abstractmethod
import os
import requests


class API(ABC):

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def get_vacancies(self):
		pass

	@abstractmethod
	def get_city_id(self):
		pass


class HeadHunter_API(API):
	"""Получение вакансий с платформы HeadHunter API"""
	HH_URL = "https://api.hh.ru/vacancies"
	HH_AREAS = "https://api.hh.ru/suggests/areas"

	def __init__(self, city_name, prof_name):
		self.city_name = city_name
		self.prof_name = prof_name

	def __repr__(self):
		return (f"Указанный город: {self.city_name}"
				f"Указанная профессия: {self.prof_name}")

	def get_city_id(self):
		"""Получение id города для получения в нем вакансий"""
		params = {
				"text": self.city_name
		}
		hh_areas_url = self.HH_AREAS
		response = requests.get(hh_areas_url, params=params)

		for city in response.json()["items"]:
			if city["text"] == self.city_name:
				return city["id"]

	def get_vacancies(self):
		"""Получение всех вакансий выбранного города по профессии"""
		hh_vac_url = self.HH_URL
		params = {
				"only_with_salary": True,
				"text": self.prof_name,
				"per_page": 100,
				"area": self.get_city_id()
		}
		response = requests.get(hh_vac_url, params=params)

		if response.status_code == 200:
			vacancies = response.json()
			return vacancies["items"]


class SuperJob_API(API):
	"""Получение вакансий с платформы SuperJob API"""
	SJ_URL = "https://api.superjob.ru/2.0/vacancies"
	SJ_AREAS = "https://api.superjob.ru/2.0/towns"
	SJ_TOKEN = os.getenv('SJ_API_TOKEN')

	def __init__(self, town_name, prof_name):
		self.city_name = town_name
		self.prof_name = prof_name

	def __repr__(self):
		return (f"Указанный город: {self.city_name}"
				f"Указанная профессия: {self.prof_name}")

	def get_city_id(self):
		pass

	def get_vacancies(self):
		"""Получение всех вакансий выбранного города"""
		hh_vac_url = self.SJ_URL
		params = {
				"keyword": self.prof_name,
				"count": 100,
				"town": self.city_name
		}

		headers = {'Hosts': 'api.superjob.ru',
				   'X-API-APP-id': self.SJ_TOKEN
				   }

		response = requests.get(hh_vac_url, params=params, headers=headers)

		if response.status_code == 200:
			vacancies = response.json()
			return vacancies['objects']