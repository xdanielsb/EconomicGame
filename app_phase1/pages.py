from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
	def is_displayed(self):
		if self.player.subsession.round_number == 1:
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
		vrange = [ x * 0.5 for x in range(3) ]
		return vrange

class Results(Page):
	pass

class ResultsWaitPage(WaitPage):
		body_text = "Hello, Could you wait a second, please?"
		def after_all_players_arrive(self):
			self.group.set_new_endowments()


class Results(Page):
  pass

page_sequence = [
  Intro,
	Contrib,
  ResultsWaitPage,
  Results,
]
