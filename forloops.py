
phoneShipment = []
doesPhonework = ""
defevtivePhones = []
for x in range(10):
    print("1 make phone case")
    print("2 solder motherboard and chips to case")
    print("3 put screen on casing")
    print("4 check if phone can turn on")
    doesPhonework = input("does this phone work?")
    if doesPhonework != "true":
        phone = "this is phone number:" + str(x)
        print("this phonw does not work")
        defevtivePhones.append(phone)
    else:
      print("5 place phone in shipment")
      phone = "this is the phone number:" + str(x)
      phoneShipment.append(phone)

    print(phoneShipment)
    print(defevtivePhones)