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

# products = productOrganizer()

def productSearch(productList):

    searchByName = input("What is the name of the item you're searching for?: ").lower().strip()

    for itemList in products.values():
        for key in itemList.keys():
            if searchByName in itemList['name']:
                result = itemList['name']

    print(result)
# productSearch(products)

# 3. Python Programming Challenges for Customer Service Data Handling
# Objective:
# This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement:
# Develop a program that:

# 1) Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# 2) Implement functions to:
#    A. Open a new service ticket.
#    B. Update the status of an existing ticket.
#    C. Display all tickets or filter by status.
# 3) Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

def ticketTracker():
    user_found = False
    status = "open"
    adminPassword = "TTadmin"
    serviceTickets = {}
    print("Welcome to ticket Tracker!")

    while True:
        admin_or_customer = input("Are you an admin or customer?: (enter 'quit' when finished) ").lower().strip()
        if admin_or_customer == 'quit':
            print("Goodbye")
            break
        if admin_or_customer == 'admin':
            password = input("What is admin password?:" )
            if adminPassword == password:
                while True:
                    try:
                        menu = input("What would you like to do?:\n1) Open new service Ticket?\n2) Update ticket status?\n3) Display all tickets or filter by status?\n4) Quit\n ")
                        menu = int(menu)

                        if menu == 4:
                            print("thank you for choosing Ticket Tracker")
                            break
                        elif menu not in range(1,5):
                            print("Invalid Response: must be a number between 1-4")
                            continue


                        if menu == 1:
                            while True:
                                cxName = input("What is customer name?: enter('done' when finished) ").lower().strip()
                                if cxName == 'done':
                                    break

                                issue = input("very breifely describe problem.. ex) 'Payment Issue': ").lower().strip()
                                
                                ticketNumber = "ticket" + str(len(serviceTickets) + 1)
                                serviceTickets[ticketNumber] ={"Customer": cxName, "issue": issue, "status": status}    
                                print(serviceTickets)

                        if menu == 2:
                            while True:
                                print(serviceTickets)
                                ticketName = input("enter the name of ticket holder: (enter 'done' when finished) ").lower().strip()
                                if ticketName == 'done':
                                    break

                                else:
                                    for ticketNumber, ticketDetails in serviceTickets.items():
                                        if ticketName == ticketDetails['Customer'].lower():
                                            user_found = True
                                            print("user found: ", ticketDetails)
                                            changeStatus = input("Do you want to open or close status?: (enter 'done' when finished) ").lower().strip()
                                            
                                            if changeStatus == 'done':
                                                print(ticketDetails)
                                                break
                                            elif changeStatus == 'open':
                                                serviceTickets[ticketNumber]['status'] = 'open'
                                                print(serviceTickets[ticketNumber])

                                            elif changeStatus == 'close':
                                                serviceTickets[ticketNumber]['status'] = 'closed'
                                                print(serviceTickets[ticketNumber])
                                            else:
                                                print("invalid response")
                                                continue
                                            break
                                        if not user_found:
                                            print("Customer not found")

                        if menu == 3:
                            while True:
                                display_or_filter = input("type 'display' to show all tickets\ntype 'filter' to filter by status: (enter 'done' when finished) ").lower().strip()
                                if display_or_filter == 'done':
                                    break

                                elif display_or_filter == 'display':
                                    print(f"All Tickets: \n{serviceTickets}")

                                elif display_or_filter == 'filter':
                                    closed_or_open = input("type 'open' or 'closed' to filter: (enter 'done' when finished) ").lower().strip()
                                    if closed_or_open == 'done':
                                        break

                                    elif closed_or_open in ['open', 'closed']:
                                        print(f"Filtered Tickets (Status: {closed_or_open}):")
                                        for ticketDetails in serviceTickets.values():
                                                if ticketDetails["status"] == closed_or_open:
                                                    print(ticketDetails)
                                        else:
                                            print("Please enter 'open', 'closed', or 'done' ")


                    except ValueError: 
                        print("Response must be a number 1-4")
                        continue
            else:
                print("invalid password")
                continue

        else:
            pass



ticketTracker()





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