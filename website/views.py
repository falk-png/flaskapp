from flask import render_template, Blueprint, flash, url_for, send_file
from price_tools.DataManager import DataManager
from price_tools.tools import price_float
from website_tools.ExcelManager import ExcelManager


views = Blueprint("views", __name__)
data_mng = DataManager()


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/overview/", methods=["GET", "POST"])
def overview():
    # Get prices
    prices = data_mng.sorted_prices(as_float=False)


    return render_template("overview.html", prices=prices)


@views.route("/download/")
def download():
    path = r"etc_files\prices.xlsx"
    file = send_file(path, as_attachment=True)

    return file
