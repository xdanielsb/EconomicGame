from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'app_phase1'
	players_per_group = None
	num_rounds = 3

class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	def set_new_endowments(self):
		players  = self.get_players()
		print("$$$$$$$$$$$$$$$$$$$$$$")
		for player in players:
			print(player.contribution)
		


class Player(BasePlayer):
	endowment = models.FloatField()
	contribution = models.FloatField(doc="Saving by each player", widget=widgets.RadioSelectHorizontal, label="How much do you want to contribute")

	
