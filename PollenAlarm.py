import json
import sys
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

POLLEN_URL="https://kafun.yahoo.co.jp/weather/%s"
CITY_CODE="14" # KANAGAWA

def get_pollen_info():
    try:
        url = POLLEN_URL % CITY_CODE
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        span = soup.find_all("div")
        hisan_yohou = ""
        for tag in span:
            try:
                string_ = tag.get("class").pop(0)
                if string_ in "z-contents__hisanyohou":
                    hisan_yohou = tag.string_
                    break
            except:
                pass
        
        print(hisan_yohou)
    except Exception as ex:
        print("Exception Error: ", ex)
        sys.exit(1)
    return soup

def main():
    pollen_json = get_pollen_info()

if __name__ == '__main__':
    main()