#!/usr/bin/python3

from bs4 import BeautifulSoup
import os, argparse, requests

def get_args():
    parser = argparse.ArgumentParser(description='PornHub Link Scrapper')
    parser.add_argument('search', metavar="search terms",
                        help='Search Term (in quotations)')
    parser.add_argument('-p', '--pages', type=int,
                        help='# of pages to scrape')
    parser.add_argument('-l', '--listname',
                        help='Custom list name (defaults to list.txt)')
    parser.add_argument('-x', '--premium',
                        help='Use premium account, will require username and password in <username:password> format')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Prints titles to console so you know what you\'re grabbing')
    parser.add_argument('--premium-only', action="store_true",
                        help='Retrieve only premium videos. (must have premium account)')
    parser.add_argument('-i', '--include',
                        help='The category to filter into the search')
    parser.add_argument('-e', '--exclude',
                        help='the categories to remove from the search(max=10). Example: "cat1,cat2,cat3,cat4"')
    parser.add_argument('--category-list', action="store_true",
                        help='list of all available categories to filter through "(what keyword mean)"')
    parser.add_argument('--prod', choices=['home', 'pro'],
                        help="production of the video")
    parser.add_argument('--min', '--min-dur', type=int, choices=[10, 20, 30],
                        help='Minimum length of videos')
    parser.add_argument('--max', '--max-dur', type=int, choices=[10, 20, 30],
                        help='Maximum length of videos')

    args = parser.parse_args()
    search = args.search
    pages = args.pages
    list_name = args.listname
    premium = args.premium
    verbose = args.verbose
    premium_only = args.premium_only
    include = args.include
    exclude = args.exclude
    production = args.prod
    max_length = args.max
    min_length = args.min
    show_category_list = args.category_list

    args_check(parser, premium, premium_only, search, show_category_list)

    return (search, pages, list_name, premium, verbose, premium_only, include, exclude,production,min_length,
            max_length,show_category_list)


def args_check(parser, premium, premium_only, search, show_category_list):
    """
    Check if there are any errors from user input
    :param parser:parse arguments received from user input
    :param premium: login credentials for premium account
    :param premium_only: show premium videos only (premium account required!)
    :param search: what to search for (required)
    :param show_category_list: display list of available categories to use while filtering
    :return: None
    """
    if not search and not show_category_list:
        parser.error('Search Term Needed!')
    if not premium and premium_only:
        parser.error("Must login to premium account to use '--premium-only' option!")


def search_filters_cat(premium_only, include, exclude):
    """
    Filters to use while searching for videos
    :param premium_only: show premium videos only (premium account required!)
    :param include: the category to include in search filter
    :param exclude: the category(ies) to exclude from search filter(max=10)
    :return: the url query to use based on category search filter(s)
    """
    filter_url = []
    if premium_only:
        filter_url.append('&premium=1')

    if include:
        filter_url.append(include_url_converter(include))

    if exclude:
        filter_url.append(exclude_url_converter(exclude))

    filter_str = ''
    return filter_str.join(filter_url)


def include_url_converter(include_param):
    """
    Convert category specified by the user into one that can be used by the url
    :param include_param: the category to filter into the search
    :return: the query parameter url to include into the search
    """
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
    result_str = ''
    if include_param in category_codes.keys():
        result_str = '&filter_category=%s' % category_codes[include_param]
    else:
        print('---------%s is not a Pornhub category! See "--category-list" for more info!' % include_param)

    return result_str


def exclude_url_converter(exclude_params):
    """
    Convert category(ies) specified by the user into one that can be used by the url
    :param exclude_params: the category(ies) to filter out of the search
    :return: the query parameter url to include into the search
    """
    exclude_params_list = exclude_params.split(',')
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
    converted_filters = []
    seperator = '-'

    for param in exclude_params_list:
        if param in category_codes.keys():
            converted_filters.append(category_codes[param])
        else:
            print('---------%s is not a Pornhub category! See "--category-list" for more info!' % param)

    result_str = seperator.join(converted_filters)
    url_str = "&exclude_category=%s" % result_str
    return url_str


def print_categories():
    """
    Print out categories that can be used for filtering the search
    :return: None
    """
    category_list = ['60fps', 'amateur', 'anal', 'arab', 'asian', 'bbw(big busty women)', 'babe', 'babysitter',
                     'btscenes(behind the scenes)',
                     'bigass', 'bigdick', 'titslg(big tits)', 'bimale', 'blonde', 'bj(blowjob)', 'bondage', 'brazilian',
                     'british', 'brunette',
                     'bukkake', 'cartoon', 'casting', 'celeb', 'cc', 'college', 'comp(compilation)', 'cosplay',
                     'creampie', 'cuckold',
                     'cumshot', 'czech', 'described', 'dp', 'ebony', 'euro', 'exclusive', 'feet',
                     'femaleorgy(female orgasm)',
                     'fetish', 'fisting', 'french', 'funny', 'gangbang', 'gay', 'german', 'hd', 'handjob', 'hardcore',
                     'hentai',
                     'indian', 'interactive', 'interracial', 'italian', 'japanese', 'korean', 'latina', 'lesbian',
                     'milf', 'massage',
                     'masturbate', 'mature', 'musclemen', 'music', 'oldyoung', 'orgy', 'pov', 'parody', 'party', 'piss',
                     'popww(popular with women)', 'pornstar', 'public', 'pussylick', 'reality', 'redhead',
                     'rp(roleplay)',
                     'romantic', 'rough', 'russian', 'sfw(safe for work)', 'school', 'titssm(small tits)', 'smoking', 'solofemale',
                     'solomale',
                     'squirt', 'step(step fantasy)', 'strip(striptease)', 'tatwomen(tatooed women)', 'teen', '3some',
                     'toys',
                     'tmale(transmale)', 'twgirl(trans with girl)', 'twguy(trans with guy)', 'trans(transgender)',
                     'veramateurs(verified amateurs)', 'vercouples(verified couples)', 'vermodels(verified models)',
                     'vintage', 'vr(virtual reality)', 'webcam']
    print(category_list)

def production_filter(production):
    """
    Filter the production of the videos
    :param production: the production of the video to use
    :return: the query parameter url for the production to filter into the search
    """
    prod_url = ''
    if production == 'prod':
        prod_url = '&p=professional'
    elif production == 'home':
        prod_url = '&p=homemade'

    return prod_url

def duration_filter(min, max):
    """
    Filter the duration of the videos
    :param min: the minimum length of the videos
    :param max: the maximum length of the videos
    :return: the query parameter url of the duration to filter into the search
    """
    min_url = ''
    max_url = ''
    if max:
        max_url = '&max_duration=%d' % max
    if min:
        min_url = '&min_duration=%d' % min

    return min_url + max_url


def scrape_web(session,domain,list_name, search_term, pages, verbose, premium_only, include, exclude, production, min, max):
    """
    Scrape the video links from the search results.
    :param session: the current connection to the website
    :param domain: the website domain
    :param list_name: the file name to use when exporting the list of video links
    :param search_term: the search term to use when finding videos
    :param pages: the number of pages to scrape from
    :param verbose: Prints video titles to the console so you know what you're grabbing
    :param premium_only: show premium videos only (premium account required!)
    :param include: include category into the search
    :param exclude: exclude category(ies) from the search
    :param production: the production of the videos
    :param min: minimum length of the videos
    :param max: maximum length of the videos
    :return: None
    """
    if os.path.exists(list_name):
        os.remove(list_name)

    full_list = open(list_name, 'w')

    search_prefix = '/video/search?search='
    search = search_term.replace(" ", "+")
    page_number_cat = '&page='
    sub_url = domain + search_prefix + search + page_number_cat

    page_range = range(1, pages + 1)

    for current_page in page_range:
        url = sub_url + str(current_page) + production_filter(production)+duration_filter(min,max) \
              + search_filters_cat(premium_only, include, exclude)
        print(url)
        req = session.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        found_links = soup.select("div.thumbnail-info-wrapper span.title")
        vid_urls = []

        for current_link in found_links:
            for video_found in current_link.find_all('a', {"class": ""}):
                vids = video_found.get('href')
                if vids:
                    if verbose:
                        print(video_found.get('title'))
                    vid_urls.append(domain + vids)

        seperator = '\n'
        print(seperator.join(vid_urls), file=full_list)
    full_list.close()


def premium_login(session,domain, username, password):
    """
    Log into premium account
    :param session: the current connection to the website
    :param domain: the website domain
    :param username: the username login credential
    :param password: the password login credential
    :return: None
    """
    login = '/premium/login'
    login_url = domain + login

    s = session.get(login_url)
    soup = BeautifulSoup(s.text, 'html.parser')
    token = soup.select("#token")[0].attrs['value']

    payload = {'username': username,
               'password': password,
               'token': token,
               'redirect': '',
               'from': 'pc_premium_login',
               'segment': 'straight'
               }

    try:
        s = session.post(domain + '/front/authenticate', data=payload)

    except Exception:
        print("Failed to login")


def user_logout(session, domain):
    """
    Logout of premium account
    :param session: the current connection to the website
    :param domain: the website domain
    :return: None
    """
    req = session.get(domain)

    soup = BeautifulSoup(req.text, 'html.parser')

    for found_links in soup.find_all("a", {"class": "js_premiumLogOut"}, href=True):
        logout = found_links['href']

    full_logout = domain + logout

    try:
        response = session.get(full_logout)
    except Exception:
        print("Failed to process logout request")

def start():
    """
    Start web scraping videos
    :return: None
    """

    (search, pages, list_name, premium, verbose, premium_only, include, exclude, production, min_length, max_length, show_category_list) = get_args()

    show_categories_check(show_category_list)

    if search:
        session = requests.Session()
        pages = pages_check(pages)

        list_name = filename_check(list_name, search)

        if premium:
            pornhub_premium(exclude=exclude, include=include, list_name=list_name, pages=pages, premium=premium,
                            premium_only=premium_only, search=search, session=session, verbose=verbose,
                            production=production, min=min_length, max=max_length)
        else:
            pornhub(exclude=exclude, include=include, list_name=list_name, pages=pages,
                    premium_only=premium_only, search=search, session=session, verbose=verbose, production=production,
                    min=min_length, max=max_length)

        session.close()



def pornhub(exclude, include, list_name, pages, premium_only, search, session, verbose, production, min, max):
    """
    The procedure to web scrape videos from Pornhub
    :param exclude: exclude category(ies) from the search
    :param include: include category into the search
    :param list_name: the file name to use when exporting the list of video links
    :param pages: the number of pages to scrape from
    :param premium_only: show premium videos only (premium account required!)
    :param search: the search term to use when finding videos
    :param session: the current connection to the website
    :param verbose: Prints video titles to the console so you know what you're grabbing
    :param production: the production of the videos
    :param min: minimum length of the videos
    :param max: maximum length of the videos
    :return: None
    """
    domain = 'https://www.pornhub.com'
    scrape_web(session=session, domain=domain, list_name=list_name, search_term=search, pages=pages, verbose=verbose,
               premium_only=premium_only, include=include, exclude=exclude, production=production, min=min, max=max)



def pornhub_premium(exclude, include, list_name, pages, premium, premium_only, search, session, verbose, production, min, max):
    """
    The procedure to web scrape videos from PornhubPremium
    :param exclude: exclude category(ies) from the search
    :param include: include category into the search
    :param list_name: the file name to use when exporting the list of video links
    :param pages: the number of pages to scrape from
    :param premium: login credentials for premium account
    :param premium_only: show premium videos only (premium account required!)
    :param search: the search term to use when finding videos
    :param session: the current connection to the website
    :param verbose: Prints video titles to the console so you know what you're grabbing
    :param production: the production of the videos
    :param min: minimum length of the videos
    :param max: maximum length of the videos
    :return: None
    """
    username, password = premium.split(':')
    domain = 'https://www.pornhubpremium.com'
    premium_login(session, domain, username, password)
    scrape_web(session=session, domain=domain, list_name=list_name, search_term=search, pages=pages, verbose=verbose,
               premium_only=premium_only, include=include, exclude=exclude, production=production, min=min, max=max)
    user_logout(session, domain)


def filename_check(list_name, search):
    """
    Check whether or not a file name has been given
    :param list_name: the name of the video link file
    :param search: the search terms used to find videos
    :return: file name with extension
    """
    if not list_name:
        file_name = search.replace(" ", "_")
        list_name = file_name + '.txt'
    return list_name


def pages_check(pages):
    """
    Check whether or not # of pages has been specified
    :param pages: the # of pages to scrape through
    :return: the # of pages
    """
    if not pages:
        pages = 1
    return pages


def show_categories_check(show_category_list):
    """
    Check whether or not the user would like to see the list of categories available.
    :param show_category_list: the list of categories
    :return: None
    """
    if show_category_list:
        print_categories()


start()