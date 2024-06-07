def format_email(name, date, email, place='Казань'):
    return "To: {}\nЗдравствуйте, {}!\nБыли бы рады видеть вас на собеседовании разработчиков" \
           " {}е, которая пройдет {}.".format(
        email, name, place, date)


print(format_email(name='Арсений', date="14.02.2016", email="ars@mail.ru"))