import unittest
import pyfiglet
from project import update_user_guess
from project import get_missing_letters
from project import load_words_chosen_category
from project import load_stickman
from project import show_goodbye
from project import start_program

class TestHangmanFunctions(unittest.TestCase):
    def test_update_user_guess(self):
        assert update_user_guess("flower", "_lowe_", "r") == "_lower"

        assert update_user_guess("bread", "_re_d", "a") == "_read"


    def test_get_missing_letters(self):
        assert get_missing_letters("ford", "___d") == "for"

        assert get_missing_letters("flower", "_lowe_") == "fr"


    def test_load_words_chosen_category(self):
        assert isinstance(load_words_chosen_category("cars"), list)

        words = load_words_chosen_category("cars")
        assert "bmw" in words

        words = load_words_chosen_category("sports")
        assert "golf" in words

        words = load_words_chosen_category("countries")
        assert "austria" in words


    def test_load_stickman(self):
        assert isinstance(load_stickman(), list)


    def test_show_goodbye(self):
        assert isinstance(show_goodbye(), pyfiglet.FigletString)


    def test_start_program(self):
        assert isinstance(start_program(), pyfiglet.FigletString)


if __name__ == "__main__":
    unittest.main()
