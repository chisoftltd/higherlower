from art import logo, vs
from game_data import data
import random
from replit import clear

def get_account():
	"""Get any account from data"""
	return random.choice(data)

def account_format(account):
	"""Format account into: name, description and country"""
	name = account["name"]
	description = account["description"]
	country = account["country"]
	return f"{name}, a {description}, from {country}"

print(logo)


print(vs)