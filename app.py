from flask import Flask, render_template, request
import pandas as pd
import subprocess

app = Flask(__name__)


@app.route("/")
def toppage():
    return render_template("top.html")


@app.route("/s-display", methods=["POST"])
def get_res_name():
    res_name = request.form("res_name")
    return res_name


def start_scraping():
    scraping_file = ["python", "scraping/main.py", "スクレイピング中"]
    proc = subprocess.Popen(scraping_file)
    proc.communicate()


def res_name_csv():
    df = pd.read_csv("scraping/assesment.csv")
    header = df.columns
    record = df.values.tolist()
    return render_template("s-display.html", header=header, record=record)


@app.route("/display", methods=["POST"])
def display_csv():
    scraping_file = ["python", "scraping/main.py", "スクレイピング中"]
    proc = subprocess.Popen(scraping_file)
    proc.communicate()
    df = pd.read_csv("scraping/assesment.csv")
    header = df.columns
    record = df.values.tolist()
    # print(df)
    return render_template("display.html", header=header, record=record)


if __name__ == "__main__":
    app.run(debug=True)