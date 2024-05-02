import re


def check_pattern():
    while True:
        pattern = r"(^\d*[Dd]\d+([+-]\d+)?)( .*)*$"
        user_word = input("Please input a pattern: ")
        if re.match(pattern, user_word):
            print("good")
            print(user_word)
            return True
        else:
            # print("blablabla")
            # print(user_word)
            return False

pattern = check_pattern()
print("entered pattern:", pattern)







