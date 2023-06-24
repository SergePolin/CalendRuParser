import requests
from bs4 import BeautifulSoup
import datetime


class Parser:
    def __init__(self, url="https://www.calend.ru/holidays/"):
        self.url = url

    def get_today_date(self):
        '''
        Returns today's date in format "YYYY-MM-DD"
        '''
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")

    def get_holiday(self, date):
        response = requests.get(self.url + date + "/")
        soup = BeautifulSoup(response.text, 'html.parser')
        # extract holiday name from path ".holidays>.title"
        holiday = soup.select(".holidays .title")
        # if holiday is not found, return None
        if len(holiday) == 0:
            return None
        # else return holiday names
        return [h.text.strip() for h in holiday]


if __name__ == "__main__":
    parser = Parser()
    today = parser.get_today_date()
    holiday = parser.get_holiday(today)
    print(today, holiday)
