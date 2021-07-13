import argparse


class Parser:
    def __init__(self, description):
        self.args = None
        self.parser = argparse.ArgumentParser(description=description)
        self.setup()
        self.arg_errors()
        self.arg_checks()

    def setup(self):
        pass

    def arg_errors(self):
        pass

    def arg_checks(self):
        pass
