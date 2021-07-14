from lib.command.phuber_args import PhuberArgs
from lib.pornhub.scraper import Scraper as PornHubScraper


if __name__ == "__main__":
    scrapers = {"pornhub": PornHubScraper()}
    args = PhuberArgs().get_args()
    scraper = scrapers[args.website]
    scraper.late_init(args).start()


