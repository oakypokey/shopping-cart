import os
import csv
import datetime

#Object Definition
class MyItem:
    def __init__(self,serial,name, aisle, department, price):
        self.serial = serial
        self.name = name
        self.aisle = aisle
        self.department = department
        self.price = price


#Set up
itemCode = '' #Init itemCode
itemList = [] #Where the serial numbers of the items that are scanned will be stored
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
    subtotal = 0
    tax = 0
    total = 0

    print("---------------------------------")
    print("GREEN FOODS GROCERY")
    print("WWW.GREEN-FOODS-GROCERY.COM")
    print("---------------------------------")
    print("CHECKOUT AT: " + datetime.datetime.now().strftime("%D %I:%M%p"))
    print("---------------------------------")
    print("SELECTED PRODUCTS: ")
    for item in itemList:
        print("... " + itemDictionary[item].name + " (" + to_usd(float(itemDictionary[item].price)) + ")")
        subtotal += float(itemDictionary[item].price)
        tax += float(itemDictionary[item].price) * NYC_TAXRATE
        total += float(itemDictionary[item].price) + (float(itemDictionary[item].price) * NYC_TAXRATE)
    print("---------------------------------")
    print("SUBTOTAL: " + str(to_usd(subtotal)))
    print("TAX: " + str(to_usd(tax)))
    print("TOTAL: " + str(to_usd(total)))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

while itemCode.upper() != "DONE":
    #Get the item code from the command line
    itemCode = input("Input the serial number for the item, or enter DONE if there are no more items left: ")

    #Don't run any code if DONE is found
    if itemCode.upper() == "DONE":
        #Receipt will be printed
        printReceipt(itemList)
    else:
        
        #Confirm that the item is in the library
        if itemCode in itemDictionary:
            #If it exists, confirm
            print("Item with serial " + itemCode + " was added to the basket")
            itemList.append(itemCode)
        else:
            #If not, tell the user that it does not exist
            print("Item does not exist. Please add to inventory list")