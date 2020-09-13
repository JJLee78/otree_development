from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

doc = """
Captcha quiz, release 1.0.1, Made by JJ(jaejun.lees@gmail.com)
"""


def cmp(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def distance_and_ok(input_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = cmp(input_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok


class Constants(BaseConstants):
    name_in_url = 'captcha_quiz'
    players_per_group = None
    progress_bar = True
    reference_texts = [
        "W93BX",
        "JA3V8",
        "RBSKW",
        "HJ9PV",
        "TSMS9",
        "459CT",
        "R84CH",
        "D4TSH",
        "3M56R",
        "HAPK3",
    ]

    num_rounds = len(reference_texts)

    allowed_error_rates = [0, 0.03]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    transcribed_text = models.StringField()
    cmp_dst = models.IntegerField()
