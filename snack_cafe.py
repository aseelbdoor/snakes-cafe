def intro():
    print('''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************''')

def menue():
    print('''
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************''')
          
def end():
    print("Thank you sir/miss for choosing our restaurant. We will start preparing the order. Hope you enjoy the service")

def order():
    minue=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado",
           "A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
    customer_order=input("> ")
    order_list={}
    customer_order=customer_order.strip().capitalize()
    while customer_order!="Quit":
        if customer_order not in minue and customer_order not in order_list:
            print('We do not have this item yet! but we will make a little exception for you ')
            order_list[customer_order]=1
            print(f"**{order_list[customer_order]} order of {customer_order} has been added to your meal **")
        elif customer_order in order_list:
            order_list[customer_order]=order_list[customer_order]+1
            print(f"**{order_list[customer_order]} order of {customer_order} has been added to your meal **")
        else:
            order_list[customer_order]=1
            print(f"**{order_list[customer_order]} order of {customer_order} has been added to your meal **")
        customer_order=input("> ")
        customer_order=customer_order.strip().capitalize()
    else:
        if len(order_list)>0:
            print("This is your order: ")
            for i in order_list:
                print(f"  {i}\t{order_list[i]}")
            end()
        else:
            print("We are very sorry if the reason for changing your mind about ordering from our restaurant is from our side")
        
        
#main
intro()
menue()
order()