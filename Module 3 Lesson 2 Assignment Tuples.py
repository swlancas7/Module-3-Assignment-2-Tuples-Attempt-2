# Task 1: Formatting Flight Itineraries

def display_itineraries(itineraries):
    for itinerary in itineraries:
        traveler, flights = itinerary[0], itinerary[1:]
        for flight in flights:
            print(f" Flight: {flight[0]}, from: {flight[1]}, To: {flight[2]}")

def find_itinerary_by_traveler(itineraries, traveler_name):
    for itinerary in itineraries:
        if itinerary[0].lower() == traveler_name.lower():
            print(f"\nItinerary for {traveler_name}:")
            for flight in itinerary[1:]:
                print(f" Flight: {flight[0]}, from: {flight[1]}, To: {flight[2]}")
            break
        else:
            print("No itinerary found for this traveler.")

def list_itineraries_from_city(itineraries, city):
    print(f"\nItineraries from {city}:")
    for itinerary in itineraries:
        for flight in itineary[1:]:
            if flight[1].lower() == city.lower():
                print(f"Traveler: {itineary[0]}, Flight: {flight[0]}, To: {flight[2]}")

def main():
    itineraries = [
        ("Alice", ("FL123", "New York", "London"), ("FL456", "London", "Paris")),
           ("Bob", ("FL789", "Tokyo", "San Francisco"), ("FL321", "San Francisco", "New York")),
    ]

    while True:
        print("\n1. View all itineraries")
        print("2. Search itinerary by traveler")
        print("3. List itineraries from a city")
        print("4. Exit")
        choice = input("Enter your choice:  ")

        if choice == '1':
            display_itineraries(itineraries)
        elif choice == '2':
            traveler = input("Enter traveler's name: ")
            find_itinerary_by_traveler(itineraries, traveler)
        elif choice == '3':
            city = input("Enter city's name:  ")
            list_itineraries_from_city(itineraries, city)
        elif choice == '4':
            exit
            print("Exiting program.")
        else: 
            print("Invalid number. Enter 1, 2, 3 or 4.")

# Task 2: Library System Enhancement

def add_book(catalog):
    try:
        title = input("Enter book title: ")
        author = input("Enter book's author: ")
        catalog.append((title, author))
    except ValueError:
        print("Invalid input.")

catalog = [add_book]

unique_list = list(set(catalog))
print(unique_list)

def display_catalog(catalog):
    for book in catalog:
        print(f"Title: {book[0]}, Author: {book[1]}")

def search_category(catalog):
    title = input ("Enter title to search: ")
    found = [book for book in catalog if book[0].lower() == title.lower()]
    if found:
        for book in found:
            print("Title: {book[0]}, Author: {book[1]}")

    

def main():
    catalog = []
    while True:
        print("\n1. Add a book.")
        print("2. View catalog.")
        print("3. Search by title.")
        print("4. Exit.")
        choice = input("Enter your choice:  ")

        if choice == '1':
            add_book(catalog)
        elif choice == '2':
            display_catalog(catalog)
        elif choice == '3':
            search_title(catalog)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

# Task 3:  Mastering Tuple Packing & Unpacking In Python

orders = {'Customer name': (1), 'Product name': (2), 'Number of products': (3)}


for element in orders: 
    if isinstance(element, dict):
        for item in element.item():
            print: (f"{key}: {value}")
    else:
        print(element)

Customer_name, Product_name, *rest = orders

print(Customer_name)
print(Product_name)
print(rest)


     





