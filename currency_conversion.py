def convert_my_dollars(usd, currency):
    pass # use CONVERSION_RATES dictionary
    if currency[0].lower() in "aeiou":
        return f"You now have {CONVERSION_RATES[currency]*usd} of {currency}."
    else:
        return f"You now have {int(str(CONVERSION_RATES[currency]),2)*usd} of {currency}."