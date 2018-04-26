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
	def creating_session(self):
		if 1 == self.round_number:
			self.session.config["total_savings"] = 0
			for group in self.get_groups():
				for player in group.get_players():
					player.participant.vars["endowment"] = self.session.config["endowment"]

class Group(BaseGroup):

	def set_new_endowments(self):
		players  = self.get_players()
		for player in players:
			print(player.contribution)
			player.participant.vars["contribution_last_round"] = player.contribution
			player.participant.vars["endowment"] = player.participant.vars["endowment"] - player.contribution
		total_savings = sum ( [x.contribution for x  in players] )
		self.session.config["total_savings"]  = self.session.config["total_savings"] + total_savings

	def set_pay_offs(self):
		players = self.get_players()
		total_players = len(players)
		pay_off = self.session.config["total_savings"] / total_players
		print("$$$$$$$$$$$$$$$$$$")
		print("total savings {} ".format(self.session.config["total_savings"]))
		print("Money per participant {}".format(pay_off))

		for player in players:
			player.savings = pay_off + player.participant.vars["endowment"]


class Player(BasePlayer):
	endowment = models.CurrencyField()
	savings = models.CurrencyField()
	contribution = models.CurrencyField(doc="Saving by each player", widget=widgets.RadioSelectHorizontal, label="How much do you want to contribute")

	
