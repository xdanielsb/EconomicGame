from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
	pass

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
