"""
Chapitre 11.1
Classes pour représenter un personnage.
"""


import random

import utils

class Weapon:
	"""
	Une arme dans le jeu.
	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	def __init__(self,name,power,min_level = 1):
		self.name = name
		self.power = power
		self.min_level = min_level


	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed",20,1)


class Character:
	"""
	Un personnage dans le jeu
	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self,name,max_hp,attack,defense,level = 1):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.hp = max_hp
		self.weapon = Weapon(None,None)










def deal_damage(attacker, defender):
	crit = random.choices([1,2],weights=[0.9375,1])[0]
	random1 = random.randint(85,100)/100
	modifier = float(crit)*random1
	dommage =(((((2*attacker.level/5)+2)*attacker.weapon.power*(attacker.attack/defender.defense))/50)+2)*modifier
	return dommage


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attaquant = c1
	defenseur = c2
	turn = 0
	print(f"{attaquant.name} starts a battle with {defenseur.name}")
	while attaquant.hp > 0 and defenseur.hp > 0:
		print(f"{attaquant.name} used {attaquant.weapon.name}")
		print(f"	{defenseur.name} took {deal_damage(attaquant,defenseur)}")
		defenseur.hp -= deal_damage(attaquant,defenseur)
		attaquant,defenseur = defenseur,attaquant
		turn += 1


	if attaquant.hp > 0:
		print(f"{attaquant.name} won the battle")
	else:
		print(f"{defenseur.name} won the battle")
	return turn

c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

turns = run_battle(c1, c2)
print(f"The battle ended in {turns} turns.")

