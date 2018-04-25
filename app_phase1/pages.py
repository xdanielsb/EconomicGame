from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
	def vars_for_template(self):
		vars = {
			'number_players': len(self.group.get_players()).
			'endowment': self.session.config['endowment'],
			'total_rounds': Constants.num_rounds,
			'total_rounds_phase_two': 2,
		}
		return vars
class Contrib(Page):
	pass

class Results(Page):
	pass

class ResultsWaitPage(WaitPage):
  def after_all_players_arrive(self):
      pass

class Results(Page):
  pass

page_sequence = [
  Intro,
	Contrib,
  ResultsWaitPage,
  Results,
]
