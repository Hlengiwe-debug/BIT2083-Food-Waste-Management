# Food Donation Management System

food donation management system is designed to manage donated food, monitor food inventory, distribute food to organizations in need, and automatically dispose of expired food. The system uses a simple menu-driven console interface

---

## Project Overview

Food waste is a major problem, while many communities and organizations still require access to food. This project provides a simple system that helps manage donated food from the moment it is received until it is distributed or disposed of.

The system allows users to:

- Donate and record food
- Store donated food in an inventory
- Automatically assign food priority based on expiry dates
- View available food
- Distribute food to organizations
- Record distribution history
- Automatically detect expired food
- Record disposed food
- View a complete donation summary

---

# ✨ Features

## 1. Main Menu

The Main Menu provides access to all functions of the system.

```text
============================================================
          FOOD DONATION MANAGEMENT SYSTEM
============================================================
1. Donate Food
2. Food Inventory
3. Distribute Food
4. Distribution History
5. Automatic Food Disposal
6. Disposal Records
7. Donation Summary
8. Exit
============================================================
```

Each option opens its corresponding module.

Every module also provides an option to return to the Main Menu.

---

## 2. Donate Food

The Donate Food module allows users to record newly donated food.

The user enters:

- Food name
- Amount
- Expiry date

The system automatically generates:

- Food ID
- Priority level

Example:

```text
Food ID      : F001
Food Name    : Rice
Amount       : 50
Expiry Date  : 2026-09-10
Priority     : 4/10
```

### Donation Options

The module provides:

```text
1. Donate Food
2. Add Another Food
3. Back to Main Menu
```

This allows users to enter multiple food items without restarting the program.

---

# 3. 📦 Food Inventory

The Food Inventory module displays all food currently available in the system.

The inventory contains:

| Information | Description |
|---|---|
| Food ID | Unique ID assigned to the food |
| Food Name | Name of the donated food |
| Amount | Current available quantity |
| Expiry Date | Date the food expires |
| Priority | Urgency level from 1–10 |

Food is sorted according to its priority.

Food with a higher priority is closer to its expiry date and should be distributed first.

Example:

```text
===========================================================================
                       FOOD INVENTORY
===========================================================================

ID      FOOD                AMOUNT    EXPIRY DATE     PRIORITY
---------------------------------------------------------------------------
F001    Bread               20        2026-08-20      9/10
F002    Rice                50        2026-12-20      2/10
F003    Canned Beans        30        2026-11-15      4/10

===========================================================================
```

---

# 4. Distribute Food

The Distribute Food module allows available food to be distributed to organizations that need it.

The system includes three example destinations:

### Orphanage

Food can be distributed to an orphanage to support children in need.

### Homeless Shelter

Food can be distributed to a homeless shelter to support people experiencing homelessness.

### Community Food Bank

Food can be distributed to a community food bank for further distribution to people in the local community.

The menu is:

```text
1. Orphanage
2. Homeless Shelter
3. Community Food Bank
4. Back to Main Menu
```

The system checks the available quantity before allowing the distribution.

For example:

```text
Original Amount: 50
Distributed:     20
Remaining:       30
```

The distribution is then automatically recorded in the Distribution History.

---

# 5. Distribution History

The Distribution History module records every successful food distribution.

Each record contains:

- Food ID
- Food name
- Amount distributed
- Destination
- Distribution date

Example:

```text
Food ID     : F001
Food Name   : Rice
Amount      : 20
Destination : Orphanage
Date        : 2026-08-18
```

This provides a record of where donated food has been distributed.

---

# 6. Automatic Food Disposal

The Automatic Food Disposal module checks whether food has passed its expiry date.

The system automatically checks for expired food when appropriate.

When expired food is detected:

```text
Expired Food
     ↓
Removed from Inventory
     ↓
Added to Disposal Records
```

For example:

```text
Food Name   : Milk
Amount      : 10
Expiry Date : 2026-08-15

Current Date: 2026-08-18

Result:
Food is automatically disposed.
```

This prevents expired food from remaining in the active inventory and being distributed.

---

# 7. Disposal Records

The Disposal Records module stores information about food that has been automatically removed because it expired.

Each disposal record contains:

- Food ID
- Food name
- Amount
- Expiry date
- Disposal date
- Reason for disposal

Example:

```text
Food ID       : F005
Food Name     : Milk
Amount        : 10
Expiry Date   : 2026-08-15
Disposal Date : 2026-08-18
Reason        : Expired
```

This allows the user to keep track of food waste generated by expired donations.

---

# 8. Donation Summary

The Donation Summary module provides an overview of the system.

It calculates:

```text
Total Food Donated
Currently Available
Total Food Distributed
Total Food Disposed
Distribution Records
Disposal Records
```

Example:

```text
============================================================
                 DONATION SUMMARY
============================================================

Total Food Donated     : 150
Currently Available    : 70
Total Food Distributed : 60
Total Food Disposed    : 20
Distribution Records   : 8
Disposal Records       : 3

============================================================
```

---

# Food Priority System

The system automatically calculates a priority from **1 to 10** based on how close the food is to its expiry date.

A higher number means the food should be distributed sooner.

| Days Until Expiry | Priority |
|---:|---:|
| 2 days or less | 10/10 |
| 3–5 days | 9/10 |
| 6–10 days | 8/10 |
| 11–20 days | 6/10 |
| 21–30 days | 4/10 |
| More than 30 days | 2/10 |

### Example

If food expires in two days:

```text
Priority: 10/10
```

If food expires several months later:

```text
Priority: 2/10
```

This allows the system to prioritize food that needs to be distributed first.

---

# Project Structure

The project is divided into **8 Python modules**.

```text
Food Donation Management System/
│
├── main.py
├── donate_food.py
├── food_inventory.py
├── distribute_food.py
├── distribution_history.py
├── automatic_food_disposal.py
├── disposal_records.py
├── donation_summary.py
├── food_data.json
└── README.md
```

---

# Module Description

## `main.py`

Controls the Main Menu and connects all eight modules.

## `donate_food.py`

Handles:

- Food donation
- Food name input
- Amount input
- Expiry date input
- Food ID generation
- Priority calculation
- Input validation

## `food_inventory.py`

Handles:

- Displaying available food
- Sorting food according to priority
- Showing food quantities
- Showing expiry dates

## `distribute_food.py`

Handles:

- Selecting a destination
- Selecting food
- Entering distribution quantity
- Checking available quantity
- Updating inventory
- Recording distributions

## `distribution_history.py`

Handles:

- Viewing previous distributions
- Displaying food distribution details
- Displaying destinations
- Displaying distribution dates

## `automatic_food_disposal.py`

Handles:

- Checking expiry dates
- Detecting expired food
- Removing expired food
- Creating disposal records
- Updating food priority

## `disposal_records.py`

Handles:

- Viewing disposed food
- Displaying disposal information
- Showing disposal dates
- Showing disposal reasons

## `donation_summary.py`

Handles:

- Total donated food
- Available food
- Distributed food
- Disposed food
- Number of distribution records
- Number of disposal records

---

# Data Storage

The system uses a JSON file for data storage.

```text
food_data.json
```

The file contains three main sections:

```json
{
    "food_items": [],
    "distribution_history": [],
    "disposal_records": []
}
```

### `food_items`

Stores food that is currently available.

### `distribution_history`

Stores records of food that has been distributed.

### `disposal_records`

Stores records of food that has been disposed of.

The JSON file allows the system to keep its records even after the program is closed.

---

# Input Validation

The system includes basic error handling and validation.

### Invalid Amount

```text
Amount: abc

Invalid input. Please enter a whole number.
```

### Negative Amount

```text
Amount: -5

Amount must be greater than 0.
```

### Invalid Date

```text
Expiry Date: 18/08/2026

Invalid date format.
Please use YYYY-MM-DD.
```

### Invalid Menu Option

```text
Enter your choice: 20

Invalid choice.
Please try again.
```

### Insufficient Food

If only 10 units are available and the user attempts to distribute 20:

```text
Amount cannot be greater than available food.
```

These validations help prevent incorrect data from being stored in the system.

---

# 🔄 System Workflow

The general system workflow is:

```text
                    MAIN MENU
        |               │                │
   DONATE FOOD     INVENTORY       DISTRIBUTE FOOD
        │               │                │
                                       
   Store Food      View Food       Select Destination
        │                                │
                                        
 Calculate Priority                Update Inventory
        │                                │
        
                         |
                DISTRIBUTION HISTORY

                         │
                         
                 EXPIRY DATE CHECK
                         │
                    
                    │         │
                  EXPIRED   NOT EXPIRED
                    │          |
             DISPOSAL      INVENTORY
              RECORD
```

---
# Run the program:
---

# 🧪 Example Usage

## Step 1 — Donate Food

Select:

```text
1. Donate Food
```

Enter:

```text
Food Name: Bread
Amount: 20
Expiry Date: 2026-08-25
```

The system automatically generates a Food ID and priority.

---

## Step 2 — Check Inventory

Select:

```text
2. Food Inventory
```

The donated bread will appear in the inventory.

---

## Step 3 — Distribute Food

Select:

```text
3. Distribute Food
```

Choose:

```text
1. Orphanage
```

Select the food and enter the amount.

The inventory will automatically be updated.

---

## Step 4 — Check Distribution History

Select:

```text
4. Distribution History
```

The previous distribution will be displayed.

---

## Step 5 — Check Expired Food

Select:

```text
5. Automatic Food Disposal
```

The system checks whether any food has expired.

Expired food is automatically removed from the inventory and added to the disposal records.

---

## Step 6 — View Disposal Records

Select:

```text
6. Disposal Records
```

The system displays all food that has been disposed of.

---

## Step 7 — View Summary

Select:

```text
7. Donation Summary
```

The system displays the overall food donation statistics.

---

# 🔐 Data Storage

The project uses a local JSON file for storage.

The system does not require:

- Internet access
- An external database
- An online account
- External APIs

All data is stored locally in:

```text
food_data.json
```

# 🎯 Project Objectives

The main objectives of this project are to:

1. Create a simple system for recording donated food.
2. Maintain an organized food inventory.
3. Prioritize food based on expiry dates.
4. Support food distribution to organizations in need.
5. Maintain records of food distributions.
6. Automatically detect and dispose of expired food.
7. Maintain disposal records.
8. Provide a summary of the system's food activity.

---