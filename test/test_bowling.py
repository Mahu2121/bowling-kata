import pytest
from src.scoreCard import ScoreCard



def test_score_card():

    card = ScoreCard("12345678911234567891")
    assert card


def test_get_pins():

    PINS = "12345678911234567891"
    card = ScoreCard(PINS)
    assert card.get_pins() == PINS


def test_normal_score():

    PINS = "12345678911234567891"       # PINS == 92
    card = ScoreCard(PINS)
    assert 92 == card.get_score_card_result(PINS)

def test_score_spare():
    PINS = "1234-6-8911234-6-891"      # PINS == 68
    card = ScoreCard(PINS)
    assert 68 == card.get_score_card_result(PINS)
