import requests

def get_exchange_rate(from_currency, to_currency):
    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/{from_currency}")
        response.raise_for_status()
        data = response.json()
        rates = data.get('rates', {})
        return rates.get(to_currency)  # Returns None if rate is not available
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None

def parse_amount(amount_str):
    amount_str = amount_str.upper()
    if 'M' in amount_str:
        return float(amount_str.replace('M', '')) * 1_000_000
    elif 'K' in amount_str:
        return float(amount_str.replace('K', '')) * 1_000
    elif 'B' in amount_str:
        return float(amount_str.replace('B', '')) * 1_000_000_000
    else:
        return float(amount_str)

def format_amount(amount):
    if amount >= 1_000_000:
        return f"{amount:,.0f} M"
    elif amount >= 1_000:
        return f"{amount:,.0f} K"
    else:
        return f"{amount:,.2f}"

def convert_currency(from_currency, to_currency, amount):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        print(f"{format_amount(amount)} {from_currency} is {format_amount(converted_amount)} {to_currency}")
    else:
        print(f"Cannot perform conversion. Exchange rate from {from_currency} to {to_currency} is not available.")
        exit()

def main():
    currencies = [
        'AMD',  # Armenian Dram
        'USD',  # US Dollar
        'EUR',  # Euro
        'JPY',  # Japanese Yen
        'KRW',  # Won Korea
        'CNY',  # Chinese Yuan
        'AED',  # Dirham
        'CHF',  # Swiss Franc
        'SGD',  # Singapore Dollar
        'AUD',  # Australian Dollar
        'ILS',  # New Israeli Sheqel
        'RUB',  # Russian Ruble
        'GBP',  # United Kingdom Pound Sterling
        'CAD',  # Canadian Dollar
        'SEK',  # Swedish Krona
        'HKD',  # Hong Kong Dollar
        'NZD',  # New Zealand Dollar
        'NOK',  # Norwegian Krone
        'MXN',  # Mexican Peso
        'INR',  # Indian Rupee
        'BRL',  # Brazilian Real
        'ZAR',  # South African Rand
        'TRY',  # Turkish Lira
        'SAR',  # Saudi Riyal
    ]

    print("Available currencies:", ", ".join(currencies))
    from_currency = input("Enter the currency you'd like to convert from: ").upper()
    to_currency = input("Enter the currency you'd like to convert to: ").upper()

    if from_currency not in currencies or to_currency not in currencies:
        print("Invalid currencies selected. Please select from the available currencies.")
        return

    while True:
        amount_input = input("Enter the amount of money (you can use 'K' for thousands, 'M' for millions, 'B' for billions): ").strip()
        try:
            amount = parse_amount(amount_input)
            convert_currency(from_currency, to_currency, amount)
            break
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

if __name__ == "__main__":
    main()