def ask_password(login: str, password: str, success, failure):
    login = login.lower()
    password = password.lower()

    num_vowels = password.count("a") + password.count("e") + password.count("i") + password.count("o") + password.count("u") + password.count("y")
    consonants = "".join([char for char in password if char not in "aeiouy"])

    login_num_vowels = login.count("a") + login.count("e") + login.count("i") + login.count("o") + login.count("u") + login.count("y")
    login_consonants = "".join([char for char in login if char not in "aeiouy"])

    if num_vowels != login_num_vowels:
        failure(login, "Wrong number of vowels")
    elif consonants != login_consonants:
        failure(login, "Wrong consonants")
    else:
        success(login)


def main(login: str, password: str):

    def success_callback(login):
        print(f"Привет, {login}!")

    def failure_callback(login, error):
        print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error.upper()}.")

    ask_password(login, password, success_callback, failure_callback)


if __name__ == "__main__":
    login = input()
    password = input()
    main(login, password)
