from copy import deepcopy
from datetime import datetime

import yaml
from requests_html import HTMLSession

from price_tools.tools import price_eur, price_float


class DataManager():
    def __init__(self):
        # Define config variable
        with open("config.yml") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

        # Create session
        self.session = HTMLSession()
        self.current_prices = self.get_prices(as_float=False)

    # Sort prices in dict function (For build in sort function)
    def __sort_prices_by_dic(self, dic):
        return price_float(dic["price"])

    def get(self, name):
        name = name.upper()
        session = self.session

        if name == "FUETTERNUNDFITT":
            # Get website data
            data = session.get("https://www.fuetternundfit.de/astoral-almazyme.html")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find(".price--content.content--default", first=True)
            # Get text from element ("22,64 € *")
            price_raw = price_element.text
            # Convert to price
            price = price_eur(price_raw)

            return price

        elif name == "TIERSHOP":
            # Get website data
            data = session.get("https://www.tiershop.de/Astoral-Almazyme.html")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find(".ts-price", first=True)
            # Get text from element ("1 Stück: 23,00 €* / Stk..")
            price_raw = price_element.text
            # Get 3rd element to avoid problems
            price_raw = price_raw.split()[2]
            # Convert to price
            price = price_eur(price_raw)

            return price

        elif name == "DRHOELTER":
            # Get website data
            data = session.get(
                "https://www.drhoelter.de/almapharm-astoral-almazyme-hund-katze-nahrungsergaenzung-verdauung-bauchspeicheldruese.html")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find(".price")[1]
            # Get text from element ("22,75 € statt 23,10 €")
            price_raw = price_element.text
            # Get 1st element to avoid problems
            price_raw = price_raw.split()[0]
            # Convert to price
            price = price_eur(price_raw)

            return price

        elif name == "TIERARZT24":
            # Get website data
            data = session.get("https://www.tierarzt24.de/almapharm-astoral-almazyme-hk")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find("#price-value-150014", first=True)
            # Get text from element ("22,87€")
            price_raw = price_element.text
            # Convert to price
            price = price_eur(price_raw)

            return price
        elif name == "VETENA":
            # Get website data
            data = session.get("https://www.vetena.de/almapharm-astoral-Almazyme-Hund.html")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find("#productPrice_Variant_0d4e60d7e9616a27ad4cfebc2e8f7e6a", first=True)
            # Get text from element ("23,10 €*")
            price_raw = price_element.text
            # Convert to price
            price = price_eur(price_raw)

            return price
        elif name == "VETMEDPRO":
            # Get website data
            data = session.get(
                "https://www.vetmedpro.de/astoralZ-AlmazymeZ-120g-Diaet-Ergaenzungsfuttermittel-fuer-Hunde-und-Katzen")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find(".price.text-nowrap", first=True)
            # Get text from element ("22,70 €")
            price_raw = price_element.text
            # Convert to price
            price = price_eur(price_raw)

            return price
        elif name == "PETSHOP_VETLINE":
            # Get website data
            data = session.get(
                "https://www.petshop-vetline.de/hunde/ergaenzungsfuttermittel/magen-darm/almapharm-astoral-almazyme-120-g?sPartner=61991")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find(".block-prices--cell")[4]
            # Get text from element ("22,64 € *")
            price_raw = price_element.text
            # Convert to price
            price = price_eur(price_raw)

            return price
        elif name == "EBAY":
            # Get website data
            data = session.get(
                "https://www.ebay.de/itm/astoral-Almazyme-120g-Diat-Erganzungsfuttermittel-fur-Hunde-und-Katzen/324480730788?epid=1344526207&hash=item4b8c8f06a4:g:XR4AAOSw2GlgWIIo")
            # Convert to HTML
            html_data = data.html
            # Get element
            price_element = html_data.find("#prcIsum", first=True)
            # Get text from element ("EUR 25,40")
            price_raw = price_element.text
            # Convert to price
            price = price_eur(price_raw)

            return price

    def get_prices(self, as_float):
        config = self.config
        fake_data = config["fake_data"]

        if fake_data:
            prices = [
                {
                    "name": "Fuettern Und Fit",
                    "link": "https://www.fuetternundfit.de/astoral-almazyme.html",
                    "price": "24,69 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Tiershop",
                    "link": "https://www.tiershop.de/Astoral-Almazyme.html",
                    "price": "22,23 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Dr. Hölter",
                    "link": "https://www.drhoelter.de/almapharm-astoral-almazyme-hund-katze-nahrungsergaenzung-verdauung-bauchspeicheldruese.html",
                    "price": "20,16 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Tierarzt24",
                    "link": "https://www.tierarzt24.de/almapharm-astoral-almazyme-hk",
                    "price": "25,72 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Vetena",
                    "link": "https://www.vetena.de/almapharm-astoral-Almazyme-Hund.html",
                    "price": "22,45 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Vetmedpro",
                    "link": "https://www.vetmedpro.de/astoralZ-AlmazymeZ-120g-Diaet-Ergaenzungsfuttermittel-fuer-Hunde-und-Katzen",
                    "price": "21,27 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Petshop Vetline",
                    "link": "https://www.petshop-vetline.de/hunde/ergaenzungsfuttermittel/magen-darm/almapharm-astoral-almazyme-120-g",
                    "price": "22,64 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Ebay",
                    "link": "https://www.ebay.de/itm/astoral-Almazyme-120g-Diat-Erganzungsfuttermittel-fur-Hunde-und-Katzen/324480730788",
                    "price": "25,40 €*",
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                }
            ]

        else:

            get = lambda name: self.get(name)

            prices = [
                {
                    "name": "Fuettern Und Fit",
                    "link": "https://www.fuetternundfit.de/astoral-almazyme.html",
                    "price": get("FUETTERNUNDFITT"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Tiershop",
                    "link": "https://www.tiershop.de/Astoral-Almazyme.html",
                    "price": get("TIERSHOP"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Dr. Hölter",
                    "link": "https://www.drhoelter.de/almapharm-astoral-almazyme-hund-katze-nahrungsergaenzung-verdauung-bauchspeicheldruese.html",
                    "price": get("DRHOELTER"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Tierarzt24",
                    "link": "https://www.tierarzt24.de/almapharm-astoral-almazyme-hk",
                    "price": get("TIERARZT24"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Vetena",
                    "link": "https://www.vetena.de/almapharm-astoral-Almazyme-Hund.html",
                    "price": get("VETENA"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Vetmedpro",
                    "link": "https://www.vetmedpro.de/astoralZ-AlmazymeZ-120g-Diaet-Ergaenzungsfuttermittel-fuer-Hunde-und-Katzen",
                    "price": get("VETMEDPRO"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Petshop Vetline",
                    "link": "https://www.petshop-vetline.de/hunde/ergaenzungsfuttermittel/magen-darm/almapharm-astoral-almazyme-120-g",
                    "price": get("PETSHOP_VETLINE"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                },
                {
                    "name": "Ebay",
                    "link": "https://www.ebay.de/itm/astoral-Almazyme-120g-Diat-Erganzungsfuttermittel-fur-Hunde-und-Katzen/324480730788",
                    "price": get("EBAY"),
                    "updated": datetime.now().strftime('%d.%m.%Y %H:%M')
                }
            ]

        # Deep-Copy prices to current float prices
        current_float_prices = deepcopy(prices)

        # Convert every price to a float (current_float_prices) (eg "100,00 €" -> 100.0)
        for dictionary in current_float_prices:
            dictionary["price"] = price_float(dictionary["price"])

        # Assign to current_float_prices
        self.current_float_prices = current_float_prices

        # Save current price
        self.current_prices = deepcopy(prices)

        # Return either as float or as normal price (X,XX €)
        if as_float:
            return self.current_float_prices
        else:
            return self.current_prices

    def sorted_prices(self, as_float):
        # Get current prices (As €)
        prices = deepcopy(self.current_prices)

        # Get current prices sorted
        sorted_prices = sorted(prices, key=self.__sort_prices_by_dic)

        # Convert to floats if needed
        if as_float:
            for dic in sorted_prices:
                dic["price"] = price_float(dic["price"])

        return sorted_prices
