import json
import sys
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

# 定数
POLLEN_URL="https://kafun.yahoo.co.jp/weather/%s"
CITY_CODE="14" # 神奈川

# 花粉情報取得
def get_pollen_info():
    try:
        url = POLLEN_URL % CITY_CODE
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        # htmlタグ dd でのタグを取得
        span = soup.find_all("dd")

        # 花粉量
        pollen_data = ""

        for tag in span:
            try:
                tag_class = tag.get("class").pop(0)
                if tag_class in "dataBox__pollenData":
                    pollen_data = tag.find("span", class_="text").string
                    break
            except:
                pass
        
        print(pollen_data)
    except Exception as ex:
        print("Exception Error: ", ex)
        sys.exit(1)
    return soup

def main():
    pollen_json = get_pollen_info()

if __name__ == '__main__':
    main()