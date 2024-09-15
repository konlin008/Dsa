def factfN(i,fact=1):
    if(i<1):
        print(fact)
        return
    else:
        fact *=i
        factfN(i-1,fact)
factfN(5)
        