import os

from lib.pornhub.scraper import Scraper
from lib.command.phuber_args import PhuberArgs


class TestScraper:
    def test_keyword_search(self):
        """
        Tests Scraper to retrieve a full page using basic keyword search
        :return: None
        """
        total_links = 20
        scraper = new_scraper("pornhub", "bright")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_cat_search(self):
        """
        Tests Scraper to retrieve a full page using basic category search
        :return: None
        """
        total_links = 32
        scraper = new_scraper("pornhub", "--cat-search", "cartoon")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_keyword_include(self):
        """
        Tests Scraper to retrieve a full page using basic keyword search with include filter
        :return: None
        """
        total_links = 20
        scraper = new_scraper("pornhub", "pool", "-i", "party")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_cat_include(self):
        """
        Tests Scraper to retrieve a full page using basic category search with include filter
        :return: None
        """
        total_links = 32
        scraper = new_scraper("pornhub", "--cat-search", "-i", "feet", "cartoon")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_keyword_gay_search(self):
        """
        Tests Scraper to retrieve a full page using basic keyword search in the gay section
        :return: None
        """
        total_links = 20
        scraper = new_scraper("pornhub", "!bright")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_cat_gay_search(self):
        """
        Tests Scraper to retrieve a full page using basic category search in gay section
        :return: None
        """
        total_links = 32
        scraper = new_scraper("pornhub", "--cat-search", "!group")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_keyword_gay_include(self):
        """
        Tests Scraper to retrieve a full page using basic keyword search in the gay section
        with include filter
        :return: None
        """
        total_links = 19
        scraper = new_scraper("pornhub", "-i", "!fetish", "!bright")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")

    def test_cat_gay_include(self):
        """
        Tests Scraper to retrieve a full page using basic category search in gay section with
        include filter
        :return: None
        """
        total_links = 16
        scraper = new_scraper("pornhub", "--cat-search", "-i", "!casting", "!group")
        scraper.start()
        with open("list.txt", 'r') as file:
            assert len(file.readlines()) == total_links
        os.remove("list.txt")


def new_scraper(*args):
    """
    Get a new Scraper object
    :param args: Commandline arguments
    :return: Scraper
    """
    return Scraper(PhuberArgs().get_args(*args))
