from flask import Flask, render_template, request
import conversions 

app = Flask(__name__)

length_units = ["meters", "kilometers", "miles", "feet"]
weight_units = ["grams", "kilograms", "pounds"]
temperature_units = ["celsius", "fahrenheit", "kelvin"]

@app.route("/", methods=["GET", "POST"])
def index():
    category = request.form.get("category", "length")  # default tab
    result = None

    if request.method == "POST":
        unit_from = request.form["unit_from"]
        unit_to = request.form["unit_to"]
        value = float(request.form["value"])

        if category == "length":
            result = conversions.convert_length(value, unit_from, unit_to)
        elif category == "weight":
            result = conversions.convert_weight(value, unit_from, unit_to)
        elif category == "temperature":
            result = conversions.convert_temperature(value, unit_from, unit_to)

    return render_template(
        "index.html",
        category=category,
        length_units=length_units,
        weight_units=weight_units,
        temperature_units=temperature_units,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
