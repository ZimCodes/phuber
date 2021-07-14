import argparse, pytest
from lib.command.phuber_args import PhuberArgs


class TestArgument:
    def test_list(self, phuber):
        assert phuber.get_args("pornhub", "--category-list") == get_namespace(category_list=True)

    def test_subcommand(self, phuber):
        assert phuber.get_args("pornhub") == get_namespace()

    def test_all_commands(self, phuber):
        result = {"search": "happiness", "pages": 2, "listname": "save", "premium": "username:password",
                  "verbose": False, "premium_only": True, "include": "cc", "exclude": "hd,exclusive,comp,cartoon",
                  "category_list": False, "prod": "home", "min": 10, "max": 20}

        assert phuber.get_args("pornhub", result['search'], "--pages=2", "-l=save", "-x=username:password",
                               "--premium-only", "-i=cc", "-e=hd,exclusive,comp,cartoon", "--prod=home", "--min=10",
                               "--max=20") == get_namespace(**result)


def get_namespace(**kwg):
    namespace = {"search": None, "pages": None, "listname": "list.txt", "premium": None, "verbose": False,
                 "premium_only": False, "include": None, "exclude": None, "category_list": False, "prod": None,
                 "min": None, "max": None}
    result = namespace | kwg
    return argparse.Namespace(**result)


@pytest.fixture
def phuber():
    return PhuberArgs()
