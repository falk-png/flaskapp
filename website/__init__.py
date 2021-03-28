import yaml
from flask import Flask
from flask_apscheduler import APScheduler
from website_tools.ExcelManager import ExcelManager
from .views import views, data_mng


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

    # Update excel file
    excel_mng = ExcelManager("website/etc_files/prices.xlsx")
    excel_mng.get_xlsx_file(data_mng.sorted_prices(as_float=True))

    # Configurate scheduler
    scheduler = APScheduler()
    scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    # Schedulers:

    @scheduler.task('interval', id='update_prices', minutes=60, misfire_grace_time=900)
    def update_prices():
        print("Updating prices.. ", end="")

        # Define compareable price variables
        old_float_prices = data_mng.current_float_prices
        new_float_prices = data_mng.get_prices(as_float=True)

        # Get old and new prices
        prices_old = [price["price"] for price in old_float_prices]
        prices_new = [price["price"] for price in new_float_prices]

        # Check if something changed
        prices_changed = prices_old != prices_new

        # Print if something changed
        if prices_changed:
            changed_text = f"Something changed!"
        else:
            changed_text = "Nothing changed"

        print(changed_text)

        # Update excel file
        excel_mng = ExcelManager("website/etc_files/prices.xlsx")
        excel_mng.get_xlsx_file(data_mng.sorted_prices(as_float=True))

    return app
