# def square(num):
#     return num*num
#
#
# def square_print(num):
#     print(num*num)
#
# a = square(10) + 11
# # print(a)
# #
# b = (square_print(10) + 12
# # print(b)
from _ast import While
from random import randint
from typing import List


def multiply(subject, times):
    return subject * times


# print(multiply(10, 2))


def power(base, exponent=2):
    return base ** exponent


# print(power(5))


def to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# print(to_celcius(100))


# def is_even(number):
#     for i in range(1, number):
#         if i % 2 == 0:
#             print(f'{i} is an even number')
#         else:
#             print(f'{i} is an odd number')
#
#
# is_even(9)

# def histogram(numbers):
#     for number in numbers:
#         if not isinstance(number, int):
#             print("Number must be an integer")
#         else:
#             print("#" * number)
#
#
# numbers = [2, 6, "f5", 1]
# histogram(numbers)


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Przykład użycia
# result = fibonacci(10)
# print("Fibonacci(5):", result)  # Wynik: 5


# def list_keys(d):
#     for key in d:
#         print(key)
#
#
# list_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4})


# def find_words(words):
#     for word in words:
#         if len(word) > 7:
#             print(word)
#
#
# find_words(["Python", "Data", "Science", "Artificial", "Intelligence", "Programming"])


# def suma(number):
#     return (number)
#
#
# print(suma([1, 2, 6, 4, 5, 6, 7, 8, 9, 10]))


# def message(input_dict):
#     if key in input_dict != ["name", "role", "movie"]:
#         return "Invalid input"
#     return f"gosc {input_dict['name']}: ma  {input_dict['role']} czaple {input_dict['movie']}"
#
#
# input_dict = {
#
#     "name": "Han Solo",
#
#     "role": "smuggler",
#
#     "movie": "Star Wars"
#
# }
#
# print(message(input_dict))


# def d6(num):
#     rolls = []
#     for i in range(num):
#         rolls.append(randint(1, 6))
#     print(rolls)
#     return sum(rolls)
#
#
# print(d6(6))


# def make_tuple(a,b,c=3,d=3):
#     return (a,b,c,d)
#
#
# nowa = make_tuple('mama', 'tata')
# nowa2 = make_tuple(0, 0, 0, 0)
# print(nowa)
# print(nowa2)


# def find(numbers):
#     return numbers
#
#
# numbers=[1,2,3,4,5,6,7,8,9]
# print(numbers[0:-1])


# def format_date(day, month, year):
#     if not 1 < day < 31 or not 1 < month < 12:
#         return None
#
#     return f"{day} {month} {year}"
#
#
# d = format_date(12, 2, 2017)
# print(d)


# def find_boundaries(numbers):
#     if len(numbers) == 0:
#         return None
#     return max(numbers), min(numbers)
#
#
# b = find_boundaries([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(b)





# def censor(text):
#     bad_words = ["Java", "C#", "Ruby", "PHP"]
#     all_words = text.split()
#     for i in range(len(all_words)):
#         if all_words[i] in bad_words:
#             all_words[i] = "****"
#     return " ".join(all_words)
#
#
# c = censor("Java is the beeeest, but PHP is the bestest!")
# print(c)


# def check_palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
#
# print(check_palindrome("ala"))


# def safe_get(l, index):
#     if index < len(l):
#         return l[index]
#     else:
#         return None
#
#
# l = list(range(1, 100))
# dang = safe_get(l, 551)
# print(dang)


# def divide(a, b):
#
#     if not isinstance(a, int) or not isinstance(b, int) or b == 0:
#         return None
#     else:
#         return a / b
#
#
# print(divide(10,"chu"))


# def phone(number):
#     call_numbers = [123213,12321,24214,21423,21422,21423,21422,21423]
#     if number not in call_numbers:
#         raise ValueError(f'Number {number} is not in {call_numbers}')
#     else:
#         return number


# print(phone(2212321))

# def random_averange(n):
#         sum_num = list(range(1, n + 1))
#         return sum(sum_num) / len(sum_num)
#
# n = randint(1, 100)
# print(random_averange(n))


# def div():
#     while True:
#         try:
#             a = int(input("Give me two numbers: :"))
#             b = int(input("Give me three numbers: :"))
#             if a == 0 and b == 0 or not isinstance(a, int) or not isinstance(b, int):
#                 raise ValueError
#             return a / b
#         except ValueError:
#             print("Invalid input")
#
#
#
# print(div())


def find_number(number):
    min_v = 0
    max_v = 1000
    print("DDASDSADA")
    print(f"czy twoja liczba to {guess}?")
    answer = input("Please say:")
    while answer != "YES":

        guess = int((max_v - min_v) // 2) - min_v


        if answer == "too small":
            min_v = guess
        elif answer == "too big":
            max_v = guess


    print("YOU CRAZY")





