import time

import requests
from bs4 import BeautifulSoup

from uk_bin_collection.uk_bin_collection.common import *
from uk_bin_collection.uk_bin_collection.get_bin_data import AbstractGetBinDataClass


# import the wonderful Beautiful Soup and the URL grabber
class CouncilClass(AbstractGetBinDataClass):
    """
    Concrete classes have to implement all abstract operations of the
    base class. They can also override some operations with a default
    implementation.
    """

    def parse_data(self, page: str, **kwargs) -> dict:

        user_uprn = kwargs.get("uprn")
        check_uprn(user_uprn)
        bindata = {"bins": []}

        SESSION_URL = "https://online.hartlepool.gov.uk/authapi/isauthenticated?uri=https%253A%252F%252Fonline.hartlepool.gov.uk%252Fservice%252FRefuse_and_recycling___check_bin_day&hostname=online.hartlepool.gov.uk&withCredentials=true"

        API_URL = "https://online.hartlepool.gov.uk/apibroker/runLookup"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://online.hartlepool.gov.uk/fillform/?iframe_id=fillform-frame-1&db_id=",
        }
        s = requests.session()
        r = s.get(SESSION_URL)
        r.raise_for_status()
        session_data = r.json()
        sid = session_data["auth-session"]
        params = {
            "id": "5ec67e019ffdd",
            "repeat_against": "",
            "noRetry": "true",
            "getOnlyTokens": "undefined",
            "log_id": "",
            "app_name": "AF-Renderer::Self",
            # unix_timestamp
            "_": str(int(time.time() * 1000)),
            "sid": sid,
        }

        data = {
            "formValues": {
                "Section 1": {
                    "collectionLocationUPRN": {
                        "value": user_uprn,
                    },
                },
            },
        }

        r = s.post(API_URL, json=data, headers=headers, params=params)
        r.raise_for_status()

        data = r.json()
        rows_data = data["integration"]["transformed"]["rows_data"]["0"]
        if not isinstance(rows_data, dict):
            raise ValueError("Invalid data returned from API")

        soup = BeautifulSoup(rows_data["HTMLCollectionDatesText"], "html.parser")

        # Find all div elements containing the bin schedule
        for div in soup.find_all("div"):
            # Extract bin type and date from the span tag
            text = div.find("span").text.strip()
            bin_type, date = text.split(" ", 1)
            dict_data = {
                "type": bin_type,
                "collectionDate": date,
            }
            bindata["bins"].append(dict_data)

        return bindata
