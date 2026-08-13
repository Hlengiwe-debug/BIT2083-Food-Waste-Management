import json
import os
from datetime import datetime, timedelta
from collections import Counter

DATA_FILE = "data/food_inventory.json"
WASTE_FILE = "data/waste_records.json"
USER_FILE = "data/user_preferences.json"

FOOD_CATEGORIES = [
    "Vegetables", "Fruits", "Dairy", "Meat & Poultry",
    "Seafood", "Grains & Cereals", "Canned Goods", "Baked Goods",
    "Beverages", "Snacks", "Condiments", "Other"
]

def initialize_data():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"items": [], "next_id": 1}, f, indent=2)
    if not os.path.exists(WASTE_FILE):
        with open(WASTE_FILE, 'w') as f:
            json.dump([], f, indent=2)
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            json.dump({"total_saved": 0, "meals_donated": 0}, f, indent=2)

def load_inventory():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"items": [], "next_id": 1}

def save_inventory(inventory):
    with open(DATA_FILE, 'w') as f:
        json.dump(inventory, f, indent=2)

def load_waste_records():
    try:
        with open(WASTE_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_waste_records(records):
    with open(WASTE_FILE, 'w') as f:
        json.dump(records, f, indent=2)

def load_user_preferences():
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"total_saved": 0, "meals_donated": 0}

def save_user_preferences(prefs):
    with open(USER_FILE, 'w') as f:
        json.dump(prefs, f, indent=2)

def get_valid_input(prompt, validation_func, error_msg="Invalid input."):
    while True:
        try:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            print(f"[ERROR] {error_msg}")
        except:
            print(f"[ERROR] {error_msg}")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

def validate_quantity(qty_str):
    try:
        return float(qty_str) > 0
    except:
        return False

def validate_positive_number(num_str):
    try:
        return float(num_str) >= 0
    except:
        return False

def add_food_item():
    print("\n" + "=" * 60)
    print("ADD FOOD ITEM TO INVENTORY")
    print("=" * 60)
    name = input("Enter food name: ").strip()
    while not name:
        name = input("[ERROR] Name cannot be empty: ").strip()
    print("\nAvailable Categories:")
    for i, cat in enumerate(FOOD_CATEGORIES, 1):
        print(f"  {i}. {cat}")
    cat_choice = get_valid_input(
        "Select category (1-12): ",
        lambda x: x.isdigit() and 1 <= int(x) <= 12,
        "Enter a number between 1 and 12"
    )
    category = FOOD_CATEGORIES[int(cat_choice) - 1]
    quantity = float(get_valid_input(
        "Enter quantity: ",
        validate_quantity,
        "Enter a positive number"
    ))
    unit = input("Enter unit (kg, g, L, each): ").strip()
    while not unit:
        unit = input("[ERROR] Unit cannot be empty: ").strip()
    expiry_date = get_valid_input(
        "Enter expiry date (YYYY-MM-DD): ",
        validate_date,
        "Use format YYYY-MM-DD"
    )
    cost = float(get_valid_input(
        "Enter cost (RM, 0 if unknown): ",
        validate_positive_number,
        "Enter a valid number"
    ))
    inventory = load_inventory()
    new_item = {
        "id": inventory["next_id"],
        "name": name,
        "category": category,
        "quantity": quantity,
        "unit": unit,
        "expiry_date": expiry_date,
        "purchase_date": datetime.now().strftime("%Y-%m-%d"),
        "cost": cost,
        "status": "active"
    }
    inventory["items"].append(new_item)
    inventory["next_id"] += 1
    save_inventory(inventory)
    print(f"\n[SUCCESS] {name} added! (ID: {new_item['id']})")
    return new_item

def view_inventory():
    inventory = load_inventory()
    items = inventory["items"]
    print("\n" + "=" * 70)
    print("FOOD INVENTORY")
    print("=" * 70)
    if not items:
        print("No items in inventory.")
        return
    active_items = [item for item in items if item["status"] == "active"]
    if not active_items:
        print("No active items in inventory.")
        return
    total_items = 0
    total_value = 0
    today = datetime.now().date()
    for item in active_items:
        expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
        days_left = (expiry - today).days
        status = ""
        if days_left <= 0:
            status = "[EXPIRED]"
        elif days_left <= 3:
            status = "[USE SOON]"
        print(f"\nID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Quantity: {item['quantity']} {item['unit']}")
        print(f"Category: {item['category']}")
        print(f"Expiry: {item['expiry_date']} ({days_left} days left) {status}")
        print(f"Cost: RM{item['cost']:.2f}")
        print("-" * 40)
        total_items += 1
        total_value += item['cost']
    print(f"\nSUMMARY: {total_items} items | Total Value: RM{total_value:.2f}")

def search_inventory():
    print("\n" + "=" * 60)
    print("SEARCH INVENTORY")
    print("=" * 60)
    search_term = input("Enter search term (name or category): ").strip().lower()
    if not search_term:
        print("[ERROR] Search term cannot be empty")
        return
    inventory = load_inventory()
    found_items = []
    for item in inventory["items"]:
        if item["status"] == "active":
            if search_term in item["name"].lower() or search_term in item["category"].lower():
                found_items.append(item)
    if found_items:
        print(f"\n[SUCCESS] Found {len(found_items)} item(s):")
        for item in found_items:
            print(f"  - {item['name']} | {item['category']} | {item['quantity']} {item['unit']}")
    else:
        print(f"[ERROR] No items found matching '{search_term}'")

def remove_food_item():
    print("\n" + "=" * 60)
    print("REMOVE FOOD ITEM")
    print("=" * 60)
    inventory = load_inventory()
    active_items = [item for item in inventory["items"] if item["status"] == "active"]
    if not active_items:
        print("[ERROR] No active items to remove.")
        return
    print("\nActive items:")
    for item in active_items:
        print(f"  ID {item['id']}: {item['name']} ({item['quantity']} {item['unit']})")
    item_id = int(get_valid_input(
        "\nEnter item ID to remove: ",
        lambda x: x.isdigit() and int(x) > 0,
        "Enter a valid ID"
    ))
    item_to_remove = None
    for item in inventory["items"]:
        if item["id"] == item_id and item["status"] == "active":
            item_to_remove = item
            break
    if not item_to_remove:
        print(f"[ERROR] No active item found with ID {item_id}")
        return
    print(f"\nItem: {item_to_remove['name']}")
    print(f"Quantity: {item_to_remove['quantity']} {item_to_remove['unit']}")
    print(f"Expiry: {item_to_remove['expiry_date']}")
    reason = input("Reason (consumed/wasted/donated/expired): ").strip().lower()
    while reason not in ['consumed', 'wasted', 'donated', 'expired']:
        reason = input("[ERROR] Enter: consumed, wasted, donated, or expired: ").strip().lower()
    if reason in ['wasted', 'expired']:
        waste_records = load_waste_records()
        waste_records.append({
            "item_name": item_to_remove['name'],
            "category": item_to_remove['category'],
            "quantity": item_to_remove['quantity'],
            "unit": item_to_remove['unit'],
            "cost": item_to_remove['cost'],
            "reason": reason,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        save_waste_records(waste_records)
        prefs = load_user_preferences()
        prefs["total_saved"] += item_to_remove['cost']
        save_user_preferences(prefs)
        print(f"[INFO] Waste recorded! Cost lost: RM{item_to_remove['cost']:.2f}")
    item_to_remove["status"] = "removed"
    save_inventory(inventory)
    print(f"\n[SUCCESS] {item_to_remove['name']} removed (Reason: {reason})")

def analyze_waste():
    print("\n" + "=" * 70)
    print("FOOD WASTE ANALYSIS REPORT")
    print("=" * 70)
    waste_records = load_waste_records()
    if not waste_records:
        print("[INFO] No waste records found.")
        return
    total_waste_items = len(waste_records)
    total_waste_cost = sum(record['cost'] for record in waste_records)
    total_waste_qty = sum(record['quantity'] for record in waste_records)
    print("\nSUMMARY STATISTICS")
    print("-" * 40)
    print(f"Total Waste Records: {total_waste_items}")
    print(f"Total Financial Loss: RM{total_waste_cost:.2f}")
    print(f"Total Waste Quantity: {total_waste_qty:.1f} units")
    print(f"Potential Meals Wasted: {int(total_waste_qty * 2)}")
    waste_by_category = {}
    waste_by_reason = {}
    for record in waste_records:
        category = record['category']
        reason = record['reason']
        waste_by_category[category] = waste_by_category.get(category, 0) + record['quantity']
        waste_by_reason[reason] = waste_by_reason.get(reason, 0) + record['quantity']
    print("\nWASTE BY CATEGORY")
    print("-" * 40)
    sorted_categories = sorted(waste_by_category.items(), key=lambda x: x[1], reverse=True)
    for category, qty in sorted_categories:
        print(f"{category}: {qty:.1f} units")
    print("\nWASTE BY REASON")
    print("-" * 40)
    for reason, qty in waste_by_reason.items():
        print(f"{reason.capitalize()}: {qty:.1f} units")

def get_waste_forecast():
    print("\n" + "=" * 70)
    print("WASTE FORECAST & PREDICTIONS")
    print("=" * 70)
    inventory = load_inventory()
    waste_records = load_waste_records()
    active_items = [item for item in inventory["items"] if item["status"] == "active"]
    if not active_items:
        print("[INFO] No items in inventory.")
        return
    today = datetime.now().date()
    at_risk_items = []
    for item in active_items:
        expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
        days_left = (expiry - today).days
        if days_left <= 7:
            at_risk_items.append({
                "name": item["name"],
                "days_left": days_left,
                "quantity": item["quantity"],
                "unit": item["unit"]
            })
    if at_risk_items:
        print("\nITEMS AT RISK OF WASTE (7 days or less)")
        print("-" * 50)
        for item in sorted(at_risk_items, key=lambda x: x["days_left"]):
            action = ""
            if item["days_left"] <= 0:
                action = "[EXPIRED] Remove now!"
            elif item["days_left"] <= 3:
                action = "[URGENT] Use immediately"
            elif item["days_left"] <= 5:
                action = "[WARNING] Use within 5 days"
            else:
                action = "[INFO] Plan usage"
            print(f"{item['name']}: {item['days_left']} days left - {action}")
    else:
        print("[INFO] No items at risk of waste.")
    weekly_waste = 0
    one_week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    for record in waste_records:
        if record["date"] >= one_week_ago:
            weekly_waste += record["quantity"]
    if weekly_waste > 0:
        projected_monthly = weekly_waste * 4
        print(f"\n[PROJECTION] Projected monthly waste: {projected_monthly:.1f} units")

def suggest_donations():
    print("\n" + "=" * 70)
    print("DONATION RECOMMENDATION SYSTEM")
    print("=" * 70)
    inventory = load_inventory()
    today = datetime.now().date()
    suggestions = []
    for item in inventory["items"]:
        if item["status"] != "active":
            continue
        expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
        days_left = (expiry - today).days
        if item["quantity"] > 5 or 0 <= days_left <= 5:
            suggestions.append(item)
    if not suggestions:
        print("[INFO] No donation recommendations at this time.")
        return
    print("\nITEMS RECOMMENDED FOR DONATION")
    print("-" * 60)
    for item in suggestions:
        expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
        days_left = (expiry - today).days
        reason = ""
        if days_left <= 3:
            reason = "Expiring soon"
        elif item["quantity"] > 10:
            reason = "Surplus quantity"
        else:
            reason = "Surplus"
        if days_left >= 0:
            print(f"{item['name']} | {item['quantity']} {item['unit']} | Expires: {item['expiry_date']} | {reason}")
    total_donation_qty = sum(item["quantity"] for item in suggestions
                            if datetime.strptime(item["expiry_date"], "%Y-%m-%d").date() >= today)
    potential_meals = int(total_donation_qty * 2)
    print("\n" + "-" * 60)
    print(f"Potential meals from donations: {potential_meals}")
    print(f"Food waste reduction: {total_donation_qty:.1f} units")
    print("\nLOCAL DONATION CENTERS")
    print("-" * 40)
    print("1. Food Bank Malaysia - www.foodbankmalaysia.org")
    print("2. The Lost Food Project - thelostfoodproject.com")
    print("3. Local mosque/food bank - Contact your community center")
    prefs = load_user_preferences()
    prefs["meals_donated"] += potential_meals
    save_user_preferences(prefs)

def calculate_environmental_impact():
    prefs = load_user_preferences()
    print("\n" + "=" * 70)
    print("ENVIRONMENTAL IMPACT CALCULATOR")
    print("=" * 70)
    total_saved = prefs.get("total_saved", 0)
    meals_donated = prefs.get("meals_donated", 0)
    if total_saved == 0 and meals_donated == 0:
        print("[INFO] No data available.")
        return
    co2_saved = total_saved * 0.5
    water_saved = total_saved * 100
    land_saved = total_saved * 0.01
    print("\nYOUR ENVIRONMENTAL IMPACT")
    print("-" * 50)
    print(f"Total Money Saved: RM{total_saved:.2f}")
    print(f"Meals Donated: {meals_donated}")
    print(f"\nENVIRONMENTAL SAVINGS:")
    print(f"   CO2 Reduced: {co2_saved:.2f} kg")
    print(f"   Water Saved: {water_saved:.0f} liters")
    print(f"   Land Preserved: {land_saved:.2f} sq meters")
    print("\nEQUIVALENT TO:")
    print(f"   Driving {co2_saved/2.5:.1f} km less")
    print(f"   Saving {water_saved/50:.0f} showers")
    print(f"   Planting {co2_saved/20:.1f} trees")
    if total_saved > 100:
        print("\nECO-SCORE: EXCELLENT (5/5)")
    elif total_saved > 50:
        print("\nECO-SCORE: GREAT (4/5)")
    elif total_saved > 20:
        print("\nECO-SCORE: GOOD (3/5)")
    elif total_saved > 0:
        print("\nECO-SCORE: FAIR (2/5)")

def show_waste_reduction_tips():
    print("\n" + "=" * 70)
    print("FOOD WASTE REDUCTION TIPS")
    print("=" * 70)
    tips = {
        "Smart Shopping": [
            "Make a shopping list before going to the store",
            "Check what you already have before shopping",
            "Don't shop when hungry - you'll buy more"
        ],
        "Storage": [
            "Store food properly to extend shelf life",
            "Keep fruits and vegetables separate",
            "Freeze items that you won't use soon"
        ],
        "Cooking": [
            "Plan meals around what needs to be used first",
            "Cook appropriate portions",
            "Use leftovers creatively"
        ],
        "Date Management": [
            "Know the difference between 'Best By' and 'Use By'",
            "Label food with purchase dates",
            "Rotate items regularly"
        ],
        "Donation": [
            "Donate surplus to local food banks",
            "Share with neighbors instead of wasting",
            "Use community fridges for sharing"
        ]
    }
    for category, category_tips in tips.items():
        print(f"\n[{category.upper()}]")
        print("-" * 40)
        for tip in category_tips:
            print(f"   - {tip}")
    waste_records = load_waste_records()
    if waste_records:
        categories = [r['category'] for r in waste_records]
        category_counts = Counter(categories)
        if category_counts:
            print(f"\nYOUR PERSONALIZED TIPS")
            print("-" * 40)
            worst_category = category_counts.most_common(1)[0][0]
            print(f"[INFO] You waste most in: {worst_category}")
            print(f"[INFO] Focus on reducing {worst_category} waste")

def display_menu():
    print("\n" + "=" * 60)
    print("FOOD WASTE MANAGEMENT SYSTEM")
    print("SDG 2: Zero Hunger")
    print("=" * 60)
    print("1. Add Food Item")
    print("2. View Inventory")
    print("3. Search Inventory")
    print("4. Remove Food Item")
    print("5. View Waste Analysis")
    print("6. Get Waste Forecast")
    print("7. Get Donation Suggestions")
    print("8. Environmental Impact")
    print("9. Waste Reduction Tips")
    print("10. Exit")
    print("-" * 60)

def main():
    initialize_data()
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ")
        if choice == "1":
            add_food_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            search_inventory()
        elif choice == "4":
            remove_food_item()
        elif choice == "5":
            analyze_waste()
        elif choice == "6":
            get_waste_forecast()
        elif choice == "7":
            suggest_donations()
        elif choice == "8":
            calculate_environmental_impact()
        elif choice == "9":
            show_waste_reduction_tips()
        elif choice == "10":
            print("\nThank you for using Food Waste Management System!")
            print("Remember: Small changes make a big difference!")
            print("Every meal saved helps achieve SDG 2: Zero Hunger!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1-10.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()