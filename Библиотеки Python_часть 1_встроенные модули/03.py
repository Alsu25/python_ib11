from random import choices, choice, shuffle
from string import ascii_lowercase as a_l
from string import ascii_uppercase as a_u
from string import digits

SYMBOLS_LOW = a_l[:11] + a_l[12:14] + a_l[15:]
SYMBOLS_UP = a_u[:8] + a_u[9:14] + a_u[15:]
SYMBOLS_DIG = digits[2:]


def generate_password(m):
    password = choices(SYMBOLS_LOW, k=m - 2)
    password.append(choice(SYMBOLS_UP))
    password.append(choice(SYMBOLS_DIG))
    shuffle(password)
    return ''.join(password)


def main(n, m):
    passwords = {generate_password(m) for _ in range(n)}
    while len(passwords) < n:
        passwords.add(generate_password(m))
    passwords = list(passwords)
    return passwords
