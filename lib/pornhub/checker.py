from ..command.args_checker import ArgsChecker
import argparse
import tabulate

class Checker(ArgsChecker):
    """Checks & modifies the commandline arguments received"""
    category_codes = {
        '60fps-1': '105',
        'amateur': '3',
        'anal': '35',
        'arab': '98',
        'asian': '1',
        'bbw': '6',
        'babe': '5',
        'babysitter-18': '89',
        'behind-the-scenes': '141',
        'big-ass': '4',
        'big-dick': '7',
        'big-tits': '8',
        'bisexual-male': '76',
        'blonde': '9',
        'blowjob': '13',
        'bondage': '10',
        'brazilian': '102',
        'british': '96',
        'brunette': '11',
        'bukkake': '14',
        'cartoon': '86',
        'casting': '90',
        'celebrity': '12',
        'closed-captions': '732',
        'college-18-1': '79',
        'compilation': '57',
        'cosplay': '241',
        'creampie': '15',
        'cuckold': '242',
        'cumshot': '16',
        'czech': '100',
        'described-video': '231',
        'double-penetration': '72',
        'ebony': '17',
        'euro': '55',
        'exclusive': '115',
        'feet': '93',
        'female-orgasm': '502',
        'fetish': '18',
        'ffm': '761',
        'fingering': '592',
        'fisting': '19',
        'french': '94',
        'funny': '32',
        'gangbang': '80',
        '!gay': '63',
        '!bareback': '40',
        '!twink-18': '49',
        '!straight-guys': '82',
        '!big-dick': '58',
        '!rough-sex': '312',
        '!creampie': '71',
        '!cartoon': '422',
        '!black': '44',
        '!interracial': '64',
        '!cumshot': '352',
        '!public': '84',
        '!mature': '332',
        '!amateur': '252',
        '!fetish': '52',
        '!japanese': '39',
        '!massage': '45',
        '!bear': '66',
        '!asian': '48',
        '!latino': '50',
        '!euro': '46',
        '!college-18': '68',
        '!solo-male': '54',
        '!reality': '85',
        '!military': '402',
        '!pov': '372',
        '!casting': '362',
        '!blowjob': '56',
        '!handjob': '262',
        '!hunks': '70',
        '!muscle': '51',
        '!chubby': '392',
        '!uncut': '272',
        '!jock': '322',
        '!feet': '412',
        '!tattooed-men': '552',
        '!compilation': '382',
        '!vintage': '77',
        '!hd-porn': '107',
        '!vr': '106',
        '!webcam': '342',
        '!closed-captions': '742',
        '!verified-amateurs': '731',
        '!pornstar': '60',
        '!daddy': '47',
        '!group': '62',
        'german': '95',
        'hd-porn': '38',
        'handjob': '20',
        'hardcore': '21',
        'hentai': '36',
        'indian': '101',
        'interactive': '108',
        'interracial': '25',
        'italian': '97',
        'japanese': '111',
        'korean': '103',
        'latina': '26',
        'lesbian': '27',
        'milf': '29',
        'massage': '78',
        'masturbation': '22',
        'mature': '28',
        'muscular-men': '512',
        'music': '121',
        'old-young-18': '181',
        'orgy': '2',
        'pov': '41',
        'parody': '201',
        'party': '53',
        'pissing': '211',
        'popular-with-women': '73',
        'pornstar': '30',
        'public': '24',
        'pussy-licking': '131',
        'reality': '31',
        'red-head': '42',
        'role-play': '81',
        'romantic': '522',
        'rough-sex': '67',
        'russian': '99',
        'sfw': '221',
        'school-18': '88',
        'strap-on': '542',
        'small-tits': '59',
        'smoking': '91',
        'solo-female': '492',
        'solo-male': '92',
        'squirt': '69',
        'step-fantasy': '444',
        'striptease': '33',
        'tattooed-women': '562',
        'teen-18-1': '37',
        'threesome': '65',
        'toys': '23',
        'trans-male': '602',
        'trans-with-girl': '572',
        'transgender': '83',
        'uncensored': '712',
        'uncensored-1': '722',
        'verified-amateurs': '138',
        'verified-couples': '482',
        'verified-models': '139',
        'vintage': '43',
        'vr': '104',
        'webcam': '61'
    }

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
        if self.args.loc is not None and (len(self.args.loc) > 2 or len(self.args.loc) < 2):
            raise argparse.ArgumentTypeError(f"--loc should be 2 character long")
        if self.args.cat_search and not self.args.search.lower() in Checker.category_codes:
            self.__category_error("search", self.args.search)
        if self.args.cat_search and self.args.include and not self.args.include.lower() in \
                                                              Checker.category_codes:
            self.__category_error("include", self.args.include)
        if self.args.exclude:
            items = self.args.exclude.split(',')
            for x in items:
                if x not in Checker.category_codes:
                    self.__category_error("exclude", x)

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
        temp_list = [[x] for x in Checker.category_codes]
        temp_list.sort()

        print(tabulate.tabulate(temp_list, headers=["Category List"], tablefmt="fancy_grid"))
