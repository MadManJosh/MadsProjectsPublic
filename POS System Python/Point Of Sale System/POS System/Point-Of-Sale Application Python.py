import os
from dataclasses import dataclass
import datetime
import textwrap

timeNow = datetime.datetime.now()
timeNow = timeNow.strftime("%d/%m/%Y, %H:%M")

class   tableAssign:
    def __init__(self, cusCount = 0, tableWaiter = None, tableCost = 0, tableItemCount = 0, tableTimeOut = None):
        self.cusCount = cusCount
        self.tableWaiter = tableWaiter
        self.tableCost = tableCost
        self.tableItemCount = tableItemCount
        self.tableTimeOut = tableTimeOut

class orderInfo():
    def __init__(self, orderWait, orderCost, orderCust, orderItemCount, orderTable, orderTime):
        self.orderWait = orderWait = str = None
        self.orderCost = orderCost = int = 0
        self.orderCust = orderCust = int = 0 
        self.orderItemCount = orderItemCount = int = 0
        self.orderTable = orderTable = str = None    
        self.orderTime = orderTime = str = timeNow

class _billInfo():
    billTable  = str = None
    billTotal = int = 0
    billList = list = None
    billWait = billWait = str = None

class orderItem():
    orderItems = list = []
    orderItemAmount = list = []
    orderItemPrice = list = []

class cashTotal():
    def __init__(self, totalIncome = [0]):
        self.totalIncome = totalIncome

daysIncome = cashTotal() #The total income for the day. 

tableOne = tableAssign()
tableTwo = tableAssign()
tableThree = tableAssign()
tableFour = tableAssign()
tableFive = tableAssign()
tableSix = tableAssign()

tabOneItemOrdered = orderItem
tabTwoItemOrdered = orderItem
tabThreeItemOrdered = orderItem
tabFourItemOrdered = orderItem
tabFiveItemOrdered = orderItem
tabSixItemOrdered = orderItem

tabOneBill = [False] #These are used to check if a bill has been prepared or not.
tabTwoBill = [False]
tabThreeBill = [False]
tabFourBill = [False]
tabFiveBill = [False]
tabSixBill = [False]

orderTotal = [0]
totalItems = [0]

fileLocation = os.path.dirname(os.path.abspath(__file__))
os.chdir(fileLocation)

def loginScreen():
    print("Welcome to Highland's Cafe. ")
    print()
    print("1. Login")
    print("2. Exit")
    print()

    loginChoice = input()
    if int(loginChoice) == 1:
        loginFunc()
    elif int(loginChoice) ==  2:
        exit
    else:
        print("Please enter a valid option. ")
        loginScreen()

def readLogin():
    data = []
    file = open("Login.txt", "r")
    for line in file:
        line = line.strip()
        if line:
            userName, passCode = line.split(",")
            data.append((userName, passCode))
    return data

def loginFunc():
    global inputName
    inputName = input("What is your name? ")
    inputPass = input("Please enter your passcode: ")
    try:
        if passCheck(inputName, inputPass):
            print("Login successful. ")
            mainMenu()
        else:
            print("You entered an incorrect password or username. Please try again. ")
            loginFunc()
    except(ValueError): 
        print("Something went wrong. Returning to login screen.")
        print()
        loginScreen()
    else:
        if passCheck(inputName, inputPass):
            print("Login successful. ")
            mainMenu()
        else:
            print("You entered an incorrect password or username. Please try again. ")
            loginFunc()
    
def passCheck(userName, passCode):
    for checkName, checkPass in data:
        if checkName == userName and checkPass == passCode:
            return True
    return False
    
def mainMenu():
    print("Welcome, ", inputName, ".")
    print("")
    print("1. Assign Table. ")
    print("2. Change Customers. ")
    print("3. Add to Order. ")
    print("4. Prepare Bill. ")
    print("5. Complete Sale. ")
    print("6. Cash up. ")
    print("7. Log Out. ")
    print("")
    menuChoice = input("Select an action: ")
    if int(menuChoice) == 1:
        assTable()
    elif int(menuChoice) == 2:
        changeCust()
    elif int(menuChoice) == 3:
        addOrder()
    elif int(menuChoice) == 4:
        prepBill()
    elif int(menuChoice) == 5: 
        chaChing()
    elif int(menuChoice) == 6:
        dollaDollaBills()
    elif int(menuChoice) == 7:
        logOut()
    else:
        print("You entered an invalid option. Please try again.")
        mainMenu()

def assTable():
    print("Select which table you would like assigned to you.")
    print("")
    print("1. Table 1")
    print("2. Table 2")
    print("3. Table 3")
    print("4. Table 4")
    print("5. Table 5")
    print("6. Table 6")
    print("")
    tableGiven = input("Table: ")
    print()
    if int(tableGiven) == 1:
        tableOne.tableWaiter = inputName
        print("Table successfully assigned to ", inputName)
        addCusQuest = input("Would you like to add customers? [y/n] ")
        print("")
        if addCusQuest == "y":
            addCust = int(input("How many would you like to add? "))
            tableOne.cusCount += addCust
            print()
            print("Successfully added ", addCust, " customers to table ", tableGiven)
            assignAgain()
        elif addCusQuest == "n":
            print("You have chosen not to add customers. ")
            assignAgain()
        else:
            print("You entered an invalid option. Returning to previous page. ")
            assTable()

    elif int(tableGiven) == 2:
        tableTwo.tableWaiter = inputName
        print("Table successfully assigned to ", inputName)
        addCusQuest = input("Would you like to add customers? [y/n] ")
        print("")
        if addCusQuest == "y":
            addCust = int(input("How many would you like to add? "))
            tableTwo.cusCount += addCust
            print()
            print("Successfully added ", addCust, " customers to table ", tableGiven)
            assignAgain()
        elif addCusQuest == "n":
            print("You have chosen not to add customers. ")
            assignAgain()
        else:
            print("You entered an invalid option. Returning to previous page. ")
            assTable()

    elif int(tableGiven) == 3:
        tableThree.tableWaiter = inputName
        print("Table successfully assigned to ", inputName)
        addCusQuest = input("Would you like to add customers? [y/n] ")
        print("")
        if addCusQuest == "y":
            addCust = int(input("How many would you like to add? "))
            tableThree.cusCount += addCust
            print()
            assignAgain()
        elif addCusQuest == "n":
            print("You have chosen not to add customers. ")
            assignAgain()
        else:
            print("You entered an invalid option. Returning to previous page. ")
            assTable()

    elif int(tableGiven) == 4:
        tableFour.tableWaiter = inputName
        print("Table successfully assigned to ", inputName)
        addCusQuest = input("Would you like to add customers? [y/n] ")
        print("")
        if addCusQuest == "y":
            addCust = int(input("How many would you like to add? "))
            tableFour.cusCount += addCust
            print()
            print("Successfully added ", addCust, " customers to table ", tableGiven)
            assignAgain()
        elif addCusQuest == "n":
            print("You have chosen not to add customers. ")
            assignAgain()
        else:
            print("You entered an invalid option. Returning to previous page. ")
            assTable()

    elif int(tableGiven) == 5:
        tableFive.tableWaiter = inputName
        print("Table successfully assigned to ", inputName)
        addCusQuest = input("Would you like to add customers? [y/n] ")
        print("")
        if addCusQuest == "y":
            addCust = int(input("How many would you like to add? "))
            tableFive.cusCount += addCust
            print()
            print("Successfully added ", addCust, " customers to table ", tableGiven)
            assignAgain()
        elif addCusQuest == "n":
            print("You have chosen not to add customers. ")
            assignAgain()
        else:
            print("You entered an invalid option. Returning to previous page. ")
            assTable()

    elif int(tableGiven) == 6:
        tableSix.tableWaiter = inputName
        print("Table successfully assigned to ", inputName)
        addCusQuest = input("Would you like to add customers? [y/n] ")
        print("")
        if addCusQuest == "y":
            addCust = int(input("How many would you like to add? "))
            tableSix.cusCount += addCust
            print()
            print("Successfully added ", addCust, " customers to table ", tableGiven)
            assignAgain()
        elif addCusQuest == "n":
            print("You have chosen not to add customers. ")
            assignAgain()
        else:
            print("You entered an invalid option. Returning to previous page. ")
            assTable()

    else:
        print("You entered a problematic value. Please try again. ")
        print("")
        assTable()
    
def assignAgain():
    print()
    print("1. Continue in the table assignment menu. ")
    print("2. Go back to the main menu. ")
    print()
    goAgain = input("Where would you like to go? ")
    if int(goAgain) ==1:
        print()
        print("You have chosen to return to the table assignment menu. ")
        print()
        assTable()
    elif int(goAgain) == 2:
        print()
        print("You have chosen to go back to the menu. ")
        print()
        mainMenu()

    else:
        print("")
        print("You have entered an invalid value. Returning to the main menu. ")
        mainMenu()

def changeCust():
    print()
    print("Hey, ", inputName, ", you have chosen to make changes to a tables customer count. ")
    print()
    if tableOne.tableWaiter == inputName:
        print("1. Table 1")
    if tableTwo.tableWaiter == inputName:
        print("2. Table 2")
    if tableThree.tableWaiter == inputName:
        print("3. Table 3")
    if tableFour.tableWaiter == inputName:
        print("4. Table 4")
    if tableFive.tableWaiter == inputName:
        print("5. Table 5")
    if tableSix.tableWaiter == inputName:
        print("6. Table 6")
    print()
    tableChosen = input("Which table would you like to make changes to? Input 0 to exit. ")
    if tableChosen == 1 or 2 or 3 or 4 or 5 or 6:
        custChange = input("What would you like to change the customer count to?")
    if int(tableChosen) == 1:
        tableOne.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 1:
        tableOne.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 2:
        tableTwo.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 3:
        tableThree.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 4:
        tableFour.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 5:
        tableFive.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 6:
        tableSix.cusCount = custChange
        print()
        print("Table ", tableChosen, " customer count successfully changed to", custChange)
    elif int(tableChosen) == 0:
        mainMenu()
    else:
        print("Please enter a valid option. ")
        changeCust()
    print()
    changeContinue = input("Would you like to make more changes? [y/n] ")
    if changeContinue == "y":
        changeCust()
    elif changeContinue == "n":
        print()
        print("Returning to main menu. ")
        mainMenu()

def addOrder():
    stockList = open("Stock.txt", "r")
    for line in stockList:
        line = line.strip()
        if stockList:
            itemName, itemPrice = line.split(",")
    print()
    readStock()
    orderDetails()

def orderDetails():
    order = []
    stockList = open("Stock.txt", "r")
    print("Which table would you like to add the order to?")
    print()
    if tableOne.tableWaiter == inputName:
        print("1. Table One. ")
    elif tableTwo.tableWaiter == inputName:
        print("2. Table Two. ")
    elif tableThree.tableWaiter == inputName:
        print("3. Table Three. ")
    elif tableFour.tableWaiter == inputName:
        print("4. Table Four. ")
    elif tableFive.tableWaiter == inputName:
        print("5. Table Five. ")
    elif tableSix.tableWaiter == inputName:
        print("6. Table Six. ")
    else:
        print("The value you entered was not available. Please try again.")
        orderDetails
    orderTable = input("Which table is this order for?")
    if int(orderTable) == 1 and tableOne.tableWaiter == inputName:
        orderTable = tableOne
    elif int(orderTable) == 2 and tableTwo.tableWaiter == inputName:
        orderTable = tableTwo
    elif int(orderTable) == 3 and tableThree.tableWaiter == inputName:
        orderTable = tableThree
    elif int(orderTable) == 4 and tableFour.tableWaiter == inputName:
        orderTable = tableFour
    elif int(orderTable) == 5 and tableFive.tableWaiter == inputName:
        orderTable = tableFive
    elif int(orderTable) == 6 and tableSix.tableWaiter == inputName:
        orderTable = tableSix
    else:
        print("You either entered a table not assigned to you, or an invalid value. Try again. ")
        orderDetails()

    print("Hey,", inputName, "what would you like to add to your order?")
    itemChosen = int(input())

    for line in stockList:
        line = line.strip()
        if stockList:
            orderItem = stockList.readlines()
            orderedItem = orderItem[-1 + itemChosen]
            itemName, itemPrice = orderedItem.split(",")
    stockList.readline(itemChosen)
    print("You have chosen to add", itemName, "which costs R" + str(itemPrice))
    itemCount = int(input("How many would they like to buy? "))
    itemTotal = int(int(itemPrice) * itemCount)
    orderTotal[0] += itemTotal
    totalItems[0] += itemCount
    if orderTable == tableOne:
        tabOneList = tabOneItemOrdered.orderItems
        tabOneList.append(itemName)
        tabOnePriceList = tabOneItemOrdered.orderItemPrice
        tabOneAmount = tabOneItemOrdered.orderItemAmount
        tabOneAmount.append(itemCount)
        tabOnePriceList.append(itemPrice)
    elif orderTable == tableTwo:
        tabTwoList = tabTwoItemOrdered.orderItems
        tabTwoList.append(itemName)
        tabTwoPriceList = tabTwoItemOrdered.orderItemPrice
        tabTwoAmount = tabTwoItemOrdered.orderItemAmount
        tabTwoAmount.append(itemCount)
        tabTwoPriceList.append(itemPrice)
    elif orderTable == tableThree:
        tabThreeList = tabThreeItemOrdered.orderItems
        tabThreeList.append(itemName)
        tabThreePriceList = tabThreeItemOrdered.orderItemPrice
        tabThreeAmount = tabThreeItemOrdered.orderItemAmount
        tabThreeAmount.append(itemCount)
        tabThreePriceList.append(itemPrice)
    elif orderTable == tableFour:
        tabFourList = tabFourItemOrdered.orderItems
        tabFourList.append(itemName)
        tabFourPriceList = tabFourItemOrdered.orderItemPrice
        tabFourAmount = tabFourItemOrdered.orderItemAmount
        tabFourAmount.append(itemCount)
        tabFourPriceList.append(itemPrice)
    elif orderTable == tableFive:
        tabFiveList = tabFiveItemOrdered.orderItems
        tabFiveList.append(itemName)
        tabFivePriceList = tabFiveItemOrdered.orderItemPrice
        tabFiveAmount = tabFiveItemOrdered.orderItemAmount
        tabFiveAmount.append(itemCount)
        tabFivePriceList.append(itemPrice)
    elif orderTable == tableSix:
        tabSixList = tabSixItemOrdered.orderItems
        tabSixList.append(itemName)
        tabSixPriceList = tabSixItemOrdered.orderItemPrice
        tabSixAmount = tabSixItemOrdered.orderItemAmount
        tabSixAmount.append(itemCount)
        tabSixPriceList.append(itemPrice)
    else:
        print()
        print("Something went wrong, returning to the main menu. ")
        mainMenu()
    
    print("The total for that item is R" + str(itemTotal) + ".")
    print("That brings the order to R" + str(orderTotal[0]) +".")
    print()
    orderTable.tableCost = orderTotal
    orderTable.tableItemCount = totalItems[0]
    orderTable.tableTimeOut = timeNow
    orderContinue()

def orderContinue():
    orderAgain = input("Is there more to the order? [y/n]")
    if orderAgain == "y":
        orderDetails()
    elif orderAgain == "n":
        print()
        print("Returning to main menu. ")
        mainMenu()
    else:
        print()
        print("You entered an incorrect value. Please try again.")
        print()
        orderAgain()

def readStock():
    itemNum = -1
    file = open("Stock.txt", "r")
    for line in file:
        line = line.strip()
        if line:
            itemName, itemPrice = line.split(",")
            itemNum += 1
            print(str(itemNum) + ". ", itemName, " R" + str(itemPrice) )

def prepBill():
    print()
    print("You have chosen to prepare a bill. ")
    if tableOne.tableWaiter == inputName:
        print("1. Table One")
    elif tableTwo.tableWaiter == inputName:
        print("2. Table Two")
    elif tableThree.tableWaiter == inputName:
        print("3. Table Three")
    elif tableFour.tableWaiter == inputName:
        print("4. Table Four")
    elif tableFive.tableWaiter == inputName:
        print("5. Table Five")
    elif tableSix.tableWaiter == inputName:
        print("6. Table Six")
    else:
        print("You currently don't have any tables assigned to you. Returning to main menu. ")
        mainMenu()
    print()
    tableChoice = input("Which table are you preparing a bill for? ")
    print()

    tableNice = input("Where they nice people? [y/n]") #If they were nice to the waiter/waitress, then they get a little discount on their meal. 
    print()
    if tableNice == "y":
        niceTotal = 0.85
    elif tableNice == "n":
        niceTotal = 1
    else:
        pass

    if int(tableChoice) == 1 and tableOne.tableWaiter == inputName:
        tableBill = "Table One"
        billTotal = tableOne.tableCost
        billList = tabOneItemOrdered.orderItems
        billWait = tableOne.tableWaiter
        billItemList = tabOneItemOrdered.orderItems
        billPriceList = tabOneItemOrdered.orderItemPrice
        billItemAmount = tabOneItemOrdered.orderItemAmount
        billBool = tabOneBill
    elif int(tableChoice) == 2 and tableTwo.tableWaiter == inputName:
        tableBill = "Table Two"
        billTotal = tableTwo.tableCost
        billList = tabTwoItemOrdered.orderItems
        billWait = tableTwo.tableWaiter
        billItemList = tabTwoItemOrdered.orderItems
        billPriceList = tabTwoItemOrdered.orderItemPrice
        billItemAmount = tabTwoItemOrdered.orderItemAmount
        billBool = tabTwoBill
    elif int(tableChoice) == 3 and tableThree.tableWaiter == inputName:
        tableBill = "Table Three"
        billTotal = tableThree.tableCost
        billList = tabThreeItemOrdered.orderItems
        billWait = tableThree.tableWaiter
        billItemList = tabThreeItemOrdered.orderItems
        billPriceList = tabThreeItemOrdered.orderItemPrice
        billItemAmount = tabThreeItemOrdered.orderItemAmount
        billBool = tabThreeBill
    elif int(tableChoice) == 4 and tableFour.tableWaiter == inputName:
        tableBill = "Table Four"
        billTotal = tableFour.tableCost
        billList = tabFourItemOrdered.orderItems
        billWait = tableFour.tableWaiter
        billItemList = tabFourItemOrdered.orderItems
        billPriceList = tabFourItemOrdered.orderItemPrice
        billItemAmount = tabFourItemOrdered.orderItemAmount
        billBool = tabFourBill
    elif int(tableChoice) == 5 and tableFive.tableWaiter == inputName:
        tableBill = "Table Five"
        billTotal = tableFive.tableCost
        billList = tabFiveItemOrdered.orderItems
        billWait = tableFive.tableWaiter
        billItemList = tabFiveItemOrdered.orderItems
        billPriceList = tabFiveItemOrdered.orderItemPrice
        billItemAmount = tabFiveItemOrdered.orderItemAmount
        billBool = tabFiveBill
    elif int(tableChoice) == 6 and tableSix.tableWaiter == inputName:
        tableBill = "Table Six"
        billTotal = tableSix.tableCost
        billList = tabSixItemOrdered.orderItems
        billWait = tableSix.tableWaiter
        billItemList = tabSixItemOrdered.orderItems
        billPriceList = tabSixItemOrdered.orderItemPrice
        billItemAmount = tabSixItemOrdered.orderItemAmount
        billBool = tabSixBill
    else:
        print("Something went wrong, returning to main menu. ")
        print()
        mainMenu()
    _billInfo.billList = billList
    _billInfo.billTable = tableBill
    _billInfo.billTotal = billTotal
    _billInfo.billWait = billWait
    orderItem.orderItems = billItemList
    orderItem.orderItemPrice = billPriceList
    orderItem.orderItemAmount = billItemAmount


    print("---------------------------------------------------------------------------------------")
    print("Bill for", tableBill)
    for x in range(len(billItemList)):
        print()
        print("             Item:", billItemList[x], "               Quantity:", billItemAmount[x], "             Price:", billPriceList[x]) 
    print("The total for your bill was R" + str(billTotal[0] * niceTotal))
    print()
    print("You were helped by", billWait)
    print("Tip culture is kinda messed up, but please consider leaving a tip if you felt that", billWait, "deserved one!")
    print()
    print("---------------------------------------------------------------------------------------")
    billBool[0] = True
    print("Enter 1 to return to main menu. ")
    billReturn = input()
    if int(billReturn) == 1:
        print()
        mainMenu()
    else:
        print()
        print("You thought your were slick entering an ivalid value, huh? Welp, now you are going back the menu, anyway, retard :P ") #Please don't deduct marks for rudeness...

def chaChing(): #Function to complete a sail
    print()
    print("You are assigned to the following tables: ")
    print()
    if tableOne.tableWaiter == inputName:
        print("1. Table One")
    elif tableTwo.tableWaiter == inputName:
        print("2. Table Two")
    elif tableThree.tableWaiter == inputName:
        print("3. Table Three")
    elif tableFour.tableWaiter == inputName:
        print("4. Table Four")
    elif tableFive.tableWaiter == inputName:
        print("5. Table Five")
    elif tableSix.tableWaiter == inputName:
        print("6. Table Six")
    else:
        print("You currently don't have any tables assigned to you. Returning to main menu. ")
        mainMenu()
    tableChosen = input("Which table would you like to complete a sale for? ")
    print()
    if int(tableChosen) == 1 and tableOne.tableWaiter == inputName:
        if tabOneBill[0] == True:
            saleCustCount = tableOne.cusCount
            saleCost = tableOne.tableCost
            saleWait = tableOne.tableWaiter
            saleItemName = tabOneItemOrdered.orderItems
            saleItemAmount = tabOneItemOrdered.orderItemAmount
            saleItemPrice = tabOneItemOrdered.orderItemPrice
        else:
            print()
            print("You have not completed the bill for this table. Please do so before finishing a sale. ")
            prepBill()

    elif int(tableChosen) == 2 and tableTwo.tableWaiter == inputName:
        if tabTwoBill[0] == True:
            saleCustCount = tableTwo.cusCount
            saleCost = tableTwo.tableCost
            saleWait = tableTwo.tableWaiter
            saleItemName = tabTwoItemOrdered.orderItems
            saleItemAmount = tabTwoItemOrdered.orderItemAmount
            saleItemPrice = tabTwoItemOrdered.orderItemPrice
        else:
            print()
            print("You have not completed the bill for this table. Please do so before finishing a sale. ")
            prepBill()

    elif int(tableChosen) == 3 and tableThree.tableWaiter == inputName:
        if tabThreeBill[0] == True:
            saleCustCount = tableThree.cusCount
            saleCost = tableThree.tableCost
            saleWait = tableThree.tableWaiter
            saleItemName = tabThreeItemOrdered.orderItems
            saleItemAmount = tabThreeItemOrdered.orderItemAmount
            saleItemPrice = tabThreeItemOrdered.orderItemPrice
        else:
            print()
            print("You have not completed the bill for this table. Please do so before finishing a sale. ")
            prepBill()

    elif int(tableChosen) == 4 and tableFour.tableWaiter == inputName:
        if tabFourBill[0] == True:
            saleCustCount = tableFour.cusCount
            saleCost = tableFour.tableCost
            saleWait = tableFour.tableWaiter
            saleItemName = tabFourItemOrdered.orderItems
            saleItemAmount = tabFourItemOrdered.orderItemAmount
            saleItemPrice = tabFourItemOrdered.orderItemPrice
        else:
            print()
            print("You have not completed the bill for this table. Please do so before finishing a sale. ")
            prepBill()

    elif int(tableChosen) == 5 and tableFive.tableWaiter == inputName:
        if tabFiveBill[0] == True:
            saleCustCount = tableFive.cusCount
            saleCost = tableFive.tableCost
            saleWait = tableFive.tableWaiter
            saleItemName = tabFiveItemOrdered.orderItems
            saleItemAmount = tabFiveItemOrdered.orderItemAmount
            saleItemPrice = tabFiveItemOrdered.orderItemPrice
        else:
            print()
            print("You have not completed the bill for this table. Please do so before finishing a sale. ")
            prepBill()

    elif int(tableChosen) == 6 and tableSix.tableWaiter == inputName:
        if tabSixBill[0] == True:
            saleCustCount = tableSix.cusCount
            saleCost = tableSix.tableCost
            saleWait = tableSix.tableWaiter
            saleItemName = tabSixItemOrdered.orderItems
            saleItemAmount = tabSixItemOrdered.orderItemAmount
            saleItemPrice = tabSixItemOrdered.orderItemPrice
        else:
            print()
            print("You have not completed the bill for this table. Please do so before finishing a sale. ")
            prepBill()
    else: 
        print("You entered an invalid value. Please try again. That table might not be assigned to you. Returning to main menu. ")
        mainMenu()
    input("Think of a good name for the file. Don't forget the .txt at the end! Press enter when you are ready. ")
    print()
    fileName = input("The file name: ")
    fileNametxt = fileName + ".txt"
    print()
    print("Hmmm... It isn't very original, but it'll do. I guess...")
    open(fileNametxt, "x")
    newFile = open(fileNametxt, "a")

    itemString = ""

    for x in saleItemName:
        itemString += "" + str(x)
    
    itemTotalInt = sum([int(x) for x in saleItemAmount])
    itemAmountString = ""
    for x in saleItemAmount:
        itemAmountString += "" + str(x)
    
    salePriceInt = sum([int(x) for x in saleItemPrice])
    saleItemPriceString = ""
    for x in saleItemPrice:
        saleItemPriceString += "" + str(x)

    custCountString = str(saleCustCount)
    costString = str(saleCost)
    
    tabChosenWrite = "The table served is: ", tableChosen, "\n"
    saleTimeWrite = "The time this was completed was:", timeNow, "\n"
    saleItemWrite = "The items sold were:", itemString, "\n"
    saleAmountWrite = "The amount of the respective items sold are:", str(itemTotalInt), "\n"
    salePriceWrite = "The quantative amount made off each respective item:",  str(salePriceInt), "\n"
    saleCustWrite = "The amount of people seated at the table:", str(saleCustCount), "\n"
    saleTotalWrite = "Total income of the sale:", str(saleCost), "\n"
    saleWaitWrite = "The ever awesome waitstaff that completed this sail:", saleWait, "\n:"
    

    newFile.writelines(tabChosenWrite)
    newFile.writelines(saleTimeWrite)
    newFile.writelines(saleItemWrite)
    newFile.writelines(saleAmountWrite)
    newFile.writelines(salePriceWrite)
    newFile.writelines(saleCustWrite)
    newFile.writelines(saleTotalWrite)
    newFile.writelines(saleWaitWrite)
    newFile.close()
    
    print("Sale completed. I hope you know that this program was made my an unpayed kid. Be happy he slaved away for you!")
    print()
    print("Returning to main menu.")
    if int(tableChosen) == 1:
        tableOne.tableItemCount = 0
        tableOne.tableWaiter = None
        tableOne.tableCost = 0
    elif int(tableChosen) == 2:
        tableTwo.tableItemCount = 0
        tableTwo.tableWaiter = None
        tableTwo.tableCost = 0
    elif int(tableChosen) == 3:
        tableThree.tableItemCount = 0
        tableThree.tableWaiter = None
        tableThree.tableCost = 0
    elif int(tableChosen) == 4:
        tableFour.tableItemCount = 0
        tableFour.tableWaiter = None
        tableFour.tableCost = 0
    elif int(tableChosen) == 5:
        tableFive.tableItemCount = 0
        tableFive.tableWaiter = None
        tableFour.tableCost = 0
    elif int(tableChosen) == 6:
        tableSix.tableItemCount = 0
        tableSix.tableWaiter = None
        tableSix.tableCost = 0

    currentTotal = daysIncome.totalIncome[0]
    newTotal = currentTotal + saleCost[0]
    daysIncome.totalIncome[0] = newTotal
    
    mainMenu()

def dollaDollaBills(): #Function to check current total income. Tied to the Cash Up option in the menu.
    print()
    print("The total income for the day is:", daysIncome.totalIncome[0])
    input("Press Enter to return to the main menu.")
    mainMenu()

def logOut():
    print()
    print("You have been logged out. ")
    print()
    loginScreen()

open("Stock.txt", "a")

data = readLogin()
loginScreen()