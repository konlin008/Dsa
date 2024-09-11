
def rec(num):
    if(num>5):
        return num
    else:
        print(num)
        num +=1
        rec(num)
count=0
rec(count)