# ============================================================
# DISTRIBUTE FOOD MODULE
# ============================================================

import json
from datetime import date
from pathlib import Path

from automatic_food_disposal import check_expired_food


DATA_FILE = Path(__file__).parent / "food_data.json"


def load_data():
    """Load data from JSON."""

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return {
            "food_items": [],
            "distribution_history": [],
            "disposal_records": []
        }


def save_data(data):
    """Save data to JSON."""

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


def get_positive_amount(maximum):
    """Get a valid distribution amount."""

    while True:

        try:

            amount = int(
                input(
                    f"Amount to distribute "
                    f"(maximum {maximum}): "
                ).strip()
            )

            if amount <= 0:

                print(
                    "Amount must be greater than 0."
                )

            elif amount > maximum:

                print(
                    "Amount cannot be greater "
                    "than available food."
                )

            else:

                return amount

        except ValueError:

            print(
                "Please enter a whole number."
            )


def distribute_to_destination(destination):
    """Distribute food to a selected organization."""

    while True:

        check_expired_food()

        data = load_data()

        food_items = data["food_items"]

        print("\n" + "=" * 75)

        print(
            f"             DISTRIBUTE TO "
            f"{destination.upper()}"
        )

        print("=" * 75)

        if not food_items:

            print(
                "No food is available."
            )

            input(
                "\nPress Enter to return..."
            )

            return

        # Show urgent food first
        food_items.sort(
            key=lambda food: food["priority"],
            reverse=True
        )

        for food in food_items:

            print(
                f"{food['id']} - "
                f"{food['name']} | "
                f"Amount: {food['amount']} | "
                f"Expiry: {food['expiry_date']} | "
                f"Priority: {food['priority']}/10"
            )

        print("\n0. Back")

        food_id = input(
            "\nEnter Food ID: "
        ).strip().upper()

        if food_id == "0":

            return

        selected_food = None

        for food in food_items:

            if food["id"] == food_id:

                selected_food = food
                break

        if selected_food is None:

            print(
                "Food ID not found."
            )

            continue

        amount = get_positive_amount(
            selected_food["amount"]
        )

        print("\n" + "-" * 55)

        print(
            f"Food        : "
            f"{selected_food['name']}"
        )

        print(
            f"Amount      : "
            f"{amount}"
        )

        print(
            f"Destination : "
            f"{destination}"
        )

        print("-" * 55)

        confirmation = input(
            "Confirm distribution? (Y/N): "
        ).strip().lower()

        if confirmation != "y":

            print(
                "Distribution cancelled."
            )

            continue

        # Reduce the inventory amount
        selected_food["amount"] -= amount

        # Save the distribution
        distribution_record = {

            "food_id":
                selected_food["id"],

            "food_name":
                selected_food["name"],

            "amount":
                amount,

            "destination":
                destination,

            "date":
                date.today().isoformat()
        }

        data[
            "distribution_history"
        ].append(
            distribution_record
        )

        # Remove food when all of it is distributed
        if selected_food["amount"] == 0:

            data["food_items"].remove(
                selected_food
            )

        save_data(data)

        print("\n" + "=" * 55)
        print("           DISTRIBUTION SUCCESSFUL")
        print("=" * 55)

        print(
            f"Food        : "
            f"{selected_food['name']}"
        )

        print(
            f"Amount      : "
            f"{amount}"
        )

        print(
            f"Destination : "
            f"{destination}"
        )

        print(
            f"Remaining   : "
            f"{selected_food['amount']}"
        )

        print("=" * 55)

        input(
            "\nPress Enter to continue..."
        )

        return


def distribute_food_page():
    """Display the distribution menu."""

    destinations = {

        "1": "Orphanage",

        "2": "Homeless Shelter",

        "3": "Community Food Bank"
    }

    while True:

        print("\n" + "=" * 60)
        print("                 DISTRIBUTE FOOD")
        print("=" * 60)

        print("1. Orphanage")
        print("2. Homeless Shelter")
        print("3. Community Food Bank")
        print("4. Back to Main Menu")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "4":

            return

        elif choice in destinations:

            distribute_to_destination(
                destinations[choice]
            )

        else:

            print(
                "Invalid choice."
            )