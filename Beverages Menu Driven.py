import os

total1 = red_horse = 250
total2 = San_Mig = 300
total3 = SM_Pilsen = 250
total4 = Colt_45 = 250
total5 = Gold_Eagle = 300
total6 = Heineken = 300
total7 = Tiger_Crystan = 300

RH_Price = 250.00
SM_Price = 200.00
SMPP_Price = 90.00
Colt_Price = 150.00
GE_Price = 175.00
Heineken_Price = 75.00
TC_Price = 120.00

amount1 = amount2 = amount3 = amount4 = amount5 = amount6 = amount7 = 0
Total_amount1 = Total_amount2 = Total_amount3 = Total_amount4 = Total_amount5 = Total_amount6 = Total_amount7 = 0
sold1 = sold2 = sold3 = sold4 = sold5 = sold6 = sold7 = 0
Total_sales = 0

while True:
    os.system('cls')
    print("1.Case Inventory")
    print("2.Take Orders")
    print("3.Weekly Sales and Purchased Records")
    print("4.Final Inventory")
    print("5.exit")

    choice = int(input("\nEnter your number of choice: "))
    os.system('cls')
    while choice == 1:
        os.system('cls')
        print("\nThe amounts of drinks that we have for this week: ")
        print("Red Horse = %d" % red_horse)
        print("San Mig Light = %d" % San_Mig)
        print("San Miguel Pale Pilsen = %d" % SM_Pilsen)
        print("Colt 45 = %d" % Colt_45)
        print("Gold Eagle = %d" % Gold_Eagle)
        print("Heineken = %d" % Heineken)
        print("Tiger Crystan = %d" % Tiger_Crystan)

        press = input("\nPress any key to continue or x to exit: ")
        if press.lower() == 'x':
            break

    while choice == 2:
        os.system('cls')
        print("\n1.Red Horse - %.2f" % (RH_Price))
        print("2.San Mig Light - %.2f" % (SM_Price))
        print("3.San Miguel Pale Pilsen - %.2f" % (SMPP_Price))
        print("4.Colt 45 - %.2f" % (Colt_Price))
        print("5.Gold Eagle - %.2f" % (GE_Price))
        print("6.Heineken - %.2f" % (Heineken_Price))
        print("7.Tiger Crystan - %.2f" % (TC_Price))

        order = int(input("\nInput orders: "))

        if order == 1:

            print("\nRed Horse")
            num1 = int(input("\nNumber of orders: "))
            amount1 = num1 * RH_Price
            total1 -= num1
            Total_amount1 += amount1
            sold1 += num1

        elif order == 2:
            print("\nSan Mig Light")
            num2 = int(input("\nNumber of orders: "))
            amount2 = num2 * SM_Price
            total2 -= num2
            Total_amount2 += amount2
            sold2 += num2

        elif order == 3:
            print("\nSan Miguel Pale Pilsen")
            num3 = int(input("\nNumber of orders: "))
            amount3 = num3 * SMPP_Price
            total3 -= num3
            Total_amount3 += amount3
            sold3 += num3

        elif order == 4:
            print("\nColt 45")
            num4 = int(input("\nNumber of orders: "))
            amount4 = num4 * Colt_Price
            total4 -= num4
            Total_amount4 += amount4
            sold4 += num4

        elif order == 5:
            print("\nGold Eagle")
            num5 = int(input("\nNumber of orders: "))
            amount5 = num5 * GE_Price
            total5 -= num5
            Total_amount5 += amount5
            sold5 += num5

        elif order == 6:
            print("\nHeineken")
            num6 = int(input("\nNumber of orders: "))
            amount6 = num6 * Heineken_Price
            total6 -= num6
            Total_amount6 += amount6
            sold6 += num6

        elif order == 7:
            print("\nTiger Crystan")
            num7 = int(input("\nNumber of orders: "))
            amount7 = num7 * TC_Price
            total7 -= num7
            Total_amount7 += amount7
            sold7 += num7

        press = input("\nPress any key to continue or x to exit: ")
        if press.lower() == 'x':
            break

    while choice == 3:
        os.system('cls')
        print("\nWeekly Sales and Purchased Records")

        print("\nRed Horse:")
        print("Item purchased for this week: %d" % int(sold1))
        print("Total sales for Red Horse: P{:,.2f}".format(float(Total_amount1)))

        print("\nSan Mig Light:")
        print("Item purchased for this week: %d" % int(sold2))
        print("Total sales for San Mig Light: P{:,.2f}".format(float(Total_amount2)))

        print("\nSan Miguel Pale Pilsen:")
        print("Item purchased for this week: %d" % int(sold3))
        print("Total sales for San Miguel Pale Pilsen: P{:,.2f}".format(float(Total_amount3)))

        print("\nColt 45:")
        print("Item purchased for this week: %d" % int(sold4))
        print("Total sales for Colt 45: P{:,.2f}".format(float(Total_amount4)))

        print("\nGold Eagle:")
        print("Item purchased for this week: %d" % int(sold5))
        print("Total sales for Gold Eagle: P{:,.2f}".format(float(Total_amount5)))

        print("\nHeineken:")
        print("Item purchased for this week: %d" % int(sold6))
        print("Total sales for Heineken: P{:,.2f}".format(float(Total_amount6)))

        print("\nTiger Crystan:")
        print("Item purchased for this week: %d" % int(sold7))
        print("Total sales for Tiger Crystan: P{:,.2f}".format(float(Total_amount7)))

        Sales = Total_amount1 + Total_amount2 + Total_amount3 + Total_amount4 + Total_amount5 + Total_amount6 + Total_amount7
        Total_sales += Sales

        print("\nTotal gross sales for this week: P{:,.2f}".format(float(Total_sales)))

        press = input("\nPress any key to continue or x to exit: ")
        if press.lower() == 'x':
            break

    while choice == 4:
        os.system('cls')
        print("\nFINAL INVENTORY")

        print("\nRED HORSE:")
        print("Stocks remaining: %d" % int(total1))
        if total1 <= 30 and total1 >= 1:
            print("We are running out of stocks")
        elif total1 == 0:
            print("We are out of stocks")

        print("\nSAN MIG LIGHT")
        print("Stocks remaining: %d" % int(total2))
        if total2 <= 30 and total2 >= 1:
            print("We are running out of stocks")
        elif total2 == 0:
            print("We are out of stocks")

        print("\nSAN MIGUEL PALE PILSEN")
        print("Stocks remaining: %d" % int(total3))
        if total3 <= 30 and total3 >= 1:
            print("We are running out of stocks")
        elif total3 == 0:
            print("We are out of stocks")

        print("\nCOLT 45")
        print("Stocks remaining: %d" % int(total4))
        if total4 <= 30 and total4 >= 1:
            print("We are running out of stocks")
        elif total4 == 0:
            print("We are out of stocks")

        print("\nGOLD EAGLE")
        print("Stocks remaining: %d" % int(total5))
        if total5 <= 30 and total5 >= 1:
            print("We are running out of stocks")
        elif total5 == 0:
            print("We are out of stocks")

        print("\nHEINEKEN")
        print("Stocks remaining: %d" % int(total6))
        if total6 <= 30 and total6 >= 1:
            print("We are running out of stocks")
        elif total6 == 0:
            print("We are out of stocks")

        print("\nCTIGER CRYSTAN")
        print("Stocks remaining: %d" % int(total7))
        if total7 <= 30 and total7 >= 1:
            print("We are running out of stocks")
        elif total7 == 0:
            print("We are out of stocks")

        press = input("\nPress any key to continue or x to exit: ")
        if press.lower() == 'x':
            break

    if choice == 5:
        break
