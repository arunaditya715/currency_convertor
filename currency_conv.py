while True:
    with open('currency_conv.txt') as f:
        lines=f.readlines()

    currencyDict={}
    for line in lines:
        parsed=line.split("\t")
        currencyDict[parsed[0]]=parsed[1]

    print(currencyDict)
    amount=eval(input("Enter The Amount:\n"))
    print('''Enter the name of currency which you would want to convert
    convert this amount to? Available Options:\n''')
    [print(item) for item in currencyDict.keys()]
    currency=input("Please Enter one of the values\n")
    print(f"{amount} INR is equal to {amount*eval(currencyDict[currency])} {currency}")
