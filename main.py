from art import logo, vs
from game_data import data
import random
from replit import clear

def get_account():
	"""Get any account from data"""
	return random.choice(data)

print(logo)


print(vs)