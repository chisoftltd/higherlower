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

def user_answer(guess, a_followers, b_followers):
	"""Checks user's guess against account followers and
	returns True if user got it right or False if user got it wrong."""
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"

print(logo)


print(vs)