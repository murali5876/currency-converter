from forex_python.converter import CurrencyRates

def get_exchange_rate(amount, from_currency, to_currency):
    c = CurrencyRates()
    rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount, rate

def main():
    user_name = input("Enter your name: ")
    print(f"Welcome {user_name} to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("Enter the source currency code (e.g., USD): ").upper()
            to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

            converted_amount, exchange_rate = get_exchange_rate(amount, from_currency, to_currency)

            print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            print(f"Exchange rate: 1 {from_currency} = {exchange_rate:.4f} {to_currency}")
            print(f"Thank you, {user_name}, for using the Currency Converter!\n")

        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
        except Exception as e:
            print(f"Error: {e}")

        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

    print(f"Thank you {user_name} for using the Currency Converter!")

if __name__ == "__main__":
    main()
