import re
from random import randint


def dice():
    while True:
        print('Witaj ludziu')
        user_answer = input('podaj czym chcesz rzucić: xDy+z')
        pattern = r'\d+[Dd]\d+\+\d+'
        if re.match(pattern, user_answer):
            print('good')
            result = re.split(r'[Dd+]', user_answer)
            x = result[0]
            y = result[1]
            z = result[2]
            dice_throw = int(x) * randint(1, int(y)) + int(z)
            print(dice_throw)
            return dice_throw
        else:
            print('najn, wrong string')



dice()
