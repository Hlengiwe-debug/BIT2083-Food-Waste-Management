# ============================================================
# DISPOSAL RECORDS MODULE
# ============================================================

import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "food_data.json"


def load_data():
    """Load disposal records."""

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


def disposal_records_page():
    """Display all food that has been disposed."""

    while True:

        data = load_data()

        records = data[
            "disposal_records"
        ]

        print("\n" + "=" * 75)
        print("                      DISPOSAL RECORDS")
        print("=" * 75)

        if not records:

            print(
                "No food has been disposed of."
            )

        else:

            for record in records:

                print(
                    f"Food ID       : "
                    f"{record['food_id']}"
                )

                print(
                    f"Food Name     : "
                    f"{record['food_name']}"
                )

                print(
                    f"Amount        : "
                    f"{record['amount']}"
                )

                print(
                    f"Expiry Date   : "
                    f"{record['expiry_date']}"
                )

                print(
                    f"Disposal Date : "
                    f"{record['disposal_date']}"
                )

                print(
                    f"Reason        : "
                    f"{record['reason']}"
                )

                print("-" * 75)

        print("1. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            return

        print("Invalid choice.")