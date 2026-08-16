# ============================================================
# FOOD DONATION MANAGEMENT SYSTEM
# Main Menu Module
# ============================================================

from donate_food import donate_food_page
from food_inventory import food_inventory_page
from distribute_food import distribute_food_page
from distribution_history import distribution_history_page
from automatic_food_disposal import check_expired_food
from disposal_records import disposal_records_page
from donation_summary import donation_summary_page


def main_menu():
    """Display the main menu and open the selected module."""

    while True:

        # Automatically check for expired food
        check_expired_food()

        print("\n" + "=" * 60)
        print("          FOOD DONATION MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Donate Food")
        print("2. Food Inventory")
        print("3. Distribute Food")
        print("4. Distribution History")
        print("5. Automatic Food Disposal")
        print("6. Disposal Records")
        print("7. Donation Summary")
        print("8. Exit")

        print("=" * 60)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            donate_food_page()

        elif choice == "2":
            food_inventory_page()

        elif choice == "3":
            distribute_food_page()

        elif choice == "4":
            distribution_history_page()

        elif choice == "5":
            check_expired_food(show_message=True)

        elif choice == "6":
            disposal_records_page()

        elif choice == "7":
            donation_summary_page()

        elif choice == "8":
            print("\nThank you for using the system!")
            print("Goodbye.")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main_menu()