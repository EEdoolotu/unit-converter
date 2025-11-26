def convert_length(value, unit_from, unit_to):
    factors = {
        "meters" : 1,
        "kilometers" : 1000,
        "miles" : 1609.34,
        "feet" : 0.3048
    }
    value_in_metres = value * factors[unit_from]
    return value_in_metres / factors[unit_to]

def convert_weight(value, unit_from, unit_to):
    factors = {
        "grams" : 1,
        "kilograms" : 1000,
        "pounds" : 453.592
    }

    value_in_grams = value * factors[unit_from]
    return value_in_grams / factors[unit_to]

def convert_temperature(value, unit_from, unit_to):
    if unit_from == unit_to:
        return value
    if unit_from == "celsius":
        if unit_to == "fahrenheit":
            return (value * 9/5) + 32
        elif unit_to == "kelvin":
            return value + 273.15
    elif unit_from == "fahrenheit":
        if unit_to == "celsius":
            return (value - 32) * 5/9
        elif unit_to == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif unit_from == "kelvin":
        if unit_to == "celsius":
            return value - 273.15
        elif unit_to == "fahrenheit":
            return (value - 273.15) * 9/5 + 32