!pip install forex_python

from forex_python.converter import CurrencyRates
c = CurrencyRates()
print("Type the currencies you'd like to convert:")
fr = input("\nFrom Currency: ").upper()
af = input("To Currency: ").upper()
amt = int(input("Amount: "))
print(fr, "to", af, amt)
result = c.convert(fr, af, amt)
print(result)