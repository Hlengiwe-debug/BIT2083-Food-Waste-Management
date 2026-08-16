# ============================================================
# DONATION SUMMARY MODULE
# ============================================================

import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "food_data.json"


def load_data():
    """Load all system data."""

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


def donation_summary_page():
    """Calculate and display the donation summary."""

    while True:

        data = load_data()

        food_items = data[
            "food_items"
        ]

        distribution_history = data[
            "distribution_history"
        ]

        disposal_records = data[
            "disposal_records"
        ]

        # Calculate available food
        available = sum(
            food["amount"]
            for food in food_items
        )

        # Calculate distributed food
        distributed = sum(
            record["amount"]
            for record
            in distribution_history
        )

        # Calculate disposed food
        disposed = sum(
            record["amount"]
            for record
            in disposal_records
        )

        # Total donated consists of all food
        # currently available, distributed,
        # or disposed.
        total_donated = (
            available
            + distributed
            + disposed
        )

        print("\n" + "=" * 60)
        print("                 DONATION SUMMARY")
        print("=" * 60)

        print(
            f"Total Food Donated     : "
            f"{total_donated}"
        )

        print(
            f"Currently Available    : "
            f"{available}"
        )

        print(
            f"Total Food Distributed : "
            f"{distributed}"
        )

        print(
            f"Total Food Disposed    : "
            f"{disposed}"
        )

        print(
            f"Distribution Records   : "
            f"{len(distribution_history)}"
        )

        print(
            f"Disposal Records       : "
            f"{len(disposal_records)}"
        )

        print("=" * 60)

        print("1. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            return

        print("Invalid choice.")