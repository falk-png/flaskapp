from flask import render_template, Blueprint, send_file
from price_tools.DataManager import DataManager

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
