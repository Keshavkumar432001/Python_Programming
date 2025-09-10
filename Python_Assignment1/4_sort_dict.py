## Write a Python program to sort a dictionary by value.

def sort_by_value(fruit_price_dict):
    return fruit_price_dict[1]
    

def sort_by_price(price_dict):
    sorted_dic_by_price = sorted(price_dict.items() , key = sort_by_value)
    return sorted_dic_by_price

fruit_price_dict = {'apple' : 60,
                    'banana' : 40,
                    'dragon fruit' : 100,
                    'orange': 50                   
                   }

sorted_price = sort_by_price(fruit_price_dict)

print("Following below are the names and prices per kg of fruits:\n",fruit_price_dict)
print("Fruits after sort by prices:\n",dict(sorted_price))