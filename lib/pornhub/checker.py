from ..command.args_checker import ArgsChecker
from .data import Data
import argparse
import tabulate


class Checker(ArgsChecker):
    """Checks & modifies the commandline arguments received"""

    def __init__(self, phuber_args):
        super().__init__(phuber_args)

    def arg_errors(self):
        """
        Check if there are any errors from user input
        parser: parse arguments received from user input
        premium: login credentials for premium account
        premium_only: show premium videos only (premium account required!)
        search: what to search for (required)
        show_category_list: display list of available categories to use while filtering
        :return: None
        """
        if not self.args.premium and self.args.premium_only:
            raise argparse.ArgumentTypeError(
                "Must login to premium account to use '--premium-only' option!")
        if (self.args.order != "top" and self.args.order != "viewed") and self.args.order_time is \
                not None:
            raise argparse.ArgumentTypeError(f"--order='{self.args.order}' cannot be used with "
                                             "--order-time argument! Reason: There is no time "
                                             "filter available for this "
                                             "--order type.")
        if self.args.promo is not None and not self.args.cat_search:
            raise argparse.ArgumentTypeError("The --promo option must be used with --cat-search "
                                             "enabled!")
        if (self.args.order != "hottest" and self.args.order != "viewed") and \
                self.args.cat_search and self.args.loc is not None:
            raise argparse.ArgumentTypeError(f"--order='{self.args.order}' cannot be used with "
                                             "--loc argument! Reason: There is no location filter "
                                             "available for this --order type.")
        if self.args.loc is not None and self.args.loc not in Data.location_codes:
            raise argparse.ArgumentTypeError(f"--loc='{self.args.loc}' cannot be found in the list "
                                             f"of locations! Please pick a valid "
                                             f"location from the location list.")
        if self.args.cat_search and not self.args.search.lower() in Data.category_codes:
            self.__category_error("search", self.args.search)
        if self.args.cat_search and self.args.include and not self.args.include.lower() in \
                                                              Data.category_codes:
            self.__category_error("include", self.args.include)
        if self.args.exclude:
            items = self.args.exclude.split(',')
            for x in items:
                if x not in Data.category_codes:
                    self.__category_error("exclude", x)
        if not self.args.cat_search and self.args.loc:
            raise argparse.ArgumentTypeError(f"'--loc' must be used with '--cat-search' enabled!")

    def __category_error(self, arg_name, val):
        raise argparse.ArgumentTypeError(f"--{arg_name}='{val}' cannot be found in the list "
                                         f"of categories! Please pick a valid "
                                         f"category from the category list.")

    def arg_checks(self):
        self.__page_check()

    def __page_check(self):
        """
        Checks whether or not # of pages has been specified
        :returns None
        """
        if not self.args.pages:
            self.args.pages = 1

    @staticmethod
    def print_categories():
        """
        Print out categories that can be used for filtering the search
        :return: None
        """
        temp_list = [[x] for x in Data.category_codes]
        temp_list.sort()

        print(tabulate.tabulate(temp_list, headers=["Category List"], tablefmt="fancy_grid"))

    @staticmethod
    def print_locations():
        """
        Prints the locations
        :return:
        """
        temp_list = [[x] for x in Data.location_codes]
        temp_list.sort()

        print(tabulate.tabulate(temp_list, headers=["Location List"], tablefmt="fancy_grid"))
