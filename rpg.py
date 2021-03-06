# MAIN SCRIPT RPG TIF
import sys
import rpg_config as config
from rpg_functools import *
import random

from os import system, name

import pdb 

def credits():
    clear_screen()
    input("A faire")

def launch_video():
    open_file('./narration/rise_of_champetier.mp4')
    clear_screen()

def menu_principal():
    debug = True ############################### changer ici pour non debug !!!!
    while(True):
        menu_choice = '2' if debug else check_input(p_color('narration/menu_principal.txt'),['1','2','3','4'])
        if menu_choice == "1":
            launch_video()
        if menu_choice == "2":
            game(debug)
        if menu_choice == "3":
            credits()
        if menu_choice == "4":
            exit(0)
        clear_screen()



def die():
    clear_screen()
    print(p_color("[RED]CATASTROPHE ! \n[GREEN]Tiphaine[DEFAULT] a [RED]crevé[DEFAULT]. Elle a visiblement fait de très [RED]mauvais[DEFAULT] choix... Il faut recommencer"),file=False)
    menu_principal()


def game(DEBUG=False):

	# global variables
	time = config.start_hour * 60 # 16 hours
	energy = Energy(100)

	# needed for advancement
	badge = False
	gpu = False
	felipe_badge = False

	hamac_votes = ['ouardia', 'tiphaine', 'alexis']
	daoult_password = False #TODO: check if used
	coffee = False
	eaten = False
	huel = False

	# potential weapons
	selfie = True
	covid = False
	fungus = False
	mbti = False
	hamac_weapon = False

	# quests
	analysis = False
	diploma = False
	hamac_quest = False
	babyfoot = False
	whistleblower = False

	# Allies
	alexis = True
	paoletti = False
	holcman = False

	###############################
	# PROLOGUE
	###############################
	# Star Wars Init
	if not(DEBUG) : 
		
		input(p_color("narration/intro.txt"))
		clear_screen()
		# TBD: remove if video

		# Retour
		input(p_color("narration/retour.txt"))
		clear_screen()

		# Tutoriel
		input(p_color("narration/tutoriel.txt"))
		clear_screen()

	###############################
	# INITIAL SEQUENCE
	###############################
	print_INFO(time, energy)

	# wake-up
	snooze =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/matin/matin.txt"), ['T', 'F'])
	if DEBUG : 
		print(snooze)
	if snooze == 'T':
		time += config.snooze_dt
		energy += config.snooze_de

		print_result_action(config.snooze_dt, config.snooze_de)
		print(p_color("narration/matin/matin_snooze.txt"))

	else:
		rd = random.random()
		if rd <= config.wakeup_proba:
			# Tif manages to wakeup
			time += config.nonsnooze_dt
			energy += config.nonsnooze_de

			print_result_action(config.nonsnooze_dt, config.nonsnooze_de)
			print(p_color("narration/matin/matin_lever_success.txt"))

		else:
			#fail
			time += config.snooze_dt
			energy += config.nonsnooze_de

			print_result_action(config.snooze_dt, config.nonsnooze_de)

			print(p_color("narration/matin/matin_lever_fail.txt"))
	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()

	# bike

	bike_fight =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/bike/bike.txt"), ['T', 'F'])
	if DEBUG : 
		print(bike_fight)
	if bike_fight == 'T':
		time += config.bike_fight_dt
		energy += config.bike_fight_de

		print_result_action(config.bike_fight_dt, config.bike_fight_de)
		print(p_color("narration/bike/bike_fight.txt"))
	else:
		time += config.non_bike_fight_dt
		energy += config.non_bike_fight_de

		print(p_color("narration/bike/bike_no_fight.txt"))
		print_result_action(config.non_bike_fight_dt, config.non_bike_fight_de)

	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()
	# arrival
	if time <= config.morning_deadline * 60: # before 9am
		# meeting with Daoult
		time += config.daoult_talk_dt
		print(p_color("narration/arrivee_ibens/daoult/daoult.txt"))
		print_result_action(config.daoult_talk_dt, 0)
		if not(DEBUG):
			input()

		if bike_fight == 'T':
			time += config.daoult_fight_dt
			energy += config.daoult_fight_de

			print(p_color(
				"narration/arrivee_ibens/daoult/daoult2_si_agression.txt"))
			print_result_action(config.daoult_fight_dt, config.daoult_fight_de)
		else:
			# daoult does take the MBTI test
			time += config.daoult_test_mbti_dt
			mbti = True

			print(p_color(
				"narration/arrivee_ibens/daoult/daoult2_si_mbti.txt"))
			print_result_action(config.daoult_test_mbti_dt, 0)

	else: # after 10am
		time += config.swann_beer_dt
		mbti = True

		print(p_color(
			"narration/arrivee_ibens/swann/swann.txt"))
		print_result_action(config.swann_beer_dt, 0)

	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()

	# sysinfo

	convince_pv =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/sysinfo/pv.txt"), ["T", "F"])
	if DEBUG : 
		print(convince_pv)
	wait_sysinfo = False
	if convince_pv == 'T':
		rd = random.random()
		if rd <= config.pv_convincing_proba:
			# pv is convinced!
			time += config.pv_dt
			badge = True

			print(p_color("narration/sysinfo/pv_after.txt"))
			print_result_action(config.pv_dt, 0)
		else:
			# local var
			wait_sysinfo = True

			print(p_color("narration/sysinfo/pv_not_convinced.txt"))

	if convince_pv == 'F' or wait_sysinfo:
		# wait
		time += config.after_pv_dt
		print_result_action(config.after_pv_dt, 0)
		if not(DEBUG):
			input()

		phiphuong =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/sysinfo/deal_w_phiphuong.txt"),
								['T', 'F'])
		if DEBUG :
			print(phiphuong)
		if phiphuong == 'T':
			time += config.phiphuong_dt
			energy += config.phiphuong_de
			badge = True

			print(p_color("narration/sysinfo/phiphuong_after.txt"))
			print_result_action(config.phiphuong_dt,
								   config.phiphuong_de)
		else:
			time += config.bilel_dt
			badge = True

			print(p_color("narration/sysinfo/bilel.txt"))
			print_result_action(config.bilel_dt,0)

	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()

	# 6th floor
	meeting_auguste =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/sixth_floor_kitchen/arrival.txt"), ['T', 'F'])
	if DEBUG : 
		print(meeting_auguste)
	if meeting_auguste == 'T':
		time += config.auguste_meeting_dt
		energy += config.auguste_meeting_de
		covid = True

		print(p_color("narration/sixth_floor_kitchen/meeting_auguste.txt"))
		print_result_action(config.auguste_meeting_dt,
							   config.auguste_meeting_de)

	else:
		# stay with Pierre and Jerome
		listen_pj =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/sixth_floor_kitchen/choice_pierrejerome.txt"), ['T', 'F'])
		if DEBUG : 
			print(listen_pj)
		if listen_pj == 'T':
			time += config.resistance_talk_dt
			daoult_password = True

			print(
				p_color("narration/sixth_floor_kitchen/listen_pierrejerome.txt"))
			print_result_action(config.resistance_talk_dt, 0)
		else:
			rd = random.random()
			if rd < 0.5:
				# montessori talk
				time += config.montessori_talk_dt
				energy += config.montessori_talk_de

				print(p_color(
						"narration/sixth_floor_kitchen/montessori.txt"))
				print_result_action(config.montessori_talk_dt,
									   config.montessori_talk_de)

			else:
				# hydroponics talk
				time += config.hydroponics_talk_dt
				energy += config.hydroponics_talk_de

				print(p_color(
						"narration/sixth_floor_kitchen/hydroponics.txt"))
				print_result_action(config.hydroponics_talk_dt,
									   config.hydroponics_talk_de)

	print_INFO(time, energy)
	if not(DEBUG) :
		input()
	clear_screen()

	# in the lab
	lab_choice = random.choice(['1', '2', '3']) if DEBUG else check_input(p_color("narration/bureau/bureau.txt"), ['1', '2', '3'])
	if DEBUG : 
		print(lab_choice)
	# local variable toilets
	toilets = False
	if lab_choice == '3':
		# plants
		time += config.plants_dt
		print(p_color("narration/bureau/plantes.txt"))
		print_result_action(config.plants_dt, 0)

	elif lab_choice == '1':
		coffee = True
		energy += config.coffee_de
		time += config.coffee_dt

		print_result_action(config.coffee_dt, config.coffee_de) #TODO: check if order is ok between the 2 prints
		lab_choice = random.choice(['1', '2']) if DEBUG else check_input(p_color("narration/bureau/cafe.txt"),
								 ['1', '2'])
		if DEBUG : 
			print(lab_choice)

	if lab_choice == '2':
		# caca
		toilets = True
		rd = random.random()
		if rd < 0.5:
			# discuss her poop
			time += config.poop_talk_dt

			poop_email =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/bureau/caca_explication.txt"),
									 ['T', 'F'])
			if DEBUG : 
				print(poop_email)
			print_result_action(config.poop_talk_dt+config.poop_dt, 0)
		else:
			energy += config.poop_constipated_de

			poop_email =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/bureau/caca_constipee.txt"),
									 ['T', 'F'])
			if DEBUG : 
				print(poop_email)
			print_result_action(config.poop_dt, config.poop_constipated_de)

		time += config.poop_dt

		if poop_email == 'T':
			time += config.poop_email_dt
			energy += config.poop_email_de

			print_result_action(config.poop_dt, config.poop_constipated_de)
			print(random.choice(['1'])) if DEBUG else check_input(p_color("narration/bureau/reponse_mail.txt"), ['1'])
		else:
			print(random.choice(['1'])) if DEBUG else check_input(p_color("narration/bureau/toilettes_degueues_passer_outre.txt"),
						['1'])


	if not toilets:
		# Tif asphyxiates Alexis, he is not her allie anymore
		print(p_color("narration/bureau/asphyxier_alexis.txt"))
		alexis = False
		hamac_votes.remove('alexis')

	if DEBUG:
		print("\nIN THE LAB\n")
		print(f"alexis = {alexis}, hamac_votes = {hamac_votes}")

	print_INFO(time, energy)
	if not(DEBUG) :
		input()
	clear_screen()

	# email auguste
	ignore_email_auguste =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/bureau/mail_auguste.txt"),
									   ['T', 'F'])
	if DEBUG : 
		print(ignore_email_auguste)
	if ignore_email_auguste == 'T':
		time += config.auguste_email_answer_dt
		print(p_color("narration/bureau/ignorer_auguste.txt"))

	else:
		covid = True

		print(p_color("narration/bureau/engueuler_auguste.txt"))
		print_result_action(config.auguste_email_answer_dt, 0)


	if DEBUG:
		print('\nLAB')
		print(f'covid = {covid}, coffee = {coffee}, toilets = {toilets}, alexis = {alexis}')

	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()

	# 7th FLOOR
	time += config.floor7_dt
	print(p_color("narration/seventh_floor/seventh_floor_data.txt"))
	print_result_action(config.floor7_dt, 0)

	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()


	# Analysis
	print(p_color("narration/gpu/gpu.txt"))
	shifumi_output = shifumi(DEBUG)
	while not shifumi_output:
		time += config.shifumi_between_games_dt
		print_result_action(config.shifumi_between_games_dt, 0)
		shifumi_output = shifumi(DEBUG)

	gpu = True

	if DEBUG:
		print('\nSHIFUMI')
		print(f'gpu = {gpu}')

	print_INFO(time, energy)
	if not(DEBUG):
		input()
	clear_screen()

	# Analysis
	print('question_troll'+random.choice(['1', '2', '3', '4'])) if DEBUG else check_input(p_color("narration/analyse/question_troll.txt"), ['1', '2', '3', '4'])

	if coffee:
		time += config.analysis_if_coffee_dt
		energy -= config.analysis_if_coffee_de

		print(p_color("narration/analyse/avec_cafe.txt"))
		print_result_action(config.analysis_if_coffee_dt,
							config.analysis_if_coffee_de)
	else:
		promise_mathieu =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/analyse/sans_cafe.txt"),
									  ['T', 'F'])
		if DEBUG : 
			print(promise_mathieu)

		if promise_mathieu == 'T':
			time += config.promise_mathieu_dt
			energy -= config.analysis_de
			# mathieu is an allie
			hamac_votes.append('mathieu')
			print(p_color("narration/analyse/gentille_avec_mathieu.txt"))
			print_result_action(config.promise_mathieu_dt,
								config.analysis_de)
		else:
			time += config.non_promise_mathieu_dt
			energy -= config.analysis_de
			print(p_color("narration/analyse/pasgentille_avec_mathieu.txt"))
			print_result_action(config.promise_mathieu_dt, config.analysis_de)

	analysis = True

	if DEBUG:
		print('\nANALYSIS')
		print(f'analysis = {analysis}, coffee = {coffee}')

	print_INFO(time, energy)
	if not(DEBUG) :
		input()
	clear_screen()

	# Discussion with Alexis about admin problems
	print(p_color("narration/convaincre_le_monde/interlude.txt"))
	if alexis:
		print(p_color("narration/convaincre_le_monde/answer_alexis_if_caca.txt"))
	else:
		print(p_color("narration/convaincre_le_monde/answer_alexis_if_not_caca.txt"))
	if not(DEBUG) :
		input()

	# France & Guillaume encounters
	discuss_france =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/convaincre_le_monde/discussion_france_beginning.txt"),
								 ['T', 'F'])
	if DEBUG : 
		print(discuss_france)
	if discuss_france == 'T':
		print(p_color("narration/convaincre_le_monde/discussion_france_follow.txt"))
		print_result_action(config.france_dt, config.france_e - energy.e)

		time += config.france_dt
		energy = Energy(config.france_e)
		huel = True
		hamac_votes.append('france')

	print_INFO(time, energy)
	if not(DEBUG) :
		input()
	clear_screen()


	discuss_guillaume =random.choice(['T', 'F'])  if DEBUG else check_input(p_color("narration/convaincre_le_monde/choice_discussion_guillaume.txt"),
									['T', 'F'])
	if DEBUG : 
		print(discuss_guillaume)
	if discuss_guillaume == 'T':
		time += config.guillaume_dt
		energy += config.guillaume_de
		hamac_votes.append('guillaume')

		print(p_color("narration/convaincre_le_monde/discussion_guillaume.txt"))
		print_result_action(config.guillaume_dt, config.guillaume_de)

	if DEBUG:
		print('\nF&G ENCOUNTERS')
		print(f'hamac_votes = {hamac_votes}')

	print_INFO(time, energy)
	if not(DEBUG) :
		input()
	clear_screen()

	if type(energy) is int :
		pdb.set_trace()
	if energy.e <= 0 :
		die()
	if time <= 14 * 60:
		print('You will never end this day : too much procrastination --> GAME OVER ! Recommence !')
		return
	assert time <= 14 * 60 # before 2pm
	assert energy.e > 0
	assert badge
	assert analysis
	assert gpu


	##########################################
	# PARALLEL QUESTS
	##########################################

	while (time < config.end_hour * 60 and energy > 0) and ((not diploma) or (not hamac_quest) or (not babyfoot)): #TODO: check constraints

		if DEBUG:
			print(f"time = {time}, energy = {energy}")
			print(f"diplome = {diploma}, hamac_quest = {hamac_quest}, babyfoot = {babyfoot}")

		to_display_menu = display_menu(time, hamac_quest, diploma, babyfoot, eaten)

		menu_choice = str(random.choice(list(to_display_menu.keys()))) if DEBUG else input('\n'.join([f'Tape {key} pour {value}' for key, value in to_display_menu.items()]) + '\n')
		if DEBUG : 
			print(menu_choice)
			#pdb.set_trace()
		# HAMAC
		# 14 people max can vote
		if menu_choice == '0':
			if ('France' in hamac_votes) and not ('Guillaume' in hamac_votes):
				hamac_votes.append('Guillaume')

			# TODO: verify hamac_votes has no redundacy
			assert len(hamac_votes) == len(set(hamac_votes))

			print(f'Il y a {len(hamac_votes)} personnes pour le hamac sur 14.')

			# try convince some people
			# TODO: il manque les fioritures la: le sprobas qui changent en fonction de la conversation
			convince_hamac =random.choice(['T', 'F'])  if DEBUG else input("Tu essayes de convaincre Felipe ? [T/F]")
			if DEBUG : 
				print(convince_hamac)
			if convince_hamac == 'T':
				rd = random.random()
				time += config.convince_felipe_dt
				energy += config.convince_felipe_de
				if rd < config.convince_felipe_proba:
					hamac_votes.append('felipe')
					print("Tu as convaincu Felipe.")

			convince_hamac =random.choice(['T', 'F'])  if DEBUG else input("Tu essayes de convaincre Tony ? [T/F]")
			if DEBUG : 
				print(convince_hamac)
			if convince_hamac == 'T':
				rd = random.random()
				time += config.convince_tony_dt
				energy += config.convince_tony_de
				if rd < config.convince_tony_proba:
					hamac_votes.append('tony')
					print("Tu as convaincu Tony.")

			convince_hamac =random.choice(['T', 'F'])  if DEBUG else input("Tu essayes de convaincre Lisa ? [T/F]")
			if DEBUG : 
				print(convince_hamac)
			if convince_hamac == 'T':
				rd = random.random()
				time += config.convince_lisa_dt
				energy += config.convince_lisa_de
				if rd < config.convince_lisa_proba:
					hamac_votes.append('lisa')
					print("Tu as convaincu Lisa.")

			if len(hamac_votes) >= config.n_people_hamac_vote:
				print(f'Quete HAMAC reussie !')
				hamac_weapon = True
				energy += config.winning_hamac_de
			else:
				# couch with auguste
				covid = True
				energy += config.loosing_hamac_de

			time += config.hamac_quest_dt
			hamac_quest = True

			if DEBUG:
				print('\nHAMAC')
				print(f'hamac_votes = {hamac_votes}, hamac = {hamac_weapon}')
				print(f'time = {time2hours(time)}; energy={energy}\n')


		# DIPLOMA
		elif menu_choice == '1':
			if time >= config.admin_deadline * 60:
				# after 6 pm
				time = config.end_hour * 60
				break

			# Lina's signature sequence
			if alexis:
				time += config.if_alexis_lina_dt
			else:
				if time <= config.admin_lina_deadline * 60:
					# before 2 pm
					time = 14 * 60
				time += config.if_not_alexis_lina_dt

			# Paoletti's signature sequence
			if alexis:
				time += config.if_alexis_paoletti_dt
			else:
				time += config.if_not_alexis_paoletti_dt

			# Auguste's signature sequence
			if alexis:
				time += config.if_alexis_auguste_dt
			else:
				time += config.if_not_alexis_auguste_dt

			# diploma quest achieved
			diploma = True

			# meet with Felipe
			felipe_badge = True

			if DEBUG:
				print('\nDIPLOMA')
				print(f'diploma = {diploma}')
				print(f'time = {time2hours(time)}; energy={energy}\n')


		# BABYFOOT
		elif menu_choice == '2':
			if fungus:
				energy += config.if_fungus_de

			# compliment Maxime and Nikita
			hamac_votes.extend(['nikita', 'maxime'])

			daoult_password = True

			time += config.baby_dt

			# choose between paoletti and holcman
			paoletti_vs_holcman = random.choice(['0', '1']) if DEBUG else input('De Pierre Paloetti et David Holcman, qui choisis-tu comme allie contre Daoult? [0/1]')
			if DEBUG : 
				print(paoletti_vs_holcman)
			if paoletti_vs_holcman == '0':
				# choose paoletti
				paoletti = True
			else:
				holcman = False

			# babyfoot quest achieved
			babyfoot = True

			if DEBUG:
				print('\nBABYFOOT')
				print(f'babyfoot = {babyfoot}, paoletti = {paoletti}, holcman = {holcman},')
				print(f'daoult_password = {daoult_password}, fungus = {fungus}')
				print(f'time = {time2hours(time)}; energy = {energy}\n')

		# LUNCH
		elif menu_choice == '3':
			if time <= config.tony_lunch_deadline * 60:
				# lunch with Tony
				selfie = True
			else:
				# eat with Solene and Elise
				hamac_votes.extend(['elise', 'raphael', 'solene'])
				# cure fungal infection?
				fungal_choice = random.choice(['0', '1']) if DEBUG else input("Pour ton champignon, tu suis le conseil d'Elise [0] ou de Solene[1] ?")
				if DEBUG : 
					print(fungal_choice)
				if fungal_choice == '0':
					# elise: the fungal infection grows worse
					fungus = True
				else:
					#solene: the fungal infection is cured
					energy += config.fungal_de

			time += config.lunch_dt
			eaten = True

			if DEBUG:
				print('\nLUNCH')
				print(f'hamac_votes = {hamac_votes}, selfie={selfie}')
				print(f'time = {time2hours(time)}; energy={energy}\n')

		# NAP
		else: #if menu_choice == '4':
			energy += config.nap_de
			time += config.nap_dt

			if DEBUG:
				print('\nNAP')
				print(f'time = {time2hours(time)}; energy={energy}\n')


	if time >= config.end_hour * 60 or energy < 0:
		print('GAME OVER ! Recommence !')
		return
	#pdb.set_trace()
	#assert babyfoot
	#assert hamac_quest
	#assert diploma
	assert (covid or fungus or hamac_weapon)


	########################################
	# WHISTLEBLOWER QUEST
	########################################

	office_check = random.choice(['0', '1','2','3']) if DEBUG else input("Choisis-tu d'aller inspecter le bureau de Daoult [0], de Pierre Paoletti [1], de David Holcman [2] ou aucun [3]?")
	if DEBUG : 
		print(office_check)
	if office_check == '0':
		if mbti:
			print("Tu trouves qqchose chez Daoult")
			energy += config.if_mbti_daoult_office_de
		else:
			print("Tu ne trouves rien chez Daoult")
			energy += config.not_mbti_adoult_office_de

	elif office_check =='1':
		if paoletti:
			print("Ton allie Paoletti est mechant")
			energy += config.allie_is_evil_de
		else:
			print("Tu ne trouves rien chez Paoletti")
	elif office_check == '2':
		if paoletti:
			print("Tu ne trouves rien chez Holcman")
		else:
			print("Ton allie Holmcan est mechant")
			energy += config.allie_is_evil_de

	if office_check != '3':
		time += config.whistleblower_dt
		if DEBUG:
			print('\nWHISTLEBLOWER')
			print(f'time = {time2hours(time)}; energy={energy}\n')


	whistleblower_choice =random.choice(['T', 'F'])  if DEBUG else input('Fais tu fuiter dans mediapart le scandale du corona-cola ? [T/F]')
	if DEBUG : 
		print(whistleblower_choice)
	if whistleblower_choice == 'T':
		whistleblower = True


	##########################################
	# FINAL QUEST
	##########################################

	if time >= config.end_hour * 60 or energy < 0:
		print('GAME OVER ! Recommence !')
		return

	if whistleblower:
		allie_confrontation = random.choice(['T', 'F'])  if DEBUG else input("Confrontes-tu ton allie ? [T/F]")
		if DEBUG : 
			print(allie_confrontation)
		if allie_confrontation == 'T':
			energy += config.confrontation_allie_de

		if huel:
			huel_choice = random.choice(['T', 'F'])  if DEBUG else input("Veux-tu un peu de huel? [T/F]")
			if DEBUG : 
				print(huel_choice)
			if huel_choice == 'T':
				energy = Energy(100) ### change 100

		daoult_proposition =  random.choice(['T', 'F'])  if DEBUG else input("Daoult te propose un poste permanent avec mobilite. Tu acceptes ? [T/F]")
		if DEBUG : 
			print(daoult_proposition)
		energy += config.daoult_proposition_de
		if daoult_proposition == 'T':
			if energy >= config.trust_daoult_energy_threshold:
				# epilogue 1
				print("Tu as gagne - Sort of")
				return
			else:
				print("GAME OVER! Recommence !")
				return
		else:
			if energy >= config.dont_trust_daoult_energy_threshold:

				daoult_weapon_choice = str(random.choice(list(daoult_attack(covid, hamac_weapon, fungus)[1]))) if DEBUG else input(daoult_attack(covid, hamac_weapon, fungus)[0])
				if DEBUG : 
					print(daoult_weapon_choice)
				if daoult_weapon_choice == '0':
					print("Tu tues Daoult avec le covid")
					# epilogue 2
				elif daoult_weapon_choice == '1':
					print("Tu emprisonnes Daoult avec le piege hamac")
					# epilogue 3
				elif daoult_weapon_choice == '2':
					print("Tu contamines Daoult avec ton champignon")
					# epilogue 4

					allie_choice = random.choice(['T', 'F'])  if DEBUG else input("Choisis-tu de changer ton choix pour le prochain directeur d'institut ? [T/F]")
					if DEBUG : 
						print(allie_choice)
					if allie_choice == 'T':
						# exchange
						paoletti = not paoletti
						holcman = not holcman

					print("Tu as gagne - Sort of")
					return

			else:
				print("GAME OVER! Recommence !")
				return

	else:
		# not whistleblower

		# fight with allie
		lie_or_not = random.choice(['T', 'F'])  if DEBUG else input("Tu n'as pas fait fuiter les infos. Ments tu a ton allie ? [T/F]")
		if DEBUG : 
			print(lie_or_not)
		if lie_or_not == 'T':
			# need to fight
			energy += config.lie_allie_fight_de
			# loose allie
			paoletti = False
			holcman = False
		else:
			energy += config.dont_lie_allie_fight_de

		if energy < 0:
			print("GAME OVER! Recommence !")
			return

		if huel:
			huel_choice = random.choice(['T', 'F'])  if DEBUG else input("Veux-tu un peu de huel? [T/F]")
			if DEBUG : 
				print(huel_choice)
			if huel_choice == 'T':
				energy = Energy(100) ### change 100

		if paoletti or holcman:
			# she still has an allie
			fight_daoult_or_both = random.choice(['0', '1']) if DEBUG else input("Choisis-tu d'attaquer Daoult [0] ou les deux [1] ?")
			if DEBUG : 
				print(fight_daoult_or_both)
			if fight_daoult_or_both == '0':
				# epilogue 4
				print("Tu as gagne - Sort of")
				return
			elif fight_daoult_or_both == '1':
				# fight both
				# not enough energy!
				print("GAME OVER! Recommence !")
				return

		else:
			# no more allie
			if (covid and energy >= config.if_covid_convince_daoult_energy_threshold):
				# epilogue 6
				print("Tu as gagne - Sort of")
				return
			elif (not covid and energy >= config.not_covid_convince_daoult_energy_threshold):
				# epilogue 7
				print("Tu as gagne - Sort of")
				return
			else:
				# not enough energy!
				print("GAME OVER! Recommence !")
				return

	if DEBUG:
		print("/!\\ No return - Pb")


if __name__ == '__main__':
	#game(DEBUG=True)
    menu_principal()
