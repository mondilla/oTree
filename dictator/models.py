# -*- coding: utf-8 -*-
from otree.db import models
import otree.models
from otree.common import money_range

doc = """
Dictator game. Single Treatment. Two players, one of whom is the dictator.
The dictator is given some amount of money, while the other player is given nothing.
The dictator must offer part of the money to the other player.
The offered amount cannot be rejected.
Source code <a href="https://github.com/oTree-org/oTree/tree/master/dictator" target="_blank">here</a>.
"""


class Subsession(otree.models.BaseSubsession):

    name_in_url = 'dictator'


class Treatment(otree.models.BaseTreatment):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    allocated_amount = models.MoneyField(
        default=1.00,
        doc="""Initial amount allocated to the dictator"""
    )


class Match(otree.models.BaseMatch):

    # <built-in>
    treatment = models.ForeignKey(Treatment)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_match = 2

    offer_amount = models.MoneyField(
        default=None,
        doc="""Amount offered by the dictator"""
    )

    def offer_choices(self):
        """Range of allowed offers"""
        return

    def set_payoffs(self):
        p1 = self.get_player_by_index(1)
        p2 = self.get_player_by_index(2)

        p1.payoff = self.treatment.allocated_amount - self.offer_amount
        p2.payoff = self.offer_amount


class Player(otree.models.BasePlayer):

    # <built-in>
    match = models.ForeignKey(Match, null=True)
    treatment = models.ForeignKey(Treatment, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>


def treatments():

    return [Treatment.create()]