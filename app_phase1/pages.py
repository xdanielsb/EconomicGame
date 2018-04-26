from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
	def is_displayed(self):
		if self.player.round_number == 1:
			return True
				
	def vars_for_template(self):
		vars = {
			'number_players': len(self.group.get_players()),
			'endowment': self.session.config['endowment'],
			'total_rounds': Constants.num_rounds,
			'total_rounds_phase_two': 2,
		}
		return vars

class Contrib(Page):
	form_model = "player"
	form_fields = ["contribution"]
	
	def contribution_choices(self):
		vrange = currency_range(c(0), c(1), c(0.5))
		return vrange
	
	def vars_for_template(self):
		vars = {
			'left_money' : self.player.participant.vars["endowment"],
		}
		return vars

class Results(Page):
	def is_displayed(self):
		if self.round_number < Constants.num_rounds:
			return True
  
	def vars_for_template(self):
		info_players = []
		#for player in self.group.get_players():
		for player in self.player.get_others_in_group():
			info_player = {}
			info_player["id"] = player.participant.id_in_session
			info_player["contribution_last_round"] =  player.participant.vars["contribution_last_round"]
			info_player["total_saving"] = player.participant.vars["endowment"]
			info_players.append(info_player)
		vars = {
			'info_players': info_players,
			'id': self.player.participant.id_in_session,
			'contribution_last_round': self.player.participant.vars["contribution_last_round"],
			'total_saving': self.player.participant.vars["endowment"],
		}
		return vars

class FinalResults(Page):
	def is_displayed(self):
		if self.round_number  == Constants.num_rounds:
			return True
	
	def vars_for_template(self):
		vars = {
			'pay_off' :self.player.savings,
			'others_pay_off' : [ x.savings for x in self.player.get_others_in_group()]
		}
		return vars

class ResultsWaitPage(WaitPage):
		body_text = "Hello, Could you wait a second, please?"
		def after_all_players_arrive(self):
			if self.round_number == Constants.num_rounds:
				self.group.set_pay_offs()
			else:
				self.group.set_new_endowments()

page_sequence = [
  Intro,
	Contrib,
  ResultsWaitPage,
  Results,
	FinalResults,
]
