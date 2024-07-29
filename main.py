from operation import welcome_message
from operation import options_message
from operation import sell_option_message
from operation import error
from functions import laptop_dic
from purchase import add_to_stock_billing
from functions import display_stock
from sell import sell_to_customer
from sell import sell_to_customer_with_shipping
from datetime import datetime
# Defining consants
current_time =  datetime.now()
stock_dic,sn = laptop_dic()
valid_id = stock_dic.keys()
next_sn = sn + 1
psn = 1
ssn = 1
purchase_dic = {}
sell_dic = {}
welcome_message()
# USING CONTINOUS LOOP 
continue_loop = True
while continue_loop == True:
    options_message()

    loop = True
    while loop == True:
        try:
            user_input = int(input("Please Type and hit enter to select option:  "))
            loop=False
        except:
            print("Enter an intger value from the list.")
    # USING IF CONDTION FOR PURCHASE OF LAPTOPS
    if user_input == 1:
        print("For billing purpose you have to submit your name")
        user_name = input("Enter your name : ")
        user_phone = input("Enter your number : ")
        # purchase_loop = True
        while True:
            while True:
                try:
                    user_id = int(input(" Enter product's ID: "))
                    break
                except:
                    print("Enter an Integer value from the list")

            if user_id in valid_id:
                while True:
                    try:
                        get_quantity = int(input("Enter the quantity you want to order: "))
                        break
                    except:
                        print("Enter appropriate value!!!")
                while get_quantity < 1:
                    print("Quantity cannot be zero or negative! \n\n")
                    get_quantity = int(input("Enter the quantity you want to order: "))
                stock_dic[user_id][3] = int(stock_dic[user_id][3]) + int(get_quantity)
                    
                name = stock_dic[user_id][0]
                brand = stock_dic[user_id][1]
                price = int(stock_dic[user_id][2].replace('$','').strip())
                # ADDING THE DETAILS IN TEMPORARY DICTIONARY TO PRINT THE INVOICE
                purchase_dic.update({psn:[name,brand,price, get_quantity]})
                # INCREAMENT OF SN FOR BILL
                psn += 1 
                #  UPDATING THE STOCK IN TXT FILE
                file = open("Stock.txt","w")
                for key,values in stock_dic.items():
                    file.write(str(values[0]).center(18)+","+str(values[1]).center(15)+","+str(values[2]).center(10)+","+str(values[3]).center(10) + "," + str(values[4]).center(10) + "," + str(values[5]).center(10))
                    file.write("\n")
                file.close()
                name = stock_dic[user_id][0].strip()
                brand = stock_dic[user_id][1].strip()
                rate = stock_dic[user_id][2].replace('$','').strip()
                purchase_more = input("Do you want to purchase more(Y/N) ?  ")
                # USING IF CONDITION FOR COMPLETION OF PURCHASE
                if purchase_more.lower()!= 'y':
                    # CALL FOR THE BIILING INVOICE AND PRINT THE BILL 
                    add_to_stock_billing(user_name,user_phone,purchase_dic)
                    break
                    
            else:
                # FOR NEW LAPTOP ADD TO THE STOCK
                print("The laptop ID you entered is not available in your Stock")
                print("Enter the following information of laptop you want to order")
                name = input("Model Name : ")
                brand = input("Brand : ")
                loop = True
                while loop == True:
                    try:
                        price = int(input("Price : "))
                        break
                    except:
                        print("Enter an intger value for price")
                
                loop = True
                while loop == True:
                    try:
                        quantity = int(input("Quantity : "))
                        while quantity < 1:
                            quantity = int(input("Enter Quantity : "))
                        break

                    except:
                        print("Enter an integer value for quantity")
                processor = input("Processor : ")
                graphic_card = input("Graphic Card : ")
                price = ' $' + str(price)
                # GETTING ALL THE INFO AND UPDATING IN THE DICTIONARY TO MAINTAIN STOCK
                stock_dic.update({next_sn:[name,brand,price,quantity,processor,graphic_card]})
                # ADDING TO THE TEMPORARY DICTINARY FOR THE INVOICE
                purchase_dic.update({psn:[name,brand,price,quantity]})
                psn += 1
                next_sn += 1
                # CALLING FOR INVOICE GENERATION
                add_to_stock_billing(user_name,user_phone,stock_dic)
                # ADDING PRODUCT TO THE STOCK
                with open("stock.txt","w") as file:
                    for key,values in stock_dic.items():
                        file.write(str(values[0]).center(18)+","+str(values[1]).center(15)+","+ str(values[2]).center(10)+","+str(values[3]).center(10) + "," + str(values[4]).center(10) + "," + str(values[5]).center(10))
                        file.write("\n")
                    file.close()

    elif user_input == 2:
        # USING IF CONDITION FOR SELL
        print("For billing purpose you have to submit your name")
        user_name = input("Enter Customer's name : ")
        user_phone = input("Enter Customer's phone : ")
        sell_option_message()
        display_stock()
        while True:

            loop = True
            while loop == True:
                try:
                    user_id = int(input("Enter the laptop ID you want to sell:  "))
                    break
                except:
                    print("Enter an integer value for ID's")
            
            while user_id <= 0 or user_id > len(stock_dic):

                print("Please provide a valid ID !!!")

                print("\n")
                loop = True
                while loop == True:
                    try:
                        user_id = int(input("Please Provide the ID of the laptop you want to sell :"))
                        break
                    except:
                        print("Enter an integer value for ID's")
                
            
            while True:
                try:
                    user_quantity = int(input("Please provide the number of quntity of the laptop you want to sell: "))
                    break
                except:
                    print("Enter an positive Integer value for quantity!")
            print("\n")
            
            #Valid Quantity

            get_quantity = stock_dic[user_id][3]
            # TAKING CONTROL OVER QUANTITY INPUT
            while  user_quantity <= 0 or user_quantity > int(stock_dic[user_id][3]):
                print("Dear Admin. Enter value from the stock!")
            
            
                user_quantity = int(input("Please Provide the number of quantity of the laptop you  want to sell: "))

                    

            #UpdatING the text file
            stock_dic[user_id][3] = int(get_quantity) - int(user_quantity)
            file = open("stock.txt","w")
            for values in stock_dic.values():
                file.write(str(values[0]).center(18) + "," + str(values[1]).center(15) + "," + str(values[2]).center(10) + "," + str(values[3]).center(10) + "," + str(values[4]).center(15) + "," + str(values[5]).center(15))
                file.write("\n")
            file.close()

            # billing function
            laptop_name = stock_dic[user_id][0]
            brand = stock_dic[user_id][1]
            rate = int(stock_dic[user_id][2].replace('$',''))
            user_quantity = int(user_quantity)
            sell_dic.update({ssn:[laptop_name,brand,rate,user_quantity]})
            ssn += 1

            sell_more = input("Do you want another Item to add(Y/N)?  ")
            # CONFIRMATION FOR COMPLETION OF SELLS
            if sell_more.lower() != 'y':
                shipping_confirmation = input("Do you want delivery at customer's door Step?...(If yes: 'Y'): ")
                if shipping_confirmation.lower() == "y":
                    loop = True
                    while loop == True:
                        try:
                            shipping_cost = int(input("Enter the shipping cost: "))
                            break
                        except:
                            print("Enter an integer value for ID's")
                    sell_to_customer_with_shipping(user_name, user_phone,shipping_cost,sell_dic)
                else:
                    sell_to_customer(user_name, user_phone,sell_dic)
                break
    
    elif user_input == 3:
        # CLOSING OF PROGRAM
        print("Thanks for using ...............")
        print("see you again..............\n\n\n")
        continue_loop = False
        break
    else:
        # THROWING ERROR FOR USER INPUT
        error()
