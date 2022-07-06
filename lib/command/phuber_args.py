from .builder import CommandBuilder


class PhuberArgs:
    """Setup the commandline parser builder to retrieve a list of arguments from the commandline"""

    def __init__(self):
        """Initialize PhuberArgs object"""
        self.builder = CommandBuilder(prog="PHUBER", description='Phuber Link Retriever')

    def get_args(self, *args):
        """
        Gets the arguments created by the CommandBuilder
        :param args: The arguments to simulate placing into the commandline
        :return: Arguments from the commandline (Namespace object)
        """

        self.pornhub_setup()
        return self.builder.get_args(*args)

    def pornhub_setup(self):
        """
        Build the parser for Pornhub option/command configurations
        :return: None
        """
        sub_name = "pornhub"
        self.builder.create_sub_level(help="Input the name of one of the supported sites")
        self.builder.create_sub_parser(sub_name, help="Retrieve links from Pornhub")

        self.builder.add_sub_arg(1, sub_name, 'search', metavar="search keywords",
                                 help='Search using keywords or by a category if --cat-search is '
                                      'enabled',
                                 nargs='?')
        self.builder.add_sub_arg(1, sub_name, '--cat-search', action="store_true",
                                 help="Search by a" \
                                      "category " \
                                      "instead of by keywords. See category list for options")
        self.builder.add_sub_arg(1, sub_name, '-p', '--pages', type=int,
                                 help='# of pages to scrape')
        self.builder.add_sub_arg(1, sub_name, '-l', '--list-name', default="list.txt",
                                 help='Name of save file')
        self.builder.add_sub_arg(1, sub_name, '-x', '--premium',
                                 help='Use premium account, will require username and password in <username:password> format')
        self.builder.add_sub_arg(1, sub_name, '-v', '--verbose', action='store_true',
                                 help='Prints titles to console so you know what you\'re grabbing')
        self.builder.add_sub_arg(1, sub_name, '--premium-only', action="store_true",
                                 help='Retrieve only premium videos. (must have premium account)')
        self.builder.add_sub_arg(1, sub_name, '-i', '--include',
                                 help='The category to filter into the search.')
        self.builder.add_sub_arg(1, sub_name, '-e', '--exclude',
                                 help='the categories to remove from the search(max=10). Example: "cat1,cat2,cat3,cat4"')
        self.builder.add_sub_arg(1, sub_name, '--category-list', action="store_true",
                                 help='list of all available categories to filter through "(what keyword mean)"')
        self.builder.add_sub_arg(1, sub_name, '--prod', choices=['home', 'pro'],
                                 help="production of the video")
        self.builder.add_sub_arg(1, sub_name, '--min', '--min-dur', type=int, choices=[10, 20, 30],
                                 help='Minimum length of videos')
        self.builder.add_sub_arg(1, sub_name, '--max', '--max-dur', type=int, choices=[10, 20, 30],
                                 help='Maximum length of videos')
        self.builder.add_sub_arg(1, sub_name, '--order',
                                 choices=['viewed', 'top', 'longest', 'hottest', 'newest'],
                                 help="Changes ordering of videos in search results. Default: (by featured/relevancy/top sold)")
        self.builder.add_sub_arg(1, sub_name, '--order-time',
                                 choices=['yearly', 'monthly', 'weekly', 'daily', 'all'],
                                 help="Changes ordering of videos in search results by time. *Only applicable for 'top' & 'viewed' options."
                                      "Default (auto)")
        self.builder.add_sub_arg(1, sub_name, '--promo', choices=['premium', 'paid'],
                                 help="Changes filter videos based on promotion. *Only applicable during category search only. Default (all)")
        self.builder.add_sub_arg(1, sub_name, '--hd', action='store_true',
                                 help="Show only HD videos.")
        self.builder.add_sub_arg(1, sub_name, '--loc', metavar="LOCATION", help="Changes ordering "
                                                                                "of videos based "
                                                                                "on locations "
                                                                                "around the "
                                                                                "world. "
                                                                                "Only "
                                                                                "applicable "
                                                                                "during category "
                                                                                "search with "
                                                                                "either 'hottest' or 'viewed' used. "
                                                                                "Default:(auto)")
