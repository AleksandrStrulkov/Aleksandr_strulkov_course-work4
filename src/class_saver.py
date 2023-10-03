from abc import ABC, abstractmethod


class Saver(ABC):
	pass


class JSONSaver(Saver):
	pass


class CLSSaver(Saver):
	pass


class XLSXSaver(Saver):
	pass
