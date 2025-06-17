from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if (birthday_this_year - today).days <= 7:
            congrats_date = birthday_this_year

            if congrats_date.weekday() >= 5:
                congrats_date += timedelta(days=7 - congrats_date.weekday())

            result.append({
                'name': user['name'],
                'congratulation_date': congrats_date.strftime("%Y.%m.%d")
            })
    return result
if __name__ == "__main__":
    users = [
        {'name': 'Олександр', 'birthday': '1990.06.20'},
        {'name': 'Марія', 'birthday': '1985.06.18'},
        {'name': 'Дмитро', 'birthday': '2000.06.22'},
        {'name': 'Анна', 'birthday': '1992.06.19'},
        {'name': 'Іван', 'birthday': '1995.06.24'},
        {'name': 'Катерина', 'birthday': '1988.06.21'},
        {'name': 'Михайло', 'birthday': '1993.06.15'},
        {'name': 'Софія', 'birthday': '1997.07.05'},
        {'name': 'Андрій', 'birthday': '1991.05.10'},
        {'name': 'Юлія', 'birthday': '1994.06.23'},
        {'name': 'Володимир', 'birthday': '1989.12.25'},
        {'name': 'Оксана', 'birthday': '1996.03.08'}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Найближчі дні народження:")
    if upcoming_birthdays:
        for user in upcoming_birthdays:
            print(f"{user['name']} - {user['congratulation_date']}")
    else:
        print("Немає днів народження у найближчі 7 днів")
