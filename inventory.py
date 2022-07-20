#==========import============
from tabulate import tabulate

#create a function (read_data()) that will
#implement a try-except block for reading the following information
#from the file
class Shoe:
    def __init__(self):
        self.stock = []

    def read_data_inventory(self):
        try:
            inventory_file = open ('inventory.txt','r')
            inventory_main_keys = next(inventory_file).strip().split(',')
            for text in inventory_file:
                self.stock .append(dict(zip(inventory_main_keys,text.strip().split(','))))
        
        except FileNotFoundError:
            print('ERROR: THE SPECIFIC FILE IS NOT FOUND!!!')

    '''Write code to determine the product with the lowest quantity, and
        restock it'''
    '''Write code to determine the product with the highest quantity and
        mark it up as being for sale'''
    def reload_stock(self):
        quantity_lowest = None
        stock_lowest = None
        for stock in self.stock:
            if (quantity_lowest == None) or int(stock['Quantity']) < stock_lowest:
                quantity_lowest = int(stock['Quantity']) 
                stock_lowest = stock
        if stock != None:
            stock['Quantity'] = 100

    def sale(self):
        quantity_highest = None
        stock_highest = None 
        for stock in self.stock:
            if quantity_highest == None or int(stock['Quantity']) < quantity_highest:
                quantity_highest = int(stock['Quantity'])
                stock_highest = stock
        if stock != None:
            stock['Cost'] = float(stock['Cost']) * 0,75

    def each_item_value(self):
        for stock in self.stock:
            stock['Value'] = float (stock['Cost']* int(stock['Quantity']))

'''Create at least 5 shoe objects and store these in a list. Add
functionality to search products in the objects list by code'''
def look_for(Shoes, Code):
    find = []
    for inventory in Shoes:
        for stock in inventory.stock:
            if stock['Code'] == Code:
                find.append(inventory)
                break
        
inventory_shoes = []
for data in range(5):
    shoe = Shoe()
    shoe.read_data_inventory()
    shoe.each_item_value()
    inventory_shoes.append(shoe)

#printing the content
print(tabulate(inventory_shoes[0].stock,headers = {'Country': 'Country', 'Country': 'Country', 'Code': 'Code','Product': 'Product', 'Cost': 'Cost', 'Quantity': 'Quantity'}))


