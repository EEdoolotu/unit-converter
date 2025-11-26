import conversions

length_units = ["meters", "kilometers", "miles", "feet"]
weight_units = ["grams", "kilograms", "pounds"]
temperature_units = ["celsius", "fahrenheit", "kelvin"]


def main():
    print("What unit would you like to convert: \n1. length \n2. weight \n3. temperature \n 1, 2 or 3?")
    unit_type = int(input())
    category = ""
    if unit_type == 1:
        category = "length"
    elif unit_type == 2:
        category = "weight"
    elif unit_type == 3:
        category = "temperature"
    else:
        raise ValueError("Please choose out of the 3 options(1, 2, 3)")

    unit_list = []

    if category == "length":
        unit_list = length_units
    elif category == "weight":
        unit_list = weight_units
    elif category == "temperature":
        unit_list = temperature_units

    
    print(f"You selected {category}")
    print(f'These are the units you can convert from.')
    print(unit_list)
    unit_from = input("Which unit are you converting from? ").lower()
    while unit_from not in unit_list:
        print("Invalid input, please try again")
        unit_from = input("Try again... ").lower()

    unit_to = input("Which unit are you converting to? ").lower()
    while unit_to not in unit_list:
        print("Invalid input, please try again")
        unit_to = input("Try again.. ").lower()


    value = float(input("Enter the value you want to convert "))

    if category == "length":
        result = conversions.convert_length(value, unit_from, unit_to)
    elif category == "weight":
        result = conversions.convert_weight(value, unit_from, unit_to)
    elif category == "temperature":
        result = conversions.convert_temperature(value, unit_from, unit_to)

    print(f'{value} {unit_from} has been converted to {result} {unit_to}')

if __name__ == "__main__":
    main()
