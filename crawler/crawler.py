import requests as re
import logging
import json


logger = logging.getLogger()
logger.setLevel(logging.INFO)

API_URL= 'https://api.vietqr.io/v2/banks'

API_URL_STATION= 'https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?data=all&tz=Etc/UTC&format=json&latlon=yes&year1={}&month1={}&day1={}&year2={}&month2={}&day2={}&station={}'

networks = [
                'AK_ASOS',
                'BS__ASOS',
                'AT__ASOS',
                'AO__ASOS',
                'AR__ASOS'
                # 'AQ_ASOS',
                # 'AF__ASOS',
                # 'AZ__ASOS',
                # 'AS__ASOS',
                # 'DZ__ASOS',
                # 'AL__ASOS',
                # 'BH__ASOS',
                # 'AW__ASOS',
                # 'AR_ASOS',
                # 'AI__ASOS',
                # 'AM__ASOS',
                # 'AU__ASOS',
                # 'AL_ASOS',
                # 'AG__ASOS',
                # 'AZ_ASOS',
                # 'CA_AB_ASOS',
                # 'BE__ASOS',
                # 'BM__ASOS',
                # 'BT__ASOS',
                # 'BZ__ASOS',
                # 'BY__ASOS',
                # 'BI__ASOS',
                # 'CA_ASOS',
                # 'BD__ASOS',
                # 'BW__ASOS',
                # 'KH__ASOS',
                # 'BB__ASOS',
                # 'CM__ASOS',
                # 'BG__ASOS',
                # 'CF__ASOS',
                # 'BO__ASOS',
                # 'BR__ASOS',
                # 'CV__ASOS',
                # 'BF__ASOS',
                # 'BA__ASOS',
                # 'VG__ASOS',
                # 'CA_BC_ASOS',
                # 'IO__ASOS',
                # 'BJ__ASOS',
                # 'CR__ASOS',
                # 'EG__ASOS',
                # 'CY__ASOS',
                # 'TD__ASOS',
                # 'CD__ASOS',
                # 'DK__ASOS',
                # 'DJ__ASOS',
                # 'DE_ASOS',
                # 'CT_ASOS',
                # 'EC__ASOS',
                # 'KM__ASOS',
                # 'CU__ASOS',
                # 'CO_ASOS',
                # 'CG__ASOS',
                # 'CZ__ASOS',
                # 'CK__ASOS',
                # 'CL__ASOS',
                # 'CN__ASOS',
                # 'CO__ASOS',
                # 'HR__ASOS',
                # 'DM__ASOS',
                # 'DO__ASOS',
                # 'FM__ASOS',
                # 'FR__ASOS',
                # 'FI__ASOS',
                # 'FL_ASOS',
                # 'GL__ASOS',
                # 'GA__ASOS',
                # 'KY__ASOS',
                # 'ET__ASOS',
                # 'FJ__ASOS',
                # 'FK__ASOS',
                # 'DE__ASOS',
                # 'GA_ASOS',
                # 'GH__ASOS',
                # 'GQ__ASOS',
                # 'GR__ASOS',
                # 'PF__ASOS',
                # 'GB__ASOS',
                # 'GM__ASOS',
                # 'EE__ASOS',
                # 'GE__ASOS',
                # 'GF__ASOS',
                # 'GI__ASOS',
                # 'SV__ASOS',
                # 'IL__ASOS',
                # 'HK__ASOS',
                # 'IS__ASOS',
                # 'GU__ASOS',
                # 'ID__ASOS',
                # 'IL_ASOS',
                # 'HU__ASOS',
                # 'IQ__ASOS',
                # 'GD__ASOS',
                # 'HI_ASOS',
                # 'IA_ASOS',
                # 'HN__ASOS',
                # 'HT__ASOS',
                # 'GY__ASOS',
                # 'IN_ASOS',
                # 'ID_ASOS',
                # 'IE__ASOS',
                # 'IN__ASOS',
                # 'GW__ASOS',
                # 'GN__ASOS',
                # 'GT__ASOS',
                # 'IR__ASOS',
                # 'CI__ASOS',
                # 'JM__ASOS',
                # 'LU__ASOS',
                # 'ME_ASOS',
                # 'MK__ASOS',
                # 'KI__ASOS',
                # 'KS_ASOS',
                # 'LA_ASOS',
                # 'JP__ASOS',
                # 'LV__ASOS',
                # 'LB__ASOS',
                # 'KW__ASOS',
                # 'MG__ASOS',
                # 'KY_ASOS',
                # 'LA__ASOS',
                # 'JO__ASOS',
                # 'IT__ASOS',
                # 'LR__ASOS',
                # 'LT__ASOS',
                # 'KE__ASOS',
                # 'LY__ASOS',
                # 'KZ__ASOS',
                # 'LS__ASOS',
                # 'MZ__ASOS',
                # 'CA_MB_ASOS',
                # 'MA__ASOS',
                # 'MA_ASOS',
                # 'MY__ASOS',
                # 'MI_ASOS',
                # 'MX__ASOS',
                # 'MM__ASOS',
                # 'MT_ASOS',
                # 'MC__ASOS',
                # 'MH__ASOS',
                # 'MR__ASOS',
                # 'YT__ASOS',
                # 'MD_ASOS',
                # 'MW__ASOS',
                # 'MD__ASOS',
                # 'ML__ASOS',
                # 'MU__ASOS',
                # 'MO_ASOS',
                # 'MV__ASOS',
                # 'MN_ASOS',
                # 'MS_ASOS',
                # 'NP__ASOS',
                # 'NG__ASOS',
                # 'NJ_ASOS',
                # 'MP__ASOS',
                # 'NL__ASOS',
                # 'CA_NB_ASOS',
                # 'NC__ASOS',
                # 'NY_ASOS',
                # 'NI__ASOS',
                # 'NA__ASOS',
                # 'AN__ASOS',
                # 'NE_ASOS',
                # 'NV_ASOS',
                # 'NH_ASOS',
                # 'NM_ASOS',
                # 'ND_ASOS',
                # 'NF__ASOS',
                # 'NC_ASOS',
                # 'CA_NF_ASOS',
                # 'NE__ASOS',
                # 'OH_ASOS',
                # 'PR__ASOS',
                # 'PH__ASOS',
                # 'PN__ASOS',
                # 'OR_ASOS',
                # 'PE__ASOS',
                # 'PL__ASOS',
                # 'CA_NU_ASOS',
                # 'PK__ASOS',
                # 'PT__ASOS',
                # 'OK_ASOS',
                # 'CA_ON_ASOS',
                # 'PG__ASOS',
                # 'CA_NS_ASOS',
                # 'KP__ASOS',
                # 'OM__ASOS',
                # 'PY__ASOS',
                # 'NO__ASOS',
                # 'CA_PE_ASOS',
                # 'PA__ASOS',
                # 'CA_NT_ASOS',
                # 'PA_ASOS',
                # 'RU__ASOS',
                # 'SN__ASOS',
                # 'LC__ASOS',
                # 'SK__ASOS',
                # 'SH__ASOS',
                # 'SB__ASOS',
                # 'SL__ASOS',
                # 'SI__ASOS',
                # 'WS__ASOS',
                # 'SA__ASOS',
                # 'CA_QC_ASOS',
                # 'SG__ASOS',
                # 'RO__ASOS',
                # 'KN__ASOS',
                # 'RS__ASOS',
                # 'RI_ASOS',
                # 'CA_SK_ASOS',
                # 'RW__ASOS',
                # 'QA__ASOS',
                # 'VC__ASOS',
                # 'SC__ASOS',
                # 'ST__ASOS',
                # 'TO__ASOS',
                # 'TN_ASOS',
                # 'TJ__ASOS',
                # 'SR__ASOS',
                # 'TX_ASOS',
                # 'ZA__ASOS',
                # 'SD__ASOS',
                # 'TH__ASOS',
                # 'SY__ASOS',
                # 'TZ__ASOS',
                # 'SD_ASOS',
                # 'KR__ASOS',
                # 'SC_ASOS',
                # 'LK__ASOS',
                # 'TW__ASOS',
                # 'TT__ASOS',
                # 'SE__ASOS',
                # 'TG__ASOS',
                # 'SO__ASOS',
                # 'ES__ASOS',
                # 'SZ__ASOS',
                # 'CH__ASOS',
                # 'WA_ASOS',
                # 'YE__ASOS',
                # 'WI_ASOS',
                # 'VU__ASOS',
                # 'VA_ASOS',
                # 'UY__ASOS',
                # 'WV_ASOS',
                # 'CA_YT_ASOS',
                # 'VN__ASOS',
                # 'WY_ASOS',
                # 'UA__ASOS',
                # 'VE__ASOS',
                # 'ZW__ASOS',
                # 'VT_ASOS',
                # 'ZM__ASOS',
                # 'TR__ASOS',
                # 'VI__ASOS',
                # 'AE__ASOS',
                # 'TM__ASOS',
                # 'UG__ASOS',
                # 'UT_ASOS',
                # 'TN__ASOS'
]

networks_dict = {}
logger.info("Fetching station data for networks...")
for network in networks:
    stations_response = re.get('https://mesonet.agron.iastate.edu/geojson/network/{}.geojson'.format(network))
    networks_dict[network] = [i['id'] for i in stations_response.json().get("features")]


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
                                logger.error(f"FAILED to save image of {bank_name}"+ str(e))
                logger.info("Saved to file successfully")
        except Exception as e:
            logger.error("There is a found issue\n" + str(e)) 

    def get_station_data(self, output_path, api_url=API_URL_STATION, **kwargs):
        url = api_url if api_url is not None else self.api
        logger.info("Initiating station data stream...")
        try:
            with re.get(url.format(
                    kwargs.get("start_year"), kwargs.get("start_month"), kwargs.get("start_day"),
                    kwargs.get("end_year"), kwargs.get("end_month"), kwargs.get("end_day"),
                    kwargs.get("station")
                ), timeout=10, stream=True) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=1000):
                    if chunk:
                        with open(f"{output_path}.json", 'ab') as f:
                            f.write(chunk)
                            logger.info("Successfully fetched station data for station: {}".format(kwargs.get("station")))
        except Exception as e:
            logger.error("An error occurred while fetching station data: " + str(e))
        