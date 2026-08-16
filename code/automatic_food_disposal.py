# ============================================================
# AUTOMATIC FOOD DISPOSAL MODULE
# ============================================================

import json
from datetime import date, datetime
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

    except (
        json.JSONDecodeError,
        OSError
    ):

        return {
            "food_items": [],
            "distribution_history": [],
            "disposal_records": []
        }


def save_data(data):
    """Save updated data."""

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


def calculate_priority(expiry_date):
    """Recalculate priority as expiry gets closer."""

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


def check_expired_food(show_message=False):
    """
    Automatically remove expired food
    and place it in disposal records.
    """

    data = load_data()

    today = date.today()

    remaining_food = []

    expired_food = []

    for food in data["food_items"]:

        expiry = datetime.strptime(
            food["expiry_date"],
            "%Y-%m-%d"
        ).date()

        # If expiry date has passed
        if expiry < today:

            disposal_record = {

                "food_id":
                    food["id"],

                "food_name":
                    food["name"],

                "amount":
                    food["amount"],

                "expiry_date":
                    food["expiry_date"],

                "disposal_date":
                    today.isoformat(),

                "reason":
                    "Expired"
            }

            data[
                "disposal_records"
            ].append(
                disposal_record
            )

            expired_food.append(food)

        else:

            # Update priority
            food["priority"] = calculate_priority(
                food["expiry_date"]
            )

            remaining_food.append(food)

    data["food_items"] = remaining_food

    save_data(data)

    # Display information if requested
    if show_message:

        print("\n" + "=" * 60)
        print("              AUTOMATIC FOOD DISPOSAL")
        print("=" * 60)

        if expired_food:

            print(
                "The following food has expired "
                "and was automatically disposed:"
            )

            print()

            for food in expired_food:

                print(
                    f"{food['id']} - "
                    f"{food['name']} | "
                    f"Amount: {food['amount']} | "
                    f"Expired: {food['expiry_date']}"
                )

        else:

            print(
                "No expired food was found."
            )

        print("=" * 60)

        input(
            "\nPress Enter to return..."
        )

    return expired_food