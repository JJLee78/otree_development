# <imports>
from otree.api import Currency as c
from otree.constants import BaseConstants
# </imports>

class Constants(BaseConstants):
    num_choices = 500
    probability = 50.00
    sure_payoff = 160.00

    delta = 80.00
    buttons = True
    progress_bar = True
    instructions = True
    results = False

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- oTree Settings (Don't Modify) --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    name_in_url = 'captcha_quiz'
    players_per_group = None
    num_rounds = num_choices
