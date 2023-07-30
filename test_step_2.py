import pytest

from challenge_2 import get_desired_court, format_output

# This fake data should ideally be in a conftest file, but I was having issues with that
fake_court_data = [
    {"name": "Unseelie Court",
     "types": ["Fairy Court"],
     "dx_number": "777 Feywild 7",
     "distance": 0.0
     },
    {"name": "Really important court",
     "types": ["High Court"],
     "dx_number": "12312 London 12",
     "distance": 1
     },
    {"name": "Less important court",
     "types": ["High Court", "Zoning Court"],
     "dx_number": None,
     "distance": 50
     }
]

fake_people = [{"person_name": "Dude who wants an existing court",
               "home_postcode": "NR2 2EQ",
                "looking_for_court_type": "Fairy Court"}]


# Tests for get desired court


def test_no_court_found(capsys):

    assert get_desired_court(
        "Non-existent court", fake_court_data) == None

    capture = capsys.readouterr()
    assert capture.out == "-----------------------------\n\
NO COURT FOUND\n\
-----------------------------\n"


def test_court_found():
    assert get_desired_court(
        "Fairy Court", fake_court_data) == {"name": "Unseelie Court",
                                            "types": ["Fairy Court"],
                                            "dx_number": "777 Feywild 7",
                                            "distance": 0.0
                                            }


def test_first_match_chosen():
    assert get_desired_court("High Court", fake_court_data) == {"name": "Really important court",
                                                                "types": ["High Court"],
                                                                "dx_number": "12312 London 12",
                                                                "distance": 1
                                                                }


# tests for format_output

def test_good_data():
    assert format_output(
        fake_people[0], fake_court_data[0]) == \
        """Person Name: Dude who wants an existing court\n\
Home Postcode: NR2 2EQ\n\
Looking For: Fairy Court\n\n\
Court Name: Unseelie Court\n\
DX number: 777 Feywild 7\n\
Straight Line Distance: 0.0 Miles \n-----------------------------"""


def test_no_DX():
    assert format_output(fake_people[0], fake_court_data[2]) == \
        """Person Name: Dude who wants an existing court\n\
Home Postcode: NR2 2EQ\nLooking For: Fairy Court\n\n\
Court Name: Less important court\n\
DX number: Not Found\nStraight Line Distance: 50 Miles \n-----------------------------"""
