from datetime import datetime
from random import random, randint, shuffle

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hi():
    cur_time = datetime.now()
    return f"{cur_time}"


@app.route('/num/<int:a>/<int:b>', methods=['GET', 'POST'])
def num(a, b):
    _suma = a + b
    return str(_suma)


@app.route('/losuj', methods=['GET', 'POST'])
def losuj():
    zbiur = []
    for i in range(3):
        num_rand = randint(1, 10)
        zbiur.append(str(num_rand))
    return ','.join(zbiur)


@app.route('/lotto', methods=['GET', 'POST'])
def lotto():
    lst = [i for i in range(1, 50)]
    shuffle(lst)
    return str(lst[:6])

@app.route('/imie', methods=['GET', 'POST'])
def imie():
    FORM = """
    <form method="POST">
    <input type="text" name="imie">
    <input type="submit">
    </FORM>"""
    if request.method == 'POST':
        imie = request.form['imie']
        return f"twoje imie {imie}"
    else:
        return FORM


@app.route('/minik', methods=['GET', 'POST'])
def minik():

    form = """
    <form method="POST">
    <br><br><br>
    <center>"SUPER MAGICZnY KALKULATOR"<br><br>
    <center>"BARTKA GASZCZYKA"<br><br><br>
    <input type="int" name="number1">
    <input type="int" name="number2">
    <select name="operations">
    <option value = "add">dodaj</option>
    <option value = "subtract">odejmij</option>
    <option value = "multiply">pomnusz</option>
    <option value = "divide">pociel</option>
    </select>
    <input type="submit" value="ZDETONUJ">
    </center>
    </form>    
    """
    if request.method == 'POST':
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        operations = request.form['operations']
        if operations == "add":
            result = number1 + number2
        elif operations == "subtract":
            result = number1 - number2
        elif operations == "multiply":
            result = number1 * number2
        elif operations == "divide":
            result = number1 / number2

        return form + f"<div style='text-align:center;'>{str(result)}</div>"
    return form


r_liczba = randint(1, 10)
print(r_liczba)

@app.route('/zgad', methods=['GET', 'POST'])
def zgad():
    form = """
    <form method="POST">
    Zgadnij liczbę ziomku
    <input type="text" name="liczba">
    <input type="submit" value="Wyślij">
    </form>    
    """


    if request.method == 'POST':
        user_answer = int(request.form['liczba'])
        if user_answer < r_liczba:
            return form + f"za malii"
        elif user_answer > r_liczba:
            return form + f"za duzi"
        elif user_answer == r_liczba:
            return f"its good"

    return form

@app.route('/o', methods=['GET', 'POST'])
def o():
    if request.method == 'POST':
        return "Wyslales post"
    elif request.method == 'GET':
        return "Wyslales get"


@app.route('/koko', methods=['GET', 'POST'])
def koko():
    form = """
    <form method="POST">
    <input type="text" name="name">
    <input type="text" name="forname">
    <input type="submit" value="sent">
    </form>
    """
    if request.method == 'POST':
        name = request.form['name']
        forname = request.form['forname']
        return f"{name} {forname}"
    return form

@app.route('/dejn', methods=['GET', 'POST'])
def dejn():
    form = """
    <form method="POST">
    PODAJ LICZBĘ NATURALNĄ <br>
    <input type="text" name="n">
    <input type="submit" value="ZDETONUJ">
    </form>
    """
    if request.method == 'GET':
        return form
    elif request.method == 'POST':
        n = int(request.form['n'])
        zen = str(2 * n)
        xen = str(2 * n)
        cen = str(2 * n)
        table = f'<table border="1"><tr><td>{zen}</td><td>{xen}</td><td>{cen}</td></tr></table>'
        return table


@app.route('/postcode', methods=['GET', 'POST'])
def postcode():
    form = """
    PODAJ MIE KOT
    <form method="POST">
    <input type="text" name="postcode">
    <input type="submit" value="ZDETONUJ">
    </table>
    """
    if request.method == 'POST':
        postcode = request.form['postcode']
        post_lst = list(postcode)
        if (len(post_lst) == 6 and post_lst[2] == '-'
                and post_lst[0].isdigit()
                and post_lst[1].isdigit()
                and post_lst[3].isdigit()
                and post_lst[4].isdigit()
                and post_lst[5].isdigit()):

            return "Kod poprawny"
        else:
            return "Kod niepoprawny"
    return form















if __name__ == "__main__":
    app.run(debug=True)