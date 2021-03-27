from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import views, data_mng
from flask_apscheduler import APScheduler
from price_tools.DataManager import DataManager
import yaml
from time import sleep
from website_tools.ExcelManager import ExcelManager


def create_app():
    # Define config variable
    with open("config.yml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)


    # Create flask app
    app = Flask(__name__)

    app.register_blueprint(views)
    app.config["SECRET_KEY"] = "QQKOPW=69420=§§QQQÖÖ;C;_:YA*WÖD?`§?=Ò§?=`?`Q§="
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.debug = config["debug_mode"]


    # Configurate scheduler
    scheduler = APScheduler()
    scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    # Schedulers:

    @scheduler.task('interval', id='update_prices', minutes=30, misfire_grace_time=900)
    def update_prices():
        print("Updating prices.. ", end="")
        sleep(1)
        
        # Define compareable price variables
        old_prices = data_mng.current_prices
        new_prices = data_mng.get_prices()

        # Update prices
        data_mng.current_prices = new_prices
        
        # Check if something changed
        prices_changed = old_prices != new_prices

        # Define "changed" text
        if prices_changed:
            changed_text = f"{old_prices} got {new_prices}"
        else:
            changed_text = "Nothing changed"

        print(changed_text)


    @scheduler.task('interval', id='update_excel_file', seconds=4, misfire_grace_time=900)
    def update_excel_file():
        excel_mng = ExcelManager("website/etc_files/prices.xlsx")
        excel_mng.get_xlsx_file(data_mng.sorted_prices)

        



    return app

