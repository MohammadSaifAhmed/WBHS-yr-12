from easygui import *


shopping_list = {

    'banana':{"price": 3.00, "quantities": 4},
    'carrots':{"price": 2.00, "quantities": 1},




}


def add_to_list(item,price,quantities):
    
    shopping_list.update({item:{"price":price,"quantities":quantities}})

    print(shopping_list)

def total_price():

    total = 0
    for i in shopping_list.values():
       
       total += i["price"] * i["quantities"]
    
    return total
    


def find_item(item):

    if item in shopping_list:
        msgbox(str(shopping_list[item]).replace("{","").replace("}", ""))

    else:
        msgbox("Item not found")
        add_the_item = buttonbox("Do you want to add the item to your list?: ",choices = ["yes","no"])
        print(add_the_item)
        if add_the_item == 'yes':
            price = integerbox("What is the price of the item?: ")
            quantity = integerbox("What is the quantity of the item?: ")
            add_to_list(item,price,quantity)

        elif add_to_list == 'no':
            pass
                                          
        else:
            msgbox("Incorrect input")




title = "GfG-EasyGUI"
 

msg = "GeeksforGeeks, Hello World from EasyGUI"
 

button_list = ["add to list","remove from list" ,"total price", "find item", "see list", "Quit"]
 
list_keys = []
for key in shopping_list.keys():
    list_keys.append(key)

while True:

    choice = buttonbox(msg,title,button_list)
    if choice == "add to list":  
        text = "What is the name of the item you want to add? :"   
        item_name = enterbox(text, title).lower().replace(' ','') 
           
        print(item_name)
        price_value = integerbox("What is the price of the item? :")
        quantity_of_product = integerbox("What is the quantity of the item? :")

        add_to_list(item_name,price_value,quantity_of_product)

    elif choice == 'total price':
        msgbox(f"The total price is : {total_price()}" )

    elif choice == 'find item':
        item = buttonbox("what item do you want to find? :", choices=list_keys)

        find_item(item)

    elif  choice == 'see list':
    
        message = ""
        for i in shopping_list:


            message += f"{i} : price: ${shopping_list[i]['price']} x {shopping_list[i]['quantities']} = ${shopping_list[i]['price'] * shopping_list[i]['quantities']} \n"
            
            
        msgbox(message)    

    elif choice == 'remove from list':
        
        item = buttonbox("What is the item you want to remove? : ", choices= list_keys)
        shopping_list.pop(item)
    elif choice == 'Quit':
        break
    else:
        enterbox("Incorrect input")


