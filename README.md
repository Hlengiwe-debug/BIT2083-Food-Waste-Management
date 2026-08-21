# BIT2083-Food-Waste-Management
Food Waste Management System for SDG 2 - Zero Hunger
# Food Waste Management System
## SDG 2: Zero Hunger

### Team Members
| No | Name | Student ID | Role |
|----|------|------------|------|
| 1 | Hlengiwe Ntunja | 202506010017| Project Leader |
| 2 | Sut Ring Naw| 202405010373 | Inventory Specialist |
| 3 | EI Phyu Phyu Phway | 202505010374 | Data Analyst |
| 4 | Mobarak Mohamad  | 202310010109 | Education Coordinator |
| 5 | Mehran Tasawar | 202505010519 | Reporting Expert |

# Food Donation Management System

## 📌 Project Overview

The Food Donation Management System is a Python-based console application developed to help manage donated food and reduce food waste.

The system allows users to record food donations, manage food inventory, distribute available food, identify expired food, and generate donation summaries.

This project is developed in support of **Sustainable Development Goal 2 (SDG 2): Zero Hunger** by promoting better management and redistribution of donated food.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Manage donated food efficiently.
- Record food name, amount, and expiry date.
- Validate the amount entered by the user.
- Validate food expiry dates.
- Calculate food priority based on expiry information.
- Manage available food inventory.
- Distribute donated food efficiently.
- Automatically identify and dispose of expired food.
- Maintain distribution and disposal records.
- Generate a summary of donation activities.

---

## 🌱 Sustainable Development Goal

### SDG 2 – Zero Hunger

This project supports **SDG 2: Zero Hunger** by providing a simple system for managing and redistributing donated food.

The system helps reduce unnecessary food waste by:

- Keeping track of donated food.
- Prioritizing food based on expiry dates.
- Supporting organized food distribution.
- Removing expired food from the available inventory.

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Application Type:** Console-based application
- **Data Storage:** JSON
- **Development Environment:** Python IDE / VS Code
- **Version Control:** GitHub

---

## ⚙️ Main Features

### 1. Donate Food

Users can add a new food donation by entering:

- Food name
- Amount
- Expiry date

The system validates the entered information before accepting the donation.

### 2. Food Priority Calculation

The system calculates a priority level for donated food based on its expiry information.

Food that is closer to expiry can receive a higher priority so that it can be considered for earlier distribution.

### 3. Amount Validation

The system checks whether the entered food amount is valid.

Invalid values are rejected and the user is asked to enter a valid amount.

### 4. Expiry Date Validation

The system checks whether the expiry date:

- Uses the required `YYYY-MM-DD` format.
- Has not already passed.

Expired or incorrectly formatted dates are rejected.

### 5. Food Inventory

The system stores and displays information about available donated food.

The inventory can contain information such as:

- Food ID
- Food name
- Amount
- Expiry date
- Priority

### 6. Food Distribution

Users can distribute available donated food.

After distribution, the remaining food amount is updated in the inventory.

### 7. Automatic Food Disposal

The system identifies food that has already expired and removes it from the available food inventory.

This helps prevent expired food from being distributed.

### 8. Distribution History

The system keeps track of food distribution activities so that previous distribution records can be reviewed.

### 9. Disposal Records

The system maintains records of food that has been removed through the disposal process.

### 10. Donation Summary

The system provides a summary of recorded food donation activities, allowing users to review the overall status of the system.

---

## 🧠 Computational Thinking

The project applies four major computational thinking concepts:

### Decomposition

The large food management problem is divided into smaller functions such as food donation, inventory management, distribution, disposal, and summary generation.

### Pattern Recognition

The system identifies the relationship between food expiry dates and distribution priority. Food approaching its expiry date can be prioritized for earlier distribution.

### Abstraction

The system focuses on important food information such as food name, amount, expiry date, and priority while hiding internal processing and data storage details from the user.

### Algorithmic Thinking

The system uses step-by-step procedures for operations such as food donation, amount validation, expiry-date validation, priority calculation, distribution, and disposal.

---

## 📋 Main Menu

When the program is started, the following main menu is displayed:

```text
1. Donate Food
2. Food Inventory
3. Distribute Food
4. Distribution History
5. Automatic Food Disposal
6. Disposal Records
7. Donation Summary
8. Exit
