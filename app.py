from flask import Flask, render_template, request #TODO I don't know why Flask literally is not working, I've downaloded it so many times & redownlaoded it
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mbta_station/', methods=["GET", "POST"])
def closest_mbta_station(): 
    if request.method == "POST":
        place_name = request.form["Location"]
        find_stop = find_stop_near(place_name)

        return render_template("MBTA_result.html", location=place_name, MBTA_stop=find_stop)

    return render_template("MBTA__first_form.html")


if __name__ == '__main__':
    app.run(debug=True)
