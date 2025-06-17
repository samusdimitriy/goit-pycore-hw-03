from datetime import datetime

def get_days_from_today(date_str):
    formats = [
        "%Y-%m-%d",
        "%d.%m.%Y",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%d-%m-%Y"
    ]

    for fmt in formats:
        try:
            given_date = datetime.strptime(date_str, fmt).date()
            today = datetime.today().date()
            return (today - given_date).days
        except:
            continue

    print("Invalid date format. Please use a supported format.")
    return None

user_input = input("Enter a date (e.g. 2023-10-01, 01.10.2023, 10/01/2023): ")
result = get_days_from_today(user_input)

if result is not None:
    print(f"Days from today: {result}")
