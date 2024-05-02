from random import randint


def shorten(x):
    expression = x.split(' ')
    first_letters = ''.join([word[0].title() for word in expression])

    print(first_letters)


# shorten('hello my name is kuku')


def name_sorter(list_name):
    my_dict = {
        'male': [],
        'female': []
    }
    for word in list_name:
        if word.endswith('a'):
            my_dict['female'].append(word)
        else:
            my_dict['male'].append(word)
    for key in my_dict:
        print(key, sorted(my_dict[key]))


list_name = ['Adam', 'Anna', 'Bartek', 'Kasia', 'Piotr', 'Martyna', 'Tomasz', 'Natalia']
# name_sorter(list_name)

def check_palindrome(_word):
    if _word == _word[::-1]:
        return True

# print(check_palindrome("ALA ALA ALA"))


def div(a, b):
    _div = range(a, b+1)
    num_list = []
    for num in _div:
        if num % 2 == 0 and num % 3 != 0:
            num_list.append(num)
    return num_list


# print(div(1, 20))

def roll(dice_amount, dice_type=6, added_num=0):
    if dice_type not in [3, 4, 6, 8, 10, 12]:
        raise ValueError('Invalid dice type. Allowed types are: 3, 4, 6, 8, 10, 12')

    result = dice_amount * randint(1, dice_type) + added_num
    print(result)



roll(10,5, -3)



