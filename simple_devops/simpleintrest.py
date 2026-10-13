def simint(p,i,t):
    return (p*i*t)/100
if __name__=="__main__":
    p=int(input("enter principal value"))
    i=int(input("enter intrest"))
    t=int(input("enter time:"))

print("simple interst :",simint(1000,12,2))