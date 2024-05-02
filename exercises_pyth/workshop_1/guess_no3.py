from flask import Flask, request

app = Flask(__name__)


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    liczba = 500
    form = f'Czy twoja liczba to {liczba}?'
    form += """

    <form method = 'POST'>
    <input type = 'submit' name = 'ts' value = 'Too small'>
    <input type = 'submit' name = 'tb' value = 'Too big'>
    <input type = 'submit' name = 'uw' value = 'You win'>
    </form>
    """

    if request.method == "POST":
        _min = 0
        _max = 1000
        while True:
            _guess = int((_max - _min) / 2 + _min)
            print(f'czy twoja liczba to {_guess}?')
            if 'tb' in request.form:
                _max = _guess
            if 'ts' in request.form:
                _min = guess
            else:
                if 'uw' in request.form:
                    print('zgadles')
                    print(f'twoja liczba to {_guess}')
                break

    return form


if __name__ == "__main__":
    app.run(debug=True)
