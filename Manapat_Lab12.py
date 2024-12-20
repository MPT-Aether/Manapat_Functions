"""
1.) Problem Statement:

• Create a Python program to simulate a simple food ordering system.


2.) Functional Requirements:

• Display Menu: Present a list of food items with their prices.
• Order Selection: Allow the user to choose an item from the menu.
• Calculate Total: Determine the total cost of the selected item.
• Payment Processing:
    ○ Prompt the user to input the cash rendered.
    ○ Validate if the cash is sufficient to cover the total cost.
    ○ If insufficient, repeatedly ask for payment until the amount is valid.
    ○ Calculate and display the change

"""

def potato_corner():
    fries_flavors = ["Barbeque", "Cheese", "Sour Cream", "Chili Barbeque", "Chili Cheese", "White Cheddar", "Wasabi", "Golden Sweet Corn", "Truffle"]
    fries_sizes = ["1 - Regular Fries = Php 41.00", "2 - Large Fries = Php 67.00", "3 - Jumbo Fries = Php 97.00","4 - Mega Fries = Php 127.00","5 - Giga Fries = Php 198.00","6 - Tera Fries = Php 228.00"]
    
    while True: 
        print("\nHello and welcome to Potato Corner's Virtual Site Menu!")
        print("=======================================================")
        
        for sizes in fries_sizes:
            print(sizes)
            
        order = int(input("\nPlease select your order: "))  
        
        if order == 1:
            print("=============")
            for flavors in fries_flavors:
                print(flavors)
            print("=============")
            flavor = input("Please choose your flavor: ")
            print("=============")
            payment = int(input("Please enter your payment: "))
            if payment == 41:
                print(f"Your order is successful! \nOrder: \nRegular Fries \n{flavor} \nTotal Cost: Php 41.00 \nChange: Php 0.00")
            elif payment > 41:
                change = payment - 41
                print(f"Your order is successful! \nOrder: \nRegular Fries \n{flavor} \nTotal Cost: Php {payment}.00 \nChange: Php {change}.00")
            elif payment < 41:
                print("Your payment is insufficient. Order unsuccessful.")
            else:
                print("Invalid payment, order unsuccessful. Next customer or order!")

        
        elif order == 2:
            print("=============")
            for flavors in fries_flavors:
                print(flavors)
            print("=============")
            flavor = input("Please choose your flavor: ")
            print("=============")
            payment = int(input("Please enter your payment: "))
            if payment == 67:
                print(f"Your order is successful! \nOrder: \nLarge Fries \n{flavor} \nTotal Cost: Php 67.00 \nChange: Php 0.00")
            elif payment > 67:
                change = payment - 67
                print(f"Your order is successful! \nOrder: \nLarge Fries \n{flavor} \nTotal Cost: Php {payment}.00 \nChange: Php {change}.00")
            elif payment < 67:
                print("Your payment is insufficient. Order unsuccessful.")
            else:
                print("Invalid payment, order unsuccessful. Next customer or order!")

        elif order == 3:
            print("=============")
            for flavors in fries_flavors:
                print(flavors)
            print("=============")
            flavor = input("Please choose your flavor: ")
            print("=============")
            payment = int(input("Please enter your payment: "))
            if payment == 97:
                print(f"Your order is successful! \nOrder: \nJumbo Fries \n{flavor} \nTotal Cost: Php 97.00 \nChange: Php 0.00")
            elif payment > 97:
                change = payment - 97
                print(f"Your order is successful! \nOrder: \nJumbo Fries \n{flavor} \nTotal Cost: Php {payment}.00 \nChange: Php {change}.00")
            elif payment < 97:
                print("Your payment is insufficient. Order unsuccessful.")
            else:
                print("Invalid payment, order unsuccessful. Next customer or order!")

        elif order == 4:
            print("=============")
            for flavors in fries_flavors:
                print(flavors)
            print("=============")
            flavor_1 = input("Please choose your first flavor: ")
            flavor_2 = input("Please choose your second flavor: ")
            print("=============")
            payment = int(input("Please enter your payment: "))
            if payment == 127:
                print(f"Your order is successful! \nOrder: \nMega Fries \n{flavor_1} & {flavor_2} \nTotal Cost: Php 97.00 \nChange: Php 0.00")
            elif payment > 127:
                change = payment - 127
                print(f"Your order is successful! \nOrder: \nMega Fries \n{flavor_1} & {flavor_2} \nTotal Cost: Php {payment}.00 \nChange: Php {change}.00")
            elif payment < 127:
                print("Your payment is insufficient. Order unsuccessful.")
            else:
                print("Invalid payment, order unsuccessful. Next customer or order!")

        elif order == 5:
            print("=============")
            for flavors in fries_flavors:
                print(flavors)
            print("=============")
            flavor_1 = input("Please choose your first flavor: ")
            flavor_2 = input("Please choose your second flavor: ")
            print("=============")
            payment = int(input("Please enter your payment: "))
            if payment == 198:
                print(f"Your order is successful! \nOrder: \nGiga Fries \n{flavor_1} & {flavor_2} \nTotal Cost: Php 97.00 \nChange: Php 0.00")
            elif payment > 198:
                change = payment - 198
                print(f"Your order is successful! \nOrder: \nGiga Fries \n{flavor_1} & {flavor_2} \nTotal Cost: Php {payment}.00 \nChange: Php {change}.00")
            elif payment < 198:
                print("Your payment is insufficient. Order unsuccessful.")
            else:
                print("Invalid payment, order unsuccessful. Next customer or order!")

        elif order == 6:
            print("=============")
            for flavors in fries_flavors:
                print(flavors)
            print("=============")
            flavor_1 = input("Please choose your first flavor: ")
            flavor_2 = input("Please choose your second flavor: ")
            flavor_3 = input("Please choose your third flavor: ")
            print("=============")
            payment = int(input("Please enter your payment: "))
            if payment == 228:
                print(f"Your order is successful! \nOrder: \nTera Fries \n{flavor_1}, {flavor_2}, and {flavor_3} \nTotal Cost: Php 97.00 \nChange: Php 0.00")
            elif payment > 228:
                change = payment - 228
                print(f"Your order is successful! \nOrder: \nTera Fries \n{flavor_1}, {flavor_2}, and {flavor_3} \nTotal Cost: Php {payment}.00 \nChange: Php {change}.00")
            elif payment < 228:
                print("Your payment is insufficient. Order unsuccessful.")
            else:
                print("Invalid payment, order unsuccessful. Next customer or order!")
    
        else:
            print("I am sorry but that is an invalid choice.")
      
potato_corner()
            
