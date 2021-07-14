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
        self.builder.create_sub_level(help="Input the name of one of the supported sites")
        self.builder.create_sub_parser("pornhub", help="Retrieve links from Pornhub")

        self.builder.add_sub_arg(1, "pornhub", 'search', metavar="search terms", help='Search Term (in quotations)',
                                 nargs='?')
        self.builder.add_sub_arg(1, "pornhub", '-p', '--pages', type=int, help='# of pages to scrape')
        self.builder.add_sub_arg(1, "pornhub", '-l', '--listname', default="list.txt", help='Name of save file')
        self.builder.add_sub_arg(1, "pornhub", '-x', '--premium',
                                 help='Use premium account, will require username and password in <username:password> format')
        self.builder.add_sub_arg(1, "pornhub", '-v', '--verbose', action='store_true',
                                 help='Prints titles to console so you know what you\'re grabbing')
        self.builder.add_sub_arg(1, "pornhub", '--premium-only', action="store_true",
                                 help='Retrieve only premium videos. (must have premium account)')
        self.builder.add_sub_arg(1, "pornhub", '-i', '--include', help='The category to filter into the search')
        self.builder.add_sub_arg(1, "pornhub", '-e', '--exclude',
                                 help='the categories to remove from the search(max=10). Example: "cat1,cat2,cat3,cat4"')
        self.builder.add_sub_arg(1, "pornhub", '--category-list', action="store_true",
                                 help='list of all available categories to filter through "(what keyword mean)"')
        self.builder.add_sub_arg(1, "pornhub", '--prod', choices=['home', 'pro'], help="production of the video")
        self.builder.add_sub_arg(1, "pornhub", '--min', '--min-dur', type=int, choices=[10, 20, 30],
                                 help='Minimum length of videos')
        self.builder.add_sub_arg(1, "pornhub", '--max', '--max-dur', type=int, choices=[10, 20, 30],
                                 help='Maximum length of videos')

