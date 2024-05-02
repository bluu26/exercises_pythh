from random import randint


def guess_numb():
    print('Hello player')
    r_num = randint(1, 100)
    print(f'{r_num}')
    while True:
        try:
            user_num = int(input('guess number: '))
        except ValueError:
            print('xxxx')
            continue
        if user_num > r_num:
            print('too big')
        elif user_num < r_num:
            print('too small')
        else:
            print('u won')
            return


guess_numb()

