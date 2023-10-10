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
	HH_URL = "https://api.hh.ru/vacancies"
	HH_AREAS = "https://api.hh.ru/suggests/areas"

	def __init__(self, city_name, prof_name):
		# self.headers = {
		# 		"User-Agent": "Your User Agent"
		# }
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
		"""Получение всех вакансий выбранного города"""
		hh_vac_url = self.HH_URL
		params = {
				"text": self.prof_name,
				"per_page": 100,
				"area": self.get_city_id()
		}
		responce = requests.get(hh_vac_url, params=params)
		return responce.json()["items"]



class SuperJob_API(API):
	pass
