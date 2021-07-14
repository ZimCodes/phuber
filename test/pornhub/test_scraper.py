import os
from lib.pornhub.scraper import Scraper
from lib.command.phuber_args import PhuberArgs


class TestScraper:
    def test_single_page(self):
        """
        Tests to see if scraper can retrieve a full page
        :return: None
        """
        total_links = 24
        scraper = new_scraper("pornhub", "bright")
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
