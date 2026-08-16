# ============================================================
# FOOD INVENTORY MODULE
# ============================================================

import json
from pathlib import Path

from automatic_food_disposal import check_expired_food


DATA_FILE = Path(__file__).parent / "food_data.json"


def load_data():
    """Load food data."""

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


def food_inventory_page():
    """Display the current available food."""

    while True:

        # Remove expired food before showing inventory
        check_expired_food()

        data = load_data()

        food_items = data["food_items"]

        print("\n" + "=" * 75)
        print("                       FOOD INVENTORY")
        print("=" * 75)

        if not food_items:

            print(
                "There is currently no food "
                "available."
            )

        else:

            # Sort highest priority first
            food_items.sort(
                key=lambda food: food["priority"],
                reverse=True
            )

            print(
                f"{'ID':<8}"
                f"{'FOOD':<20}"
                f"{'AMOUNT':<10}"
                f"{'EXPIRY DATE':<16}"
                f"{'PRIORITY':<10}"
            )

            print("-" * 75)

            for food in food_items:

                print(
                    f"{food['id']:<8}"
                    f"{food['name'][:18]:<20}"
                    f"{food['amount']:<10}"
                    f"{food['expiry_date']:<16}"
                    f"{food['priority']}/10"
                )

        print("=" * 75)

        print("1. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            return

        print("Invalid choice.")