def payCheckFilter(payrate, hours, daysworked):
    checkingaccount = 0
    retirementaccount = 0
    savingsaccount = 0

    paycheck = payrate * hours * daysworked

    savingsaccount += paycheck / 4
    retirementaccount += paycheck /4
    checkingaccount += paycheck * .5

    print("My paycheck for working" + str(daysworked)+ "days will be $" + str(paycheck))
    print ("saving account balance" + str(savingsaccount))
    print ("Retirment account balance" + str(retirementaccount))
    print("checking account balance" + str(checkingaccount))

#payCheckFilter(50.00, 8, 300)


def ridesharecalculator(miles, surgeprice, discount):
    Basefare = 3.00
    coastpermile = 2.00
    surgeprice = 3.75
    total = Basefare + miles * coastpermile
    if surgeprice == True:
        print("The final price for this ride is " + str(surgeprice +(miles * coastpermile)))
    else:
        print("The final price for this ride is " + str(Basefare +(miles * coastpermile)))
        if discount == True:
            discountprice = total * .35
            print("The final price for this ride is" + str(surgeprice))
    

ridesharecalculator(10, False)