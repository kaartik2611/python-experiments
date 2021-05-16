#  Write a program in python to accept the stock (in kg) and price (of per kg in rupees) 
#  of fruits available in fruit market using dictionary and then calculate the total value (in 
#  rupees) of fruit market
stock ={}
while True:
    print("1.Add fruit Stock Data.")
    print('2.Display Total Value of fruit market.')
    print("3.Exit the Program.")
    try: # adding exceptions if number is not string
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Try entering a valid number")
        break
    
    if choice == 1:
        fruit_name = input("Enter name of available fruit: ")
        fruit_price = int(input("Enter Price of Fruit: "))
        fruit_quantity = int(input("Enter Fruit Quantity in kg: "))
        stock[fruit_name] = {}
        stock[fruit_name]['Price'] =  fruit_price
        stock[fruit_name]['Quantity'] = fruit_quantity
        print("Data added succesfully")
        print('')      

    elif choice == 2:
        c=0
        for i in stock.values():
            c+=i['Price']*i['Quantity']
        print("Total Value of fruit market is \u20B9{}.".format(c))
        print('')
    
    elif choice == 3:
        print("Thanks for using.")
        
    else:
        print("Wrong Choice")
        print("Please try again")
        print("")
        
        
