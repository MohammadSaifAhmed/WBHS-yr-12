shopping_list = {

    'banana':3.50,
    'carrots':2.00,




}


def add_to_list(item,price):
    shopping_list.update({item:price})


def total_price():

    total = 0
    for i in shopping_list.values():
        total += i
     
    print(total)


def find_item(item):

    if item in shopping_list:
        print(shopping_list[item])

    else:
        print("Item not found")
        add_the_item = input("Do you want to add the item to your list? y or n: ")

        if add_the_item == 'y':
            price = input("What is the price of the item?: ")
            add_to_list(item,price)

        elif add_to_list == 'n':
            pass

        else:
            print("Incorrect input")


while True:

    choice = input("What are you planning to do, add to list(1), total price(2), find item(3) , see list(4), Quit(Q):")


    if choice == "1":        
        item_name = input("What is the name of the item you want to add? :").lower().replace(' ','')
        
        print(item_name)
        price_value = input("What is the price of the item? :")

        add_to_list(item_name,price_value)

    elif choice == '2':
        print("The total price is :" ,total_price())

    elif choice == '3':
        item = input("what item do you want to find? :")

        find_item(item)

    elif  choice == '4':
        print(shopping_list)

    elif choice == 'Q':
        break
    else:
        print("Incorrect input")