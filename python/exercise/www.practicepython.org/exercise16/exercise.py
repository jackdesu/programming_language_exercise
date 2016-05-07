import random


def get_random_symbol():
    random_symbol = []
    random_symbol.extend(chr(x) for x in range(35, 38))
    random_symbol.extend(chr(x) for x in range(40, 44))
    random_symbol.extend(chr(x) for x in range(58, 65))
    random_symbol.remove(chr(63))
    random_symbol.remove(chr(64))
    return random_symbol


def get_random_int():
    random_symbol = []
    random_symbol.extend(chr(x) for x in range(48, 60))
    return random_symbol


def get_random_lower_cases():
    random_symbol = []
    random_symbol.extend(chr(x) for x in range(97, 123))
    return random_symbol


def get_random_upper_cases():
    random_symbol = []
    random_symbol.extend(chr(x) for x in range(65, 91))
    return random_symbol


def generate_password(ori_strength):
    # to ask user how strong she/he want to (1 ~ 4)
    strength = ori_strength
    # according to the strength, to random pick candidate
    password_set = [get_random_symbol(), get_random_int(), get_random_lower_cases(), get_random_upper_cases()]
    # let's randomly pick password length from 8 ~ 12
    password_candidate = []
    while True:
        password_candidate.append(password_set.pop(random.randint(0, len(password_set)-1)))
        strength -= 1
        if strength <= 0:
            break

    print(password_candidate)

    # to generate password and display it
    password = ""
    for x in range(0, random.randint(8, 13)):
        temp_password_set = password_candidate[random.randint(0, len(password_candidate)-1)]
        password += temp_password_set[random.randint(0, len(temp_password_set)-1)]

    print("your password: " + password)


while True:
    user_input = int(raw_input("please tell me the password strength you need (1 ~ 4): "))
    generate_password(user_input)
    if "y" != raw_input("To generate a new password? ").lower():
        print("Bye!")
        break
