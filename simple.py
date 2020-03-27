def sic(p,r,t):
    return (p*r*t/100)
if __name__== "__main__":
    p=int(input("enter the amount: "))
    r=int(input("enter the rate: "))
    t=int(input("enter the time: "))
    print("simple interest: "+str(sic(p,r,t)))
