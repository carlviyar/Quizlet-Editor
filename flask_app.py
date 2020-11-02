from flask import Flask, request, redirect, render_template, session
from openpyxl import Workbook, load_workbook
from datetime import datetime
import quizlet

app = Flask(__name__)
app.secret_key = b'yuhgetintoit'

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/submit", methods=["GET"])
def submit():
    link = request.args.get(key='url')
    lst = quizlet.find_terms(quizlet.get_quizlet_set(link))
    session['number_of_cards'] = len(lst)
    return render_template("received.html", cards=lst)

@app.route("/cards", methods=["POST"])
def display_cards():
    number_of_cards = session.get('number_of_cards')
    quizlet_string = ""
    for card_num in range(1,number_of_cards+1):
        card_term = request.form.get('term' + str(card_num))
        definition_term = request.form.get('definition' + str(card_num))
        quizlet_string += card_term + "\t" + definition_term + "\n"
    return render_template("finished_cards.html", output=quizlet_string)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
