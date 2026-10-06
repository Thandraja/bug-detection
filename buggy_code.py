def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return average


def find_largest(numbers):
    largest = 0

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def get_user_details(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def calculate_discount(price, discount_percentage):
    discount = price * discount_percentage
    final_price = price - discount

    return final_price


def main():
    numbers = [10, 20, 30, 40]

    average = calculate_average(numbers)
    print("Average:", average)

    largest = find_largest(numbers)
    print("Largest:", largest)

    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

    user = get_user_details(users, 3)
    print("User:", user["name"])

    final_price = calculate_discount(1000, 20)
    print("Final price:", final_price)


if __name__ == "__main__":
    main()