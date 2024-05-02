def guess_number():
    print("pomysl liczbe od 1-1000")
    _min = 0
    _max = 1000
    while True:
        guess = int((_max - _min)/2 + _min)
        print(f'czy twoja liczba to {guess}?')
        user_answer = input('zduzo/zmalo/good')
        if user_answer == 'zduzo':
            _max = guess
        if user_answer == 'zmalo':
            _min = guess
        else:
            if user_answer == "good":
                print('zgadles')
                print(f'twoja liczba to {guess}')
            break


guess_number()


