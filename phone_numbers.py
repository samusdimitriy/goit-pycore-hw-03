import re

def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    cleaned = re.sub(r'[^\d+]', '', phone_number)

    if cleaned.startswith('+'):
        return '+' + re.sub(r'[^\d]', '', cleaned)
    elif cleaned.startswith('380'):
        return '+' + cleaned
    else:
        return '+38' + re.sub(r'[^\d]', '', cleaned)

def get_phone_number():
    phone_number = input("Enter a phone number: ")
    normalized = normalize_phone(phone_number)

    if re.fullmatch(r'\+380\d{9}', normalized):
        print(f"Valid phone number: {normalized}")
    else:
        print("Invalid phone number format. Please enter a valid Ukrainian phone number.")

get_phone_number()
