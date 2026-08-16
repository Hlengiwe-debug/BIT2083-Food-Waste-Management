# ============================================================
# DONATE FOOD MODULE
# ============================================================

import json
from datetime import datetime, date
from pathlib import Path


DATA_FILE = Path(__file__).parent / "food_data.json"


def load_data():
    """Load data from the JSON file."""

    if not DATA_FILE.exists():

        return {
            "food_items": [],
            "distribution_history": [],
            "disposal_records": []
        }

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (json.JSONDecodeError, OSError):

        return {
            "food_items": [],
            "distribution_history": [],
            "disposal_records": []
        }


def save_data(data):
    """Save data to the JSON file."""

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def generate_food_id():
    """Generate a unique ID such as F001."""

    data = load_data()

    numbers = []

    for food in data["food_items"]:

        food_id = food.get("id", "")

        if (
            food_id.startswith("F")
            and food_id[1:].isdigit()
        ):

            numbers.append(
                int(food_id[1:])
            )

    for record in data["disposal_records"]:

        food_id = record.get("food_id", "")

        if (
            food_id.startswith("F")
            and food_id[1:].isdigit()
        ):

            numbers.append(
                int(food_id[1:])
            )

    next_number = max(
        numbers,
        default=0
    ) + 1

    return f"F{next_number:03d}"


def calculate_priority(expiry_date):
    """
    Calculate food priority based on
    how close the expiry date is.

    Higher priority = expires sooner.
    """

    expiry = datetime.strptime(
        expiry_date,
        "%Y-%m-%d"
    ).date()

    days_remaining = (
        expiry - date.today()
    ).days

    if days_remaining <= 2:
        return 10

    elif days_remaining <= 5:
        return 9

    elif days_remaining <= 10:
        return 8

    elif days_remaining <= 20:
        return 6

    elif days_remaining <= 30:
        return 4

    else:
        return 2


def get_positive_amount():
    """Ask the user for a valid food amount."""

    while True:

        try:

            amount = int(
                input("Amount: ").strip()
            )

            if amount > 0:
                return amount

            print("Amount must be greater than 0.")

        except ValueError:

            print(
                "Invalid input. "
                "Please enter a whole number."
            )


def get_expiry_date():
    """Ask the user for a valid future expiry date."""

    while True:

        expiry_date = input(
            "Expiry Date (YYYY-MM-DD): "
        ).strip()

        try:

            selected_date = datetime.strptime(
                expiry_date,
                "%Y-%m-%d"
            ).date()

            if selected_date < date.today():

                print(
                    "The expiry date cannot "
                    "already have passed."
                )

                continue

            return selected_date.isoformat()

        except ValueError:

            print(
                "Invalid date format."
            )

            print(
                "Please use YYYY-MM-DD."
            )


def donate_one_food():
    """Collect information and add one food item."""

    print("\n" + "-" * 60)
    print("                 FOOD DONATION")
    print("-" * 60)

    # Get food name
    while True:

        food_name = input(
            "Food Name: "
        ).strip()

        if food_name:
            break

        print(
            "Food name cannot be empty."
        )

    # Get amount
    amount = get_positive_amount()

    # Get expiry date
    expiry_date = get_expiry_date()

    # Automatically calculate priority
    priority = calculate_priority(
        expiry_date
    )

    food = {
        "id": generate_food_id(),
        "name": food_name,
        "amount": amount,
        "expiry_date": expiry_date,
        "priority": priority
    }

    data = load_data()

    data["food_items"].append(food)

    save_data(data)

    print("\n" + "=" * 60)
    print("             DONATION SUCCESSFUL")
    print("=" * 60)

    print(
        f"Food ID      : {food['id']}"
    )

    print(
        f"Food Name    : {food['name']}"
    )

    print(
        f"Amount       : {food['amount']}"
    )

    print(
        f"Expiry Date  : {food['expiry_date']}"
    )

    print(
        f"Priority     : {food['priority']}/10"
    )

    print("=" * 60)


def donate_food_page():
    """Display the Donate Food page."""

    while True:

        print("\n" + "=" * 60)
        print("                    DONATE FOOD")
        print("=" * 60)

        print("1. Donate Food")
        print("2. Add Another Food")
        print("3. Back to Main Menu")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            donate_one_food()

        elif choice == "2":

            donate_one_food()

        elif choice == "3":

            return

        else:

            print(
                "Invalid choice. "
                "Please enter 1, 2, or 3."
            )