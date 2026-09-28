import requests as re
import logging
import json


logger = logging.getLogger()
logger.setLevel(logging.INFO)

API_URL= 'https://api.vietqr.io/v2/banks'

class Crawler():
    def __init__(self, api_url=API_URL):
        self.api = api_url
    def get_bank_logos(self,output_path, api_url=None):
        try:
            logging.info("Starting bank crawling")
            api = api_url if api_url is not None else self.api
            print(api)
            bank_info = re.get(api).json()
            logger.info("Vietnam Bank Information's here:" + str(bank_info))
            with open("bank_info.json", "w", encoding="utf-8") as file:
                params = {"obj": bank_info, "fp":file, "ensure_ascii": False}
                json.dump(**params)
                for bank in dict(bank_info).get("data", []):
                    bank_name = bank["shortName"]
                    img_link = bank.get("logo", "")
                    if img_link is not None:
                        img_logo = re.get(img_link)
                        if img_logo.status_code==200:
                            logger.info("Succeed to extract logo image of {0}".format(bank_name))
                            try:
                                with open("""{0}/{1}.png""".format(output_path,bank_name), "wb") as f:
                                    f.write(img_logo.content)
                                    logger.info("SUCCEED to crawl bank's logos")
                            except Exception as e:
                                logger.error(f"FAILED to save image of {bank["shortName"]}"+ str(e))
                logger.info("Saved to file successfully")
        except Exception as e:
            logger.error("There is a found issue\n" + str(e)) 
