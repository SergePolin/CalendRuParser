"""
Module: parse.py
Description: This module provides a Parser class to retrieve holiday names from calend.ru.
"""

import datetime
import requests
from bs4 import BeautifulSoup


class Parser:
    """
    Parser class for retrieving holiday names from calend.ru.
    """

    def __init__(self, url="https://www.calend.ru/holidays/", css_selector=".holidays .title"):
        """
        Constructor of Parser class.

        :param url: URL to parse
        :param css_selector: CSS selector to extract holiday names
        """
        self.url = url
        self.css_selector = css_selector

    def get_today_date(self):
        """
        Returns today's date in format "YYYY-MM-DD"
        """
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")

    def get_holiday(self, date):
        """
        Retrieves the holiday names for a given date.

        :param date: Date in format "YYYY-MM-DD"
        :return: List of holiday names or None if holiday is not found
        """
        full_url = self.url + date + "/"
        try:
            response = requests.get(full_url, timeout=5)  # Set a timeout value for the HTTP request
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
        except requests.exceptions.RequestException as ex:
            print(f"Error occurred while retrieving {full_url}: {ex}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract holiday names from css selector
        holidays = soup.select(self.css_selector)
        if not holidays:
            return None
        return [h.text.strip() for h in holidays]


if __name__ == "__main__":
    parser = Parser()
    current_date = parser.get_today_date()
    holiday = parser.get_holiday(current_date)
    if holiday:
        print(f"Holidays on {current_date}: {', '.join(holiday)}")
    else:
        print(f"No holidays found on {current_date}")
