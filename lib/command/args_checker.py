class ArgsChecker:
    """Checks & modifies the commandline arguments received"""
    def __init__(self, phuber_args):
        self.args = phuber_args
        self.arg_errors()
        self.arg_checks()

    def arg_errors(self):
        """
        Raises an error if there are any abnormalities with the commandline arguments
        :return: None
        """
        pass

    def arg_checks(self):
        """Checks & apply the appropriate solution for the commandline arguments"""
        pass
