from flask import Flask, render_template
import sensors

w = sensors.Weather()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = w.get_weather_info()
    return render_template("index.html", temp=data["temperature"], humidity=data["humidity"], pressure=data["pressure"])

