# . Real-World Python Dictionary Applications
# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.
restaurant_menu["Berverages"] = "Water","Lemonade"
# print(restaurant_menu)

# Update the price of "Steak" to 17.99.

restaurant_menu["Main Course"]["Steak"] = 15.99
# print(restaurant_menu)

# Remove "Bruschetta" from "Starters".
del restaurant_menu["Starters"]["Bruschetta"]
# print(restaurant_menu)



# 2. Advanced Data Handling with Python
# Objective:
# The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

# Task 1: Hotel Room Booking Tracker
# Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

# Problem Statement:
# Develop a program that:

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.
# Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def booking():
    print("Welcome to Hotel Kiosk")
    frontKiosk = input("Checking in or out?: ").lower()
    if frontKiosk == 'out':
        hotel_rooms["102"]["customer"] = ""
        hotel_rooms["status"] = "available"
        print(f"here is confirmation that you have vacated the room\n {hotel_rooms['102']}")
        
    if frontKiosk == "in":
        name = input("What is your first and Last name?: ").lower().strip()
        hotel_rooms["101"]["status"] = "booked"
        hotel_rooms["101"]['customer'] = name
        print(f"here is confirmation of your reservation\n room 101: {hotel_rooms['101']}")

    else:
        print("Invalid Response")
        print(f"Here is current hotel status {hotel_rooms}, please try again")
    

# booking()


# Task 2: E-commerce Product Search Feature
# Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

# Problem Statement:
# Create a system that:

# 1)Holds a dictionary of products where each product has attributes like name, category, and price.
 
# 2) Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).

# 3) Handle cases where no matches are found.
# Example product dictionary:



def productOrganizer():
    products = {}
    
    while True:
        itemName = input("item name?: (enter 'done' when finished) ").lower().strip()
        if itemName == 'done':
            print(products)
            break
        itemCategory = input("item Category?: ").lower().strip()
        try:
            itemPrice = int(input("how much is item?: "))
            itemPrice = round(itemPrice)
            if itemPrice < 0:
                raise ValueError("Price can't be lower than zero")                
        except ValueError:
            print("Item price must be integer")
            continue
        itemNumber = len(products)
        products[itemNumber] = {'name': itemName, 'category': itemCategory, 'price': itemPrice}

    return products

# productOrganizer()

products = productOrganizer()

def productSearch(productList):

    searchByName = input("What is the name of the item you're searching for?: ").lower().strip()

    for itemList in products.values():
        for key in itemList.keys():
            if searchByName in itemList['name']:
                result = itemList['name']

    print(result)
productSearch(products)

# 3. Python Programming Challenges for Customer Service Data Handling
# Objective:
# This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement:
# Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }
# 4. Python Essentials for Business Analytics
# Objective:
# This assignment aims to strengthen your proficiency in Python by tackling challenges that simulate real-world business analytics scenarios. You'll practice copying dictionaries, utilizing built-in methods, managing nested collections, and implementing try-except blocks for error handling.

# Task 1: Sales Data Cloning and Modification
# Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

# Problem Statement:
# You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy of this data and update the sales figures for a specific week.

# Given Sales Data:

# weekly_sales = {
#     "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
#     "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
# }
# Create a deep copy of weekly_sales.
# Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.