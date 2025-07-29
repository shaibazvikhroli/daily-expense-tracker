from flask import Flask, render_template, request, redirect
import csv
import os
from datetime import datetime

app = Flask(__name__)
FILENAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Category", "Note"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    amount = request.form["amount"]
    category = request.form["category"]
    note = request.form["note"]
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])
    return redirect("/")

@app.route("/view")
def view():
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            next(reader)
            expenses = list(reader)
    return render_template("view.html", expenses=expenses)

@app.route("/total")
def total():
    total = 0.0
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                total += float(row[1])
    return render_template("total.html", total=total)

if __name__ == "__main__":
    init_file()
    app.run(debug=True)
