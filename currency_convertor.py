def convert_currency(from_currency, to_currency, amount):
    exchange_rates = {
        'USD': {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.72, 'INR': 74.98},
        'EUR': {'USD': 1.18, 'EUR': 1.0, 'GBP': 0.85, 'INR': 88.45},
        'GBP': {'USD': 1.39, 'EUR': 1.18, 'GBP': 1.0, 'INR': 104.23},
        'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.0096, 'INR': 1.0}
    }

    try:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        return f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
    except KeyError:
        return "Invalid currency."

if __name__ == "__main__":
    from_currency = input("Enter the source currency (e.g., USD, EUR, GBP, INR): ").upper()
    to_currency = input("Enter the target currency (e.g., USD, EUR, GBP, INR): ").upper()
    amount = float(input("Enter the amount: "))

    result = convert_currency(from_currency, to_currency, amount)
    print(result)
