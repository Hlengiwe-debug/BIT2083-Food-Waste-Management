# ============================================================
# DISTRIBUTION HISTORY MODULE
# ============================================================

import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "food_data.json"


def load_data():
    """Load distribution data."""

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


def distribution_history_page():
    """Display all food distribution records."""

    while True:

        data = load_data()

        records = data[
            "distribution_history"
        ]

        print("\n" + "=" * 75)
        print("                    DISTRIBUTION HISTORY")
        print("=" * 75)

        if not records:

            print(
                "No distribution records found."
            )

        else:

            for record in records:

                print(
                    f"Food ID     : "
                    f"{record['food_id']}"
                )

                print(
                    f"Food Name   : "
                    f"{record['food_name']}"
                )

                print(
                    f"Amount      : "
                    f"{record['amount']}"
                )

                print(
                    f"Destination : "
                    f"{record['destination']}"
                )

                print(
                    f"Date        : "
                    f"{record['date']}"
                )

                print("-" * 75)

        print("1. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            return

        print("Invalid choice.")