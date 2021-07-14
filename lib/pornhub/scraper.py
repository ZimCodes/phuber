from .checker import Checker
import os, requests
from bs4 import BeautifulSoup
from .configurator import Configurator
from lib.abstract_scraper import AbstractScraper


class Scraper(AbstractScraper):
    def __init__(self, args=None):
        self.args = Checker(args).args if args else None

    def late_init(self, args):
        self.args = Checker(args).args
        return self

    def scrape_web(self, session, domain):
        """
        Scrape video links from search results.
        :param session: the current connection to the website
        :param domain: the website domain
        list_name: the file name to use when exporting the list of video links
        search_term: the search term to use when finding videos
        pages: the number of pages to scrape from
        verbose: Prints video titles to the console so you know what you're grabbing
        premium_only: show premium videos only (premium account required!)
        include: include category into the search
        exclude: exclude category(ies) from the search
        production: the production of the videos
        min: minimum length of the videos
        max: maximum length of the videos
        :return: None
        """
        if os.path.exists(self.args.listname):
            os.remove(self.args.listname)

        with open(self.args.listname, 'w') as full_list:
            search_prefix = '/video/search?search='
            search = self.args.search.replace(" ", "+")
            page_number_cat = '&page='
            sub_url = domain + search_prefix + search + page_number_cat

            page_range = range(1, self.args.pages + 1)

            for current_page in page_range:
                url = sub_url + str(current_page) + Configurator.production_filter(self.args.prod) + \
                      Configurator.duration_filter(self.args.min, self.args.max) \
                      + Configurator.search_filters_cat(self.args.premium_only, self.args.include, self.args.exclude,
                                                        Checker.category_codes) \
                      + Configurator.order_filter(self.args.order, self.args.order_time)
                print(url)
                req = session.get(url)
                soup = BeautifulSoup(req.text, 'html.parser')
                found_links = soup.select("div.thumbnail-info-wrapper span.title")
                vid_urls = []

                for current_link in found_links:
                    for video_found in current_link.find_all('a', {"class": ""}):
                        video_url = video_found.get('href')
                        if video_url and ":void(0)" not in video_url:
                            if self.args.verbose:
                                print(video_found.get('title'))
                            vid_urls.append(domain + video_url)

                separator = '\n'
                print(separator.join(vid_urls), file=full_list)

    def __pornhub(self, session):
        """
        The procedure to web scrape videos from Pornhub
        :param session: the current connection to the website
        :return: None
        """
        domain = 'https://www.pornhub.com'
        self.scrape_web(session=session, domain=domain)

    def __pornhub_premium(self, session):
        """
        The procedure to web scrape videos from PornhubPremium
        :param session: the current connection to the website
        :return: None
        """
        username, password = self.args.premium.split(':')
        domain = 'https://www.pornhubpremium.com'
        self.__premium_login(session, domain, username, password)
        self.scrape_web(session, domain)
        self.__user_logout(session, domain)

    def __premium_login(self, session, domain, username, password):
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

    def __user_logout(self, session, domain):
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

    def start(self):
        """
        Start web scraping videos
        :return: None
        """
        # If specified, show all categories
        if self.args.category_list is True:
            Checker.print_categories()
            return

        # Must have search term to proceed scraping
        if not self.args.search:
            return

        session = requests.Session()
        if self.args.premium:
            self.__pornhub_premium(session)
        else:
            self.__pornhub(session)

        session.close()



