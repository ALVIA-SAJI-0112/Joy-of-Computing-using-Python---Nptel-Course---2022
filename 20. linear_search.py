def linear_search(n,x):
    element=[]
    for i in range(1,1001):
        element.append(i)
    count=0
    flag=0   
    for i in element:
        if(i==x):
            print("Yes! I found my number at position:"+str(i))
            flag=1
            break;
            
    if(flag==0):
        print("Number is not found")
        
    print("Number of iterations: "+str(count))