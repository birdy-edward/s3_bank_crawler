from crawler.crawler import Crawler, logger, networks, networks_dict
import argparse
from datetime import datetime, timedelta
import time
import requests as re



parser = argparse.ArgumentParser(description="A simple script to accept arguments.")
parser.add_argument("--output_path", type=str, help="The folder path storing images")

parser.add_argument("--event", type=str, help="The event to crawl, either 'bank' or 'station'")

args = parser.parse_args()

stations= [data[0] for data in [[i] for i in list(set().union(*networks_dict.values()))]]

if args.event == "station":
    logger.info("Crawling station data...")
    today = datetime.now()
    today_year = today.year
    crawler = Crawler()
    for station in stations:
        args_dict = {
            "start_year": today_year,
            "start_month": today.month,
            "start_day": today.day,
            "end_year": today_year+1,
            "end_month": today.month,
            "end_day": today.day,
            "station": station
        }
        time.sleep(10)
        crawler.get_station_data(args.output_path, **args_dict)

else:
    logger.info("Crawling bank data...")
    crawler = Crawler()
    crawler.get_bank_logos(args.output_path)


