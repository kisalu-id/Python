class Bankkonto:
	def __init__(self, user_name, kontonummer, kontostand):
		self.__user_name = user_name     #in Python wird eine Variable privat gemacht, indem ihr Name mit zwei Unterstrichen __ beginnt
		self.__kontonummer = kontonummer
		self.__kontostand = kontostand

	def get_kontostand(self):
			return self.__kontostand
	
	def get_kontonum(self):
			return "Access denied"
	
	def get_name(self):
			return self.__user_name
	
	def einzahlen(self, betrag):
		if betrag > 0:
			self.__kontostand += betrag
		else:
			raise ValueError("Der Betrag muss positiv sein")

	def abheben(self, betrag):
		if 0 <betrag < self.__kontostand:
			self.__kontostand -= betrag
		else:
			raise ValueError("Ungültiger Abhebungsbetrag")

konto = Bankkonto("Anna Smidt", "123456789", 1000)
print(konto.get_kontostand())  #1000
print(konto.get_kontonum())  #Access denied
print(konto.get_name())  #Anna Smidt

konto.abheben(500)
print(konto.get_kontostand())
konto.einzahlen(300)
print(konto.get_kontostand())
