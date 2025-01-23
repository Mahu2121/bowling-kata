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

    PINS = "12345123451234512345"       # PINS == 92
    card = ScoreCard(PINS)
    assert 60 == card.get_score()

def test_missed_rolls():
    PINS = "9-9-9-9-9-9-9-9-9-9-"      # PINS == 68
    card = ScoreCard(PINS)
    assert 90 == card.get_score()

def test_score_spare():
    PINS = "5/5/5/5/5/5/5/5/5/5/5"
    card = ScoreCard(PINS)
    assert 150 == card.get_score()

def test_symbols_to_numbers():
    PINS = "5/XX4/1/7/2-23X12"
    card = ScoreCard(PINS)
    assert "55101046197320231012" == card.symbols_to_numbers()

def test_split_frames():

    PINS = "5/XX4/1/7/2-23X12"
    card = ScoreCard(PINS)
    assert [["5","/"],["X"],["X"],["4","/"],["1","/"],["7","/"],["2","-"],["2","3"],["X","1","2"]] == card.split_frames()

def test_two_strikes_in_extra_rolls():

    PINS = "9-9-9-9-9-9-9-9-9-XXX"
    card = ScoreCard(PINS)
    assert 111 == card.get_score()