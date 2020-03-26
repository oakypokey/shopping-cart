import os
import csv
import datetime

#Object Definition
class MyItem:
    """
    Item object that stores the information about the item
    
    Params: serial (string),name (string), aisle (string), department (string), price (string)
    """
    def __init__(self,serial,name, aisle, department, price):
        self.serial = serial
        self.name = name
        self.aisle = aisle
        self.department = department
        self.price = price


#Set up
itemCode = '' #Init itemCode
basket = [] #Where the serial numbers of the items that are scanned will be stored
itemDictionary = dict() #Where all the objects from items.csv will be stored
NYC_TAXRATE = 0.0875

#Pulling information from csv file and adding it to the dictionary
##Open the file
pathName = os.getcwd()
file = open(os.path.join(pathName, "items.csv"))
reader = csv.reader(file, delimiter=',')

##Iterate over file, create objects, add to the itemDictionary
for row in reader:
    itemDictionary[row[0]] = MyItem(row[0], row[1], row[2], row[3], row[4])

def printReceipt(arrayOfItems):
    """
    Prints the receipt given a basket of items.
    
    Param: Array of itemCodes
    Example: printReceipt(["1", "2", "3"])
    Returns: NULL
    """

    totals = calculate_total_price(arrayOfItems)
    print("---------------------------------")
    print("GREEN FOODS GROCERY")
    print("WWW.GREEN-FOODS-GROCERY.COM")
    print("---------------------------------")
    print("CHECKOUT AT: " + human_friendly_timestamp(datetime.datetime.now()))
    print("---------------------------------")
    print("SELECTED PRODUCTS: ")

    for item in arrayOfItems: #iterating through and printing all the items
        product = find_product(item)
        print("... " + product.name + " (" + to_usd(float(product.price)) + ")")

    print("---------------------------------")
    print("SUBTOTAL: " + str(to_usd(totals["subtotal"])))
    print("TAX: " + str(to_usd(totals["tax"])))
    print("TOTAL: " + str(to_usd(totals["total"])))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")

def human_friendly_timestamp(datetimeObject):
    return datetimeObject.strftime("%D %I:%M%p")

def calculate_total_price(basket):
    """
    Calculates the subtotals of a shopping basket and returns a dict with the totals
    
    Param: Array of itemCodes
    Example: calculate_total_price(["1", "2", "3"])
    Returns: {
        "subtotal": 100.00,
        "tax": 8.75,
        "total": 108.75 
    }
    """
    subtotal = 0.00
    tax = 0.00
    total = 0.00

    for item in basket: #while iterating through and printing all the items, add all the totals up!
        product = find_product(item)
        subtotal += float(product.price) #convert to float to preserve cents
        tax += float(product.price) * NYC_TAXRATE
        total += float(product.price) + (float(product.price) * NYC_TAXRATE)
    
    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

def find_product(itemCode):
    """
    Finds the product in the dictionary and returns it
   
    Param: itemCode in the form a string.
    Example: find_product("2")
    Returns: MyItem Object
    """

    if itemCode in itemDictionary:
        return itemDictionary[itemCode]
    else:
        raise ValueError()

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

if __name__ == "__main__":
    while itemCode.upper() != "DONE":
        #Get the item code from the command line
        itemCode = input("Input the serial number for the item, or enter DONE if there are no more items left: ")

        #Don't run any code if DONE is found
        if itemCode.upper() == "DONE":
            #Receipt will be printed
            printReceipt(basket)
        else:
            
            #Confirm that the item is in the library
            if itemCode in itemDictionary:
                #If it exists, confirm
                print(itemDictionary[itemCode].name + " was added to the basket")
                basket.append(itemCode) #add to basket
            else:
                #If not, tell the user that it does not exist
                print("Item does not exist. Please add to inventory list")