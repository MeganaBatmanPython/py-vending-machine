nickels_value = 1.25
dimes_value = 2.5
quarters_value = 6.25
nickel_amount = 25
dime_amount = 25
quarter_amount = 25
print("This is your very own vending machine program!")
print("Chips = $2.50")
print("Cookies = $2.50")
print("Cake = $3.00")
print("Soda = $3.50")
print("Water = $2.00")
print("Change maker initialized...")
print("Nickel number: 25")
print("Dime number: 25")
print("Quarter number: 25")
purchase_price=float(input("Please enter the price of your purchase."))
purchase_round=purchase_price*100
purchase_round=round(purchase_round,2)
purchase_round= purchase_round % 5
while purchase_round==0:
    print("Deposit menu:")
    print("n - deposit a nickel")
    print("q - deposit a quarter")
    print("d - deposit a dime")
    print("o - deposit a one dollar bill")
    print("f - deposit a five dollar bill")
    print("c - cancel (You can also press this when the 'payment due' shows you a negative number.)")
    user_menu=input("Please type in a letter from the menu.")
    change_100=None
    nickel_decrease=None
    if user_menu=="n" or "q" or "d" or "o" or "f" or "c":
        if user_menu=="n":
            user_menu_value=0.05
            if user_menu_value==purchase_price:
                print("You have finished. You don't have any more payment due.")
                print("Thanks for stopping by!")
                break;
            purchase_price=purchase_price-0.05
            round(purchase_price)
            print("Paymzent due: " +str(purchase_price))
        elif user_menu=="q":
            user_menu_value=0.25
            if user_menu_value == purchase_price:
                print("You have finished. You don't have any more payment due.")
                print("Thanks for stopping by!")
                break;
            purchase_price=purchase_price - 0.25
            round(purchase_price)
            print("Payment due: " + str(purchase_price))
            if user_menu_value>purchase_price:
                change=-1*purchase_price
                multiply_100=purchase_price*100
                divisibility=multiply_100%25
                if divisibility==0:
                    quarter_decrease=25-(multiply_100//25)
                    quarter_amount = quarter_decrease
                    print("Stock now...")
                    print("Nickel number: " + str(nickel_amount))
                    print("Dime number:  " + str(dime_amount))
                    print("Quarter number: " + str(quarter_amount))
                elif divisibility > 0:
                    dime_decrease = 25 - (-1) * (multiply_100 // 10)
                    dime_divi = multiply_100 % 10
                    if dime_divi > 0:
                        nickel_decrease = 25 - (-1) * (multiply_100 // 5)
                        nick_divi = multiply_100 % 5
                        if nick_divi > 0:
                            print("Please see store manager for the rest of your change.")
        elif user_menu=="d":
            user_menu_value=0.1
            if user_menu_value==purchase_price:
                print("You have finished. You don't have any more payment due.")
                print("Thanks for stopping by!")
                break;
            purchase_price = purchase_price - 0.1
            round(purchase_price)
            print("Payment due: " + str(purchase_price))
            if user_menu_value > purchase_price:
                change = -1 * purchase_price
                multiply_100 = purchase_price * 100
                divisibility = multiply_100 % 25
                if divisibility == 0:
                    quarter_decrease = 25 - (multiply_100 // 25)
                    quarter_amount = quarter_decrease
                    print("Stock now...")
                    print("Nickel number: " + str(nickel_amount))
                    print("Dime number:  " + str(dime_amount))
                    print("Quarter number: " + str(quarter_amount))
                elif divisibility > 0:
                    dime_decrease = 25 - (-1) * (multiply_100 // 10)
                    dime_divi = multiply_100 % 10
                    if dime_divi > 0:
                        nickel_decrease = 25 - (-1) * (multiply_100 // 5)
                        nick_divi = multiply_100 % 5
                        if nick_divi > 0:
                            print("Please see store manager for the rest of your change.")
        elif user_menu=="o":
            user_menu_value=1.00
            if user_menu_value==purchase_price:
                print("You have finished. You don't have any more payment due.")
                print("Thanks for stopping by!")
                break;
            purchase_price = purchase_price - 1.00
            round(purchase_price)
            print("Payment due: " + str(purchase_price))
            if user_menu_value > purchase_price:
                change = (-1) *(purchase_price)
                multiply_100 = purchase_price * 100
                divisibility = multiply_100 % 25
                if divisibility == 0:
                    quarter_decrease = 25 - (-1)*(multiply_100 // 25)
                    quarter_amount = quarter_decrease
                    print("Stock now...")
                    print("Nickel number: " + str(nickel_amount))
                    print("Dime number:  " + str(dime_amount))
                    print("Quarter number: " + str(quarter_amount))
                elif divisibility > 0:
                    dime_decrease = 25 - (-1) * (multiply_100 // 10)
                    dime_divi = multiply_100 % 10
                    if dime_divi > 0:
                        nickel_decrease = 25 - (-1) * (multiply_100 // 5)
                        nick_divi = multiply_100 % 5
                        if nick_divi > 0:
                            print("Please see store manager for the rest of your change.")
        elif user_menu=="f":
            user_menu_value = 5.00
            if user_menu_value==purchase_price:
                print("You have finished. You don't have any more payment due.")
                print("Thanks for stopping by!")
                break;
            purchase_price = purchase_price - 5.00
            round(purchase_price)
            print("Payment due: " + str(purchase_price))
            if user_menu_value > purchase_price:
                change = (-1*purchase_price)
                multiply_100 = purchase_price * 100
                divisibility = multiply_100 % 25
                if divisibility == 0:
                    quarter_decrease = 25 - (-1)*(multiply_100 // 25)
                    quarter_amount = quarter_decrease
                    print("Stock now...")
                    print("Nickel number: " + str(nickel_amount))
                    print("Dime number:  " + str(dime_amount))
                    print("Quarter number: " + str(quarter_amount))
                elif divisibility>0:
                    dime_decrease = 25 - (-1)*(multiply_100 // 10)
                    dime_divi=multiply_100 % 10
                    if dime_divi>0:
                        nickel_decrease = 25 - (-1)*(multiply_100 // 5)
                        nick_divi=multiply_100%5
                        if nick_divi>0:
                            print("Please see store manager for the rest of your change.")
                    nickel_amount=nickel_decrease
                    dime_amount=dime_decrease
                    print("Stock now...")
                    print("Nickel number: " +str(nickel_amount))
                    print("Dime number:  " +str(dime_amount))
                    print("Quarter number: " +str(quarter_amount))
        elif user_menu=="c":
            if change_100==0:
                print("Bye.")
                break;
            else:
                print("Here is your change: " + str(change) + " dollars")
                if nickel_amount<=0:
                    print("We have run out of nickels. please talk to the store manager.")
                elif dime_amount<=0:
                    print("We have run out of dimes, please see store manager.")
                elif quarter_amount<=0:
                    print('We have run out of quarters, please see store manager.')
                print("Thanks for stopping by!")
                break



else:
    print("Error. Please make your purchase price a multiple of 0.05.")






