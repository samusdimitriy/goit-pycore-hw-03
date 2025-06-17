import random

def get_numbers_ticket(min, max, quantity):
    is_range_valid = 1 <= min < max <= 1000
    is_quantity_valid = min <= quantity <= (max - min + 1)

    if not (is_range_valid and is_quantity_valid):
        return []

    available_numbers = range(min, max + 1)
    selected_numbers = random.sample(available_numbers, quantity)
    return sorted(selected_numbers)

input_min = int(input("Enter the minimum number (1-999): "))
input_max = int(input("Enter the maximum number (2-1000): "))
input_quantity = int(input("Enter the quantity of numbers (1-1000): "))
numbers = get_numbers_ticket(input_min, input_max, input_quantity)

if numbers:
    print(f"Generated numbers: {numbers}")
else:
    print("Invalid input. Please ensure the minimum is less than the maximum, and the quantity is within the valid range.")
