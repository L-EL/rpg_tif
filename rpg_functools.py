# RPG USEFUL FUNCTIONS
import random
import math
import rpg_config as config

import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def check_input(txt, choices):
	key = input(txt)
	key = key.upper()
	while key not in choices:
		print(f"Ta réponse n'est pas reconnue. [{'/'.join(choices)}]")
		key = input()
	return key


def time2hours(time):
	return f"{time//60}h{time%60:02d}"

def shifumi(DEBUG = False):
	choice = random.choice([0, 1, 2])  if DEBUG else  int(check_input(p_color("narration/gpu/shifumi_play.txt"),
							 ['0', '1', '2']))
	print('your choice : ' +str(choice))
	choice_lisa = random.randint(0, 2)
	print('Lisa choice : ' +str(choice_lisa))
	choice_raphael = random.randint(0, 2)
	print('Raphael choice : ' +str(choice_raphael))
	m_ = max(config.shifumi_truth_table[choice][choice_lisa],
			 config.shifumi_truth_table[choice][choice_raphael])

	while m_ == -1:
		# ex-aequo
		print("Ex-aequo.")
		choice = random.choice([0, 1, 2])  if DEBUG else  int(check_input(p_color("narration/gpu/shifumi_play.txt"),
								 ['0', '1', '2']))
		print('your choice : '+str(choice))
		choice_lisa = random.randint(0, 2)
		print('Lisa choice : ' +str(choice_lisa))
		choice_raphael = random.randint(0, 2)
		print('Raphael choice : ' +str(choice_raphael))
		m_ = max(config.shifumi_truth_table[choice][choice_lisa],
				 config.shifumi_truth_table[choice][choice_raphael])

	if m_ == 0:
		# Tif looses
		print(p_color("narration/gpu/shifumi_loose.txt"))
		return False

	print(p_color("narration/gpu/shifumi_win.txt"))
	return True


menu_choice = {0: "Faire amener un hamac pour piéger Daoult [Obligatoire]",
			   1: "Diplôme de thèse [Obligatoire] Réaliser avant 18h.",
               2: "Organiser un tournoi de babyfoot [Obligatoire]",
	           3: "Manger [Facultatif] Possible jusque 15h.",
			   4: "Sieste [Facultatif]"}

def display_menu(time, hamac, diploma, babyfoot, eaten):
	to_display = dict(menu_choice)
	if hamac:
		del to_display[0]
	if diploma:
		del to_display[1]
	elif time > config.diploma_deadline * 60:
		del to_display[1]
	if babyfoot:
		del to_display[2]
	if eaten:
		del to_display[3]
	elif time > config.lunch_deadline * 60:
		del to_display[3]
	return to_display


def daoult_attack(covid, hamac, fungus):
	to_display = {0: "covid",
				  1: "hamac",
				  2: "champignon"}
	if not covid:
		del to_display[0]
	if not hamac:
		del to_display[1]
	if not fungus:
		del to_display[2]
	txt = "Tu attaques Daoult avec le " + ','.join([f'{value} [{key}]' for key, value in to_display.items()])
	return txt,to_display.keys()


class Energy():
	def __init__(self, energy):
		self.e = energy

	def __add__(self, de):
		result = self.e + de
		# force energy to be between 0 and 100
		if not 0 <= result <= 100:
			result = min(max(result, 0), 100)
		self.e = result
		return self

	def __sub__(self,de):
		result = self.e - de
		if 0 >= result:
			die()
		else:
			self.e = result
			return self

	def __lt__(self,value):
		return self.e < value

	def __gt__(self,value):
		return self.e > value

	def __le__(self,value):
		return self.e <= value


	def __isub__(self,de):
		return self.__sub__(de)

	def __iadd__(self, de):
		return self.__add__(de)

	def __str__(self):
		return str(self.e)

	def __repr__(self):
		return str(self.e)

	def __ge__(self,value):
		return self.e >= value

	def __isub__(self,de):
		return self.__sub__(de)

	def __iadd__(self, de):
		return self.__add__(de)

	def __str__(self):
		return str(self.e)

	def __repr__(self):
		return str(self.e)

def clear_screen(): # https://www.geeksforgeeks.org/clear-screen-python/
	# import only system from os
	from os import system, name
	# import sleep to show output for some time period
	from time import sleep

	# for windows
	if name == 'nt':
		_ = system('cls')

    # for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')


class bbcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def p_color(input, file=True):  # Afficher avec une couleur
    if file:
        input = open(input, 'r').read()
    string = input.replace("[BLUE]", bbcolors.BLUE) \
        .replace("[GREEN]", bbcolors.GREEN) \
        .replace("[YELLOW]", bbcolors.YELLOW) \
        .replace("[RED]", bbcolors.RED) \
        .replace("[DEFAULT]", bbcolors.DEFAULT) \
        .replace("[BOLD]", bbcolors.BOLD) \
        .replace("[UNDERLINE]", bbcolors.UNDERLINE)
    return string


def print_INFO(time, energy):
    print('*'*80)
    print('** ', end='          ')
    print(p_color(f"Il est [GREEN][BOLD]{time2hours(time)}[DEFAULT]. Il te reste [BOLD][YELLOW]{energy} d'#NRJ[DEFAULT].",
                  file=False))
    print('*' * 80)
    return

def print_result_action(dt, de):
    txt = f"Cette action t'a pris [GREEN][BOLD]{dt} minutes[DEFAULT] et "
    if de > 0:
        txt += "tu as gagné "
    else:
        txt += "tu as perdu "
    txt += f"[YELLOW][BOLD]{de} point(s) d'#NRJ[DEFAULT]."

    print('*' * 80)
    print('** ', end='          ')
    print(p_color(txt, file=False))
    print('*' * 80)
    return
