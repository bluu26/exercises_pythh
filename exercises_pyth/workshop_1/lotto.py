from random import randint


def lotto():
    print("WITAJ GRAczU")

    def r_numbers():
        ra_numbers = []
        for i in range(6):
            number = randint(1, 49)
            if number not in ra_numbers:
                ra_numbers.append(number)
                ra_numbers.sort()
        return ra_numbers

    print(r_numbers())

    r_nums = r_numbers()

    def user_guess():
        x = 1
        user_numbers = []
        while True:

            if len(user_numbers) < 6:
                try:
                    user_number = int(input(f'podaj mi liczbe: {x} \n'))
                except ValueError:
                    print('not number')
                if user_number not in user_numbers and 0 < user_number < 50:
                    user_numbers.append(user_number)
                    x += 1
                else:
                    print('wroooong number')
            else:
                user_numbers.sort()
                print(user_numbers)
                return user_numbers

    user_nums = user_guess()

    def compare_num(r_nums, user_nums):
        shots = 0
        for num in r_nums:
            if num in user_nums:
                shots += 1
        print(shots)
        return shots
    _shots= compare_num(r_nums, user_nums)
    print(f'wylosowane liczby: {r_nums}')
    print(f'twoje liczby: {user_nums}')
    print(f'strzauy {_shots}')


lotto()
