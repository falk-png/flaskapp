from xlsxwriter import Workbook
from xlsxwriter.exceptions import FileCreateError
import os


class ExcelManager():
    def __init__(self, path):
        # Create Workbook
        self.workbook = Workbook(path)


        # Create Sheet
        self.sheet = self.workbook.add_worksheet()


    def close(self):
        self.workbook.close()


    def write(self, cell, value, options=None):
        self.sheet.write(cell, value, options)


    def get_xlsx_file(self, prices_dic):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        names = [price["name"] for price in prices_dic]
        links = [price["link"] for price in prices_dic]
        prices = [price["price"] for price in prices_dic]

        bold = self.workbook.add_format({
            "bold": True,
        })
        money = self.workbook.add_format({
            'num_format': '#,##0.00 €'
        })


        # Define columns
        self.write("A1", "Name:", bold)
        self.write("B1", "Link:", bold)
        self.write("C1", "Preis:", bold)


        # Write names
        for index, name in enumerate(names, 2):
            self.write("A" + str(index), name)


        # Write links
        for index, link in enumerate(links, 2):
            self.write("B" + str(index), link)


        # Write prices
        for index, price in enumerate(prices, 2):
            self.write("C" + str(index), price, money)


        # Close / Save file
        self.close()