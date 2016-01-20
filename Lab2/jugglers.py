import sys

from peewee import *

db = SqliteDatabase("jugglers.db")

MAIN_MENU = ["[1] Search and Delete", "[2] Search and Update", "[3] Quit"]

jugglers = [
	{"name": "Ian Stewart",
	"country": "Canada",
	"catches": 94},
	{"name": "Aaron Gregg",
	"country": "Canada",
	"catches": 88},
	{"name": "Chad Taylor",
	"country": "USA",
	"catches": 78 }
]

class Juggler(Model):
	name = CharField(max_length = 255, unique="True")
	country = CharField(max_length = 255)
	catches = IntegerField(default = 0)

	class Meta:
		database = db



def add_jugglers():
	"""Adds initial data to the database"""
	try:
		for juggler in jugglers:
			Juggler.create(name=juggler["name"],
				country=juggler["country"],
				catches=juggler["catches"])
	# if entry exists updates entries instead	
	except IntegrityError:
		juggler_record = Juggler.get(name=juggler["name"])	
		juggler_record.country = juggler["country"]
		juggler_record.catches = juggler["catches"]
		juggler_record.save()


def print_records():
	"""Prints all the records in the database"""
	record_number = 1
	for juggler in Juggler:
		print("[{}]\tName: {}\tCountry: {}\tCatches: {}\t"
			.format(record_number,juggler.name, juggler.country, juggler.catches))
		record_number += 1


def main_menu():
	"""Displays options for manipulating database entries"""
	print("\n" + "=" * 20)
	for option in MAIN_MENU:
		print(option)
	selection = input("\nPlease make a selection: ")
	if selection in "123":
		if selection == "1":
			search_and_delete()
		if selection == "2":
			search_and_update()
		if selection == "3":
			sys.exit()
	else:
		print("Not a valid selection")
		main_menu()				


def search_and_delete():
	"""Allows users to delete a record from the database"""
	# get the search term from the user
	search_term = input("Enter the name of the record you would like to delete: ")
	try:
		juggler = Juggler.select().where(Juggler.name.startswith(search_term)).get()
		#juggler = db.execute_sql('SELECT * FROM Juggler WHERE name Like ?', search_term)
	except DoesNotExist:
		 	print("Record not found")
		 	search_and_delete()
	else:	 	
		choice = input("Delete record for {}? y/N? ".format(juggler.name))
		if choice in "yn":
			if choice == "y":
				juggler.delete_instance()
				print_records()
				main_menu()
			elif choice == "n":
				print_records()
				main_menu()
		else:
			search_and_delete()


def search_and_update():
	"""Allows users to delete a record from the database"""
	search_term = input("Enter the name of the record you would like to update:")
	try:
		juggler = Juggler.select().where(Juggler.name.startswith(search_term)).get()
	except DoesNotExist:
		print("Record not found")
		search_and_update()
	else:
		choice = input("Update record for {}? y/N".format(juggler.name))
		if choice in "yn":
			if choice == "y":
				juggler.catches = int(input("What is the new record? "))
				juggler.save()
				print_records()
				main_menu()
			elif choice == "n":
				print_records()
				main_menu()
		else:
			search_and_update()		


						


				

if __name__ == "__main__":
	db.connect()
	db.create_tables([Juggler], safe=True)
	add_jugglers()
	print_records()
	main_menu()


