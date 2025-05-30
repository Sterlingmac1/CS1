import random 
items = ["Bigmac","Bacon Mcdouble","Fila-O-Fish","Mcchicken","Egg Mcmuffin","Cheese Burger","Mccrispy" ]
prices = [6, 3, 5, 3, 3, 2, 4]
sauces = ["Honey Mustard","Spicy Buffalo Sauce", "Sweet and sour sauce", "Creamy Ranch", "Hot mustard", "Barbecue sauce", "Ketchup"]

num_of_items = int(input('how many items'))

for i in range(num_of_items):                                                   #for num_of_items times (repetition):
    item = random.choice(items)                                                 #randomly select an item from items
    sauce = random.choice(sauces)
    price = prices[items.index(item)]                                      #randomly select a sauce from sauces
    index = items.index(item)                                               #index of item in items
    print(f"{item} with {sauce} ${price}")
    
