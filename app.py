from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def toppage():
    return render_template("top.html")


@app.route("/display", methods=["POST"])
def display_csv():
    df = pd.read_csv("assesment.csv")
    header = df.columns
    record = df.values.tolist()
    # print(df)
    return render_template("display.html", header=header, record=record)


if __name__ == "__main__":
    app.run(debug=True)