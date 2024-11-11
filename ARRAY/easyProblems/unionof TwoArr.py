a= [1, 2, 3, 4, 5]
b= [1, 2, 3, 6, 7]

def unionofTwoArray(a,b):
    i=0
    j=0
    unionArr=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            if not unionArr or unionArr[-1] !=a[i]:
                unionArr.append(a[i])
                i+=1
        elif b[j]<a[i]:
            if not unionArr or unionArr[-1] !=b[j]:
               unionArr.append(b[j])
               j+=1
        elif a[i]==b[j]:
            if not unionArr or unionArr[-1] !=a[i]:
               unionArr.append(a[i])
               i+=1
               j+=1
    while i<len(a):
        if not unionArr or unionArr[-1] !=a[i]:
                unionArr.append(a[i])
                i+=1
    while j<len(b):
        if not unionArr or unionArr[-1] !=b[j]:
            unionArr.append(b[j])
            j+=1          
    print(unionArr)  
    
          
unionofTwoArray(a,b)    
    