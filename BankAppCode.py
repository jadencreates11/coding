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

payCheckFilter(50.00, 8, 300)
