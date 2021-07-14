class AbstractScraper:
    """Abstract class to provide definition for a scraper"""
    def start(self):
        """Starts the scraper"""
        pass

    def late_init(self, args):
        """
        Provides a means to initialize the scraper at a later time
        :param args: Arguments retrieved from the commandline
        :return: None
        """
        pass
