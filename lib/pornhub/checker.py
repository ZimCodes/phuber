from ..command.args_checker import ArgsChecker
import argparse


class Checker(ArgsChecker):
    """Checks & modifies the commandline arguments received"""
    category_codes = {
        '60fps': '150',
        'amateur': '3',
        'anal': '35',
        'arab': '98',
        'asian': '1',
        'bbw': '6',
        'babe': '5',
        'babysitter': '89',
        'btscenes': '141',
        'bigass': '4',
        'bigdick': '7',
        'titslg': '8',
        'bimale': '76',
        'blonde': '9',
        'bj': '13',
        'bondage': '10',
        'brazilian': '102',
        'british': '96',
        'brunette': '11',
        'bukkake': '14',
        'cartoon': '86',
        'casting': '90',
        'celeb': '12',
        'cc': '732',
        'college': '79',
        'comp': '57',
        'cosplay': '241',
        'creampie': '15',
        'cuckold': '242',
        'cumshot': '16',
        'czech': '100',
        'described': '231',
        'dp': '72',
        'ebony': '17',
        'euro': '55',
        'exclusive': '115',
        'feet': '93',
        'femaleorgy': '502',
        'fetish': '18',
        'fisting': '19',
        'french': '93',
        'funny': '32',
        'gangbang': '80',
        'gay': '63',
        'german': '95',
        'hd': '38',
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
        'masturbate': '22',
        'mature': '28',
        'musclemen': '512',
        'music': '121',
        'oldyoung': '181',
        'orgy': '2',
        'pov': '41',
        'parody': '201',
        'party': '53',
        'piss': '211',
        'popww': '73',
        'pornstar': '30',
        'public': '24',
        'pussylick': '131',
        'reality': '31',
        'redhead': '42',
        'rp': '81',
        'romantic': '522',
        'rough': '67',
        'russian': '99',
        'sfw': '221',
        'school': '88',
        'titssm': '59',
        'smoking': '91',
        'solofemale': '492',
        'solomale': '92',
        'squirt': '69',
        'step': '444',
        'strip': '33',
        'tatwomen': '562',
        'teen': '37',
        '3some': '65',
        'toys': '23',
        'tmale': '602',
        'twgirl': '572',
        'twguy': '58',
        'trans': '83',
        'veramateurs': '138',
        'vercouples': '482',
        'vermodels': '139',
        'vintage': '43',
        'vr': '104',
        'webcam': '178'
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
            raise argparse.ArgumentError("Must login to premium account to use '--premium-only' option!")

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
        category_list = ['60fps', 'amateur', 'anal', 'arab', 'asian', 'bbw(big busty women)', 'babe', 'babysitter',
                         'btscenes(behind the scenes)',
                         'bigass', 'bigdick', 'titslg(big tits)', 'bimale', 'blonde', 'bj(blowjob)', 'bondage',
                         'brazilian',
                         'british', 'brunette',
                         'bukkake', 'cartoon', 'casting', 'celeb', 'cc', 'college', 'comp(compilation)', 'cosplay',
                         'creampie', 'cuckold',
                         'cumshot', 'czech', 'described', 'dp', 'ebony', 'euro', 'exclusive', 'feet',
                         'femaleorgy(female orgasm)',
                         'fetish', 'fisting', 'french', 'funny', 'gangbang', 'gay', 'german', 'hd', 'handjob',
                         'hardcore',
                         'hentai',
                         'indian', 'interactive', 'interracial', 'italian', 'japanese', 'korean', 'latina', 'lesbian',
                         'milf', 'massage',
                         'masturbate', 'mature', 'musclemen', 'music', 'oldyoung', 'orgy', 'pov', 'parody', 'party',
                         'piss',
                         'popww(popular with women)', 'pornstar', 'public', 'pussylick', 'reality', 'redhead',
                         'rp(roleplay)',
                         'romantic', 'rough', 'russian', 'sfw(safe for work)', 'school', 'titssm(small tits)',
                         'smoking',
                         'solofemale',
                         'solomale',
                         'squirt', 'step(step fantasy)', 'strip(striptease)', 'tatwomen(tatooed women)', 'teen',
                         '3some',
                         'toys',
                         'tmale(transmale)', 'twgirl(trans with girl)', 'twguy(trans with guy)', 'trans(transgender)',
                         'veramateurs(verified amateurs)', 'vercouples(verified couples)', 'vermodels(verified models)',
                         'vintage', 'vr(virtual reality)', 'webcam']
        print(category_list)
