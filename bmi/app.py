from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    color = None

    if request.method == "POST":
        try:
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            height_m = height / 100  
            bmi = round(weight / (height_m ** 2), 2)
            if bmi < 18.5:
                category = "Underweight"
                color = "red"
            elif 18.5 <= bmi < 24.9:
                category = "Normal"
                color = "green"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "red"
            else:
                category = "Obese"
                color = "purple"

        except (ValueError, ZeroDivisionError):
            bmi = None
            category = "Invalid input"
            color = "black"

    return render_template("index.html", bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(debug=True)
