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

def game():
	"""Game logic engine"""
	print(logo)
	score = 0
	continue_game = True
	account_a = get_account()
	account_b = get_account()

	while continue_game:
		account_a = account_b
		account_b = get_account()

		while account_a == account_b:
			account_b = get_account()

		print(f"Compare A: {account_format(account_a)}")
		print(vs)
		print(f"Compare B: {account_format(account_b)}")

		reply = input("Who has more followers? Type 'A' or 'B': ").lower()
		a_follower_count = account_a["follower_count"]
		b_follower_count = account_b["follower_count"]
		is_correct = user_answer(reply, a_follower_count, b_follower_count)

		clear()
		print(logo)
		if is_correct:
			score += 1
			print(f"You're right! Current score: {score}")
		else:
			continue_game = False
			print(f"Sorry, that's wrong. Final score: {score}")

game()


