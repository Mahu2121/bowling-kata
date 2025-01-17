import pytest
from src.scoreCard import ScoreCard



def test_score_card():

    card = ScoreCard("1234567891")
    assert card


def test_get_pins():

    PINS = "1234567891"
    card = ScoreCard(PINS)
    assert card.get_pins() == PINS 


def test_normal_score():

    PINS = "1234567891"       # PINS == 46
    card = ScoreCard(PINS)                
    assert 46 == card.get_score_card_result(PINS)

def test_():
    PINS = "1234-6-891"      # PINS == 34    
    card = ScoreCard(PINS)
    assert 34 == card.get_score_card_result(PINS)
