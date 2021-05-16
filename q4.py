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
        stock[fruit_name] = fruit_price # adding the fruit name and price as key value pair
        print(stock)
        print('')

    if choice == 2:
        print("Total Value of fruit market is \u20B9{}.".format(sum(stock.values())))
        print('')
    
    if choice == 3:
        print("Thanks for using.")
        break
    
    else:
        print("Wrong Choice")
        print("Please try again")
        print("")