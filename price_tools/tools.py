from money_parser import price_str as price_from_raw
from money import Money
from babel.numbers import format_currency


def price_float(price_raw: str, default="0"):
    # Convert to valid number
    money = price_from_raw(price_raw, default=default)
    # Convert to float
    money = float(money)

    return money


def price_eur(price_raw: str, default="0"):
    # Convert to valid number
    money_float = price_float(price_raw, default=default)
    # Create money object and format to eur
    money = Money(money_float, "EUR")
    money = money.format("de_DE", "#,##0.00 ¤")

    return money
    
