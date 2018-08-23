
def fact(n):
    assert(n>0) #check condition, throws error if negative, if just does not runs
    if n==1:
        return(1) #ends recursion
    else:
        return n*fact(n-1) #return n and calls function again

# print(
# fact(1)
# ,fact(3)
# ,fact(20)
# )
#
# fact(-2)

def change(amount):
    assert(amount>=8)
    if amount==8:
        return [3,5]
    if amount==9:
        return [3,3,3]
    if amount==10:
        return [5,5]
    coins=change(amount-3) #call change again with lower amount
    coins.append(3) #add a 3 to coins each time you decrease amount by 3
    print(coins,"Amount:",amount)
    return coins

    # change(31)


def no57change(amt):
    if amt>=0:
        if amt in ([1,2,3,4,5,6,7,8,9,11,13,16,17,18]):
            return('no change')
        else:
            amt=no57no57change(amt-5)

    # if amt>0:
    #     print(amt)
    # amt=no57change(amt-5)

no57change(19)

# def s99(x):
#     if x==1:
#         return 0.5
#     else:
#         return xx=1/((2*x)-1)+s99(xx)
# s99(1)



def sum1(x):
    if(x>0):
        return(x+sum1(x-1))
    else:
        return 0
sum1(100)

def sum2(x):
    if(x>0):
        return(1/(x*(x+1)))+sum2(x-1)
    else:
        return 0

sum2(2500)


def change(amount):
  if amount == 24:
    return [5, 5, 7, 7]
  else:
    amount=amount-5
    x.append(5)
    if amount%7==0:
        for i in np.arange(1,amount/7)
        x.append(7)
        return(x)
    else change(amount-5)
    return(x)

def exact57(a):
    if(a%5==0):
        b=int(a/5)
        l=[5]*b
        return(l)
    else:
        if(a%7==0):
            c=int(a/7)
            l=[7]*c
            return(l)
        else:
            l=[]
            return(l)

def change(amount):
    assert(amount>0)
    if amount == 24:
        ll=list()
        ll=[5, 5, 7, 7]
        return(ll)
    elif len(exact57(amount))>0:
        ll=list()
        ll.extend(exact57(amount))
        return(ll)
    else:
        ll=list()
        ll.append(5)
        amount=amount-5
        ll.extend(change(amount))
        return(ll)


change(47)

change(24)
change(27)




change(27)

  else:
    amount=amount-5
    print(amount)
    x.append(5)
    if amount%7==0:
        for i in np.arange(1,amount/7):
            x.append(7)
    else:
        change(amount)
  return(x)

change(25)

x=list()
x.append(5)
x


26-5=21/7=3
27-5=22-5=17-5=12-5=7

25
55555
26
5777
27
55557
28
7777
