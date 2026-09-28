from crawler.crawler import Crawler
import argparse

parser = argparse.ArgumentParser(description="A simple script to accept arguments.")
parser.add_argument("--output_path", type=str, help="The folder path storing images")
args = parser.parse_args()

crawler = Crawler()
crawler.get_bank_logos(args.output_path)


