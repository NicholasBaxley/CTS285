# For ownedStocks list [0,1,2] 0->Mcdonalds Stocks, 1->Kmart Stocks, 2->Walmart Stocks
import random

# The main menu for the game
def menu():
    global money
    global ownedStocks
    mcdStock = changeStockValue()
    kmartStock = changeStockValue()
    walmartStock = changeStockValue()
    loop = 1
    while loop == 1:
        menuSelect = input("What do you want to do? (Show Money, Stock Prices, Buy Stocks, Sell Stocks, Quit, Reset) ").lower()
        if menuSelect == "show money":
            print("$",money, sep="")
            print("Current owned stocks is:\n","Mc:",ownedStocks[0],
            " K:",ownedStocks[1]," W:",ownedStocks[2])
        elif menuSelect == "stock prices":           
            print("Mcdonalds is now",mcdStock,"|Kmart is now",kmartStock,"|Walmart is now",walmartStock,)
        elif menuSelect == "buy stocks":
            loop = 2
            stockbuy(mcdStock,kmartStock,walmartStock)
        elif menuSelect == "quit":
            loop = 2
        elif menuSelect == "reset":
            money = 10000
            ownedStocks = [0,0,0]
            print()
            print("Money has been reset to 10k and you own no stocks.")
        elif menuSelect == "sell stocks":
            loop = 2
            sellstocks(mcdStock, kmartStock, walmartStock)
        else:
            print("Not an option! ")
   
# Gives a random value to the company stock prices 
def changeStockValue():
    stock = random.randint(50, 200)
    return stock

# Asks the player how many stocks they wanna buy from each company
def stockbuy(mcdStock, kmartStock, walmartStock):
    global money 
    global ownedStocks
    leftOverMoney = 1
    loop = 1
    while loop == 1:
        print()
        print("Whose stock do you want to invest in? (Mcdonalds, Kmart, Walmart, or type stop at any time to return to menu) ")
        company = input().lower()
        if company == "mcdonalds":
            stockPrice = mcdStock
            loop = 2
        elif company == "kmart":
            stockPrice = kmartStock
            loop = 2
        elif company == "walmart":
            stockPrice = walmartStock
            loop = 2
        elif company == "stop":
            loop = 3
            menu()
        else:
            print("Not an option!")
        while loop == 2:
            print("How many do you wanna buy? (or type stop at any time to return to menu) ")
            buyAmount = input()
            if buyAmount == "stop":
                loop = 3
                menu()
                break
            elif not isNumber(buyAmount):
                print("Only accepts 'stop' or a number.")
                continue
            else:
                buyAmount = int(buyAmount)              
                leftOverMoney = money - (buyAmount * stockPrice)
            if leftOverMoney < 0:
                print()
                print("You need",buyAmount*stockPrice,"to purchase that much!")
                print("You only have",money)
                print()
            elif leftOverMoney > 0:
                addstocks(company, buyAmount)
                totalCost = buyAmount * stockPrice
                money = leftOverMoney
                print("The cost was $",totalCost, sep="")
                print("Current money is $",money, sep="")
                print("Current owned stocks is:\n","Mc:",ownedStocks[0],
                      " K:",ownedStocks[1]," W:",ownedStocks[2])
                loop = 3
                menu()
                
# Increases the stocks the player owns by the argument amount
def addstocks(company, amount):
    global ownedStocks
    if company == "mcdonalds":
        ownedStocks[0] += amount
    elif company == "kmart":
        ownedStocks[1] += amount
    elif company == "walmart":
        ownedStocks[2] += amount
        
# Takes the player to the selling stocks menu       
def sellstocks(mcdStock, kmartStock, walmartStock):
    global ownedStocks
    global money
    print()
    print("What stocks do you want to sell? (McDonalds, Kmart, Walmart, or type stop at any time.) ")
    stocks = input()
    tempoStocks = 0
    while tempoStocks == 0:
        if stocks.lower() == "mcdonalds": 
            tempoStocks = 0
            owned = ownedStocks[0]
            stockPrice = mcdStock
        elif stocks.lower() == "kmart": 
            tempoStocks = 1
            owned = ownedStocks[1]
            stockPrice = kmartStock
        elif stocks.lower() == "walmart": 
            tempoStocks = 2
            owned = ownedStocks[2]
            stockPrice = walmartStock
        elif stocks.lower() == "stop":
            menu()
            return
        else:
            print("Not an option!")
            print()
    print()
    print("How many stocks did you want to sell? (Or type stop at any time. )")
    print("Current owned stocks is:\n","Mc:",ownedStocks[0],
          " K:",ownedStocks[1]," W:",ownedStocks[2])
    sellStock = input()
    checkSellStock = 1
    if sellStock.lower() == "stop":
        menu()
        return
    while checkSellStock == 1:
        while not isNumber(sellStock):
            print()
            print("Please input a number or type stop at any time. ")
            sellStock = input()
            if sellStock.lower() == "stop":
                menu()
                return
        sellStock = int(sellStock)
        if sellStock > owned:
            print("You do not own enough!, You only have",owned,"in that stock.")
            sellStock = ""
        else:
            checkSellStock = 2
    moneyEarned = sellStock * stockPrice
    money += moneyEarned
    ownedStocks[tempoStocks] -= sellStock
    print()
    print("You now own $",money)
    print("Current owned stocks is:\n","Mc:",ownedStocks[0],
          " K:",ownedStocks[1]," W:",ownedStocks[2])
    menu()
        
# Sees if the argument is a number or not
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Sets the intial starting money and stocks
def main(): 
    global ownedStocks
    global money 
    ownedStocks = [10,10,10]
    money = 10000
    menu()

main()