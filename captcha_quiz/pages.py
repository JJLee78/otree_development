from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, cmp, distance_and_ok
from django.conf import settings


class Transcribe(Page):
    form_model = 'player'
    form_fields = ['transcribed_text']

    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_rounds
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'image_path': 'captcha_quiz/paragraphs/{}.jpg'.format(
                self.round_number),
            'reference_text': Constants.reference_texts[self.round_number - 1],
            'debug': False,
            'required_accuracy': 100,
            'page': page,
            'total': total,
            'progress': progress

        }

    def transcribed_text_error_message(self, transcribed_text):
        reference_text = Constants.reference_texts[self.round_number - 1]
        distance, ok = distance_and_ok(transcribed_text, reference_text,
                                       0)
        if ok:
            self.player.cmp_dst = distance
        else:
            return "The answer should be exactly the same as on the image."

    def before_next_page(self):
        self.player.payoff = 0


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            row = {
                'round_number': prev_player.round_number,
                'reference_text_length': len(Constants.reference_texts[prev_player.round_number - 1]),
                'transcribed_text_length': len(prev_player.transcribed_text),
                'distance': prev_player.levenshtein_distance,
            }
            table_rows.append(row)

        return {'table_rows': table_rows}

    def app_after_this_page(self, upcoming_apps):
        return "mpl"


page_sequence = [Transcribe]
