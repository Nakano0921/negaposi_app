from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["POST"])
def toppage():
    print(request.form)
    # main.pyを動かすコードを書く
    # displayに行くコードを書く
    return render_template("top.html")


@app.route("/display", methods=["POST"])
def desplay_csv():
    # lacal_name = request.form.get("local_name")
    df = pd.read_csv("/Users/nakanoken/lessons/scraping/assesment.csv")
    header = df.columns
    record = df.values.tolist()
    print(df)
    return render_template("display.html", header=header, record=record)


if __name__ == "__main__":
    app.run()