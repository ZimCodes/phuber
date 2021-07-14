import argparse
import sys


class SubParser:
    """A class to represent a parser of a parser (summary: subparser)"""
    def __init__(self, sub_parser_maker):
        """
        Initialize SubParser object
        :param sub_parser_maker: An object for creating a group of parsers
        """
        self.maker = sub_parser_maker
        self.__parsers = {}

    def create_parser(self, name, **kwargs):
        """
        Creates a subcommand. An ArgumentParser object

        Ex: git push --options ...

        In the example 'push' is the subcommand
        :param name: Name of subcommand
        :param kwargs: options for creating the parser
        :return: None
        """
        self.__parsers[name] = self.maker.add_parser(name, **kwargs)

    def create_arg(self, parser_name, *names, **options):
        """
        Creates a new argument for the subcommand
        :param parser_name: Name of the subcommand
        :param names: Name(s) to give the option/positional argument. Ex: -l --list
        :param options: options for creating the argument
        :return: None
        """
        self.__parsers[parser_name].add_argument(*names, **options)


class CommandBuilder:
    """A class to make it easier to use argparse"""
    def __init__(self, **parser_kwargs):
        """
        Initialize CommandBuilder object
        :param parser_kwargs: Options for configuring the parser
        """
        self.parser = argparse.ArgumentParser(**parser_kwargs)
        self.__sub_parsers = []

    def create_sub_level(self, **sub_kwargs):
        """
        Creates a subcommand maker from the previous parser
        :param sub_kwargs: Options to configure the subcommand maker
        :return: None
        """
        sub_parser = None
        if len(self.__sub_parsers) == 0:
            sub_parser_maker = self.parser.add_subparsers(**sub_kwargs)
            sub_parser = SubParser(sub_parser_maker)
        else:
            sub_parser = SubParser(self.__sub_parsers[len(self.__sub_parsers) - 1].maker)
        self.__sub_parsers.append(sub_parser)

    def create_sub_parser(self, name, depth=1, **sub_kwargs):
        """
        Creates a new subcommand
        :param name: Name of the subcommand
        :param depth: How far deep the level to create a new subcommand
        :param sub_kwargs: Configuration options of the subcommand
        :return: None
        """
        depth -= 1 if depth > 0 else 0
        if depth < 0:
            depth = 0
        elif depth >= len(self.__sub_parsers):
            return
        self.__sub_parsers[depth].create_parser(name, **sub_kwargs)

    def add_arg(self, *names, **options):
        """
        Creates a new argument for the main parser
        :param names: Aliases to call the argument
        :param options: Configuration options for main parser
        :return: None
        """
        self.parser.add_argument(*names, **options)

    def add_sub_arg(self, depth, sub_name, *names, **options):
        """
        Creates an argument for a subcommand
        :param depth: How far to look through in order to find subcommand
        :param sub_name: Name of the subcommand
        :param names: Aliases to call the sub argument
        :param options: Configuration options for the sub argument
        :return: None
        """
        depth -= 1 if depth > 0 else 0
        if depth < 0:
            depth = 0
        elif depth >= len(self.__sub_parsers):
            return

        self.__sub_parsers[depth].create_arg(sub_name, *names, **options)

    def get_args(self, *args):
        """
        Provides the arguments retrieved from the commandline
        :param args: The arguments to simulate placing into the commandline
        :return: Arguments from the commandline (Namespace object)
        """
        new_args = self.parser.parse_args(args) if args else self.parser.parse_args()
        # Attempts to add the website to scrape from into the Namespace object
        try:
            new_args.website = sys.argv[1]
        except IndexError:
            pass
        finally:
            return new_args
